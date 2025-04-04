import asyncio
import websockets
import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import threading

# Store last 5 messages
last_messages = []

# Serve HTML and JS


def start_http_server():
    os.chdir("public")  # Folder where index.html and script.js are
    handler = SimpleHTTPRequestHandler
    httpd = TCPServer(("0.0.0.0", 8000), handler)
    print("🌐 HTTP server running at http://localhost:8000")
    httpd.serve_forever()

# Handle WebSocket chat


async def handle_connection(websocket):
    global last_messages
    try:
        async for message in websocket:
            message = message.strip()
            if message == "GET_LAST_5":
                response = "\n".join(
                    last_messages) if last_messages else "No messages yet."
                await websocket.send(response)
            else:
                reversed_msg = message[::-1]
                last_messages.append(f"You: {message}")
                last_messages.append(f"Server: {reversed_msg}")
                if len(last_messages) > 10:
                    last_messages = last_messages[-10:]
                await websocket.send(reversed_msg)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

# Run both servers


async def main():
    # Start HTTP server in a separate thread
    http_thread = threading.Thread(target=start_http_server, daemon=True)
    http_thread.start()

    # Start WebSocket server
    async with websockets.serve(handle_connection, "0.0.0.0", 8080):
        print("🧠 WebSocket server running at ws://localhost:8080")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
