import asyncio
import websockets

# Store last 5 messages
last_messages = []

async def handle_connection(websocket):  
    global last_messages
    try:
        async for message in websocket:
            message = message.strip()  # Remove extra spaces/newlines

            if message == "GET_LAST_5":
                # Send the last 5 messages joined with new lines
                response = "\n".join(last_messages) if last_messages else "No messages yet."
                await websocket.send(response)
            else:
                # Reverse the message
                reversed_msg = message[::-1]

                # Store the original message (for user view) and reversed message (for server response)
                last_messages.append(f"You: {message}")  # Store user message
                last_messages.append(f"Server: {reversed_msg}")  # Store server response

                # Keep only the last 5 messages
                if len(last_messages) > 10:  # Since each input generates 2 messages
                    last_messages = last_messages[-10:]

                await websocket.send(reversed_msg)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

# Start WebSocket server
async def main():
    async with websockets.serve(handle_connection, "localhost", 8080):  
        print("✅ WebSocket server running on ws://localhost:8080")
        await asyncio.Future()  # Keep server running

if __name__ == "__main__":
    asyncio.run(main())
