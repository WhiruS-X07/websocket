# WebSocket Chat App

This is a simple WebSocket-based chat application where users can send messages, receive responses from the server (which reverses the text), and fetch the last 5 messages exchanged.

## Project Structure

```
-- server.py
-- public
   -- index.html
   -- script.js
-- README.md
```

## Features

- Users can send messages via WebSockets.
- The server reverses the text and sends it back.
- The last 5 messages (including user inputs and server responses) are stored.
- Users can request the last 5 messages at any time.

## Prerequisites

Make sure you have Python installed (version 3.7 or higher recommended).

Install required Python dependencies:

```sh
pip install websockets flask
```

## How to Run

1. **Start the server**

   Run the following command in the root folder (where `server.py` is located):

   ```sh
   python server.py
   ```

   This will start a WebSocket server on `ws://localhost:8080` and also serve the frontend via Flask.

2. **Open the Frontend**

   - The frontend will automatically open after starting the server.
   - If it doesn't, manually open your browser and go to:
     
     ```
     http://localhost:8000
     ```

   - The chat interface should be displayed.

## Troubleshooting

- If `localhost` is not working:
  - Stop the server (press `Ctrl + C` in the terminal)
  - Close the terminal
  - Reopen it and run `python server.py` again.

- If you see a WebSocket error, ensure the server is running before opening the frontend.

## How It Works

1. When a user sends a message, it is sent to the WebSocket server.
2. The server reverses the message and sends it back.
3. The last 5 messages (both user and server responses) are stored.
4. Clicking "Get Last 5 Messages" retrieves and displays them.

## Future Improvements

- Add support for multiple users.
- Implement message timestamps.
- Enhance UI with better styling.

