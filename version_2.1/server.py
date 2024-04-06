import asyncio
import json
from setting import HOST, PORT, MESSAGE_SIZE
from typing import Dict

"""
HOST = "localhost"
PORT = 9999
MESSAGE_SIZE = 1024
"""

# This section imports the necessary modules and variables:
# asyncio for asynchronous IO operations,
# json for serializing and deserializing data,
# and HOST, PORT, MESSAGE_SIZE from setting.py for server configuration.


def server_function(msg:Dict)->Dict:
    pass



async def handle_echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    # This coroutine handles incoming client connections.
    while True:
        data = await reader.read(MESSAGE_SIZE)
        if not data:
            break  # Exit if connection closed/no data

        # Deserialize the incoming data to a dictionary
        msg = json.loads(data.decode())
        addr = writer.get_extra_info('peername') # Get client address.
        print(f"Received from {addr}: {msg}")

        # Respond to the client with a serialized JSON message.
        response = {"message": "Hello Buddy"}
        writer.write(json.dumps(response).encode())
        await writer.drain() # Ensure the response is sent.


    print("Closing connection")
    writer.close()  # Close the writer to end the connection.
    await writer.wait_closed() # Wait until the connection is fully closed.

async def run_server() -> None:
    # Create and start the server.
    server = await asyncio.start_server(handle_echo, HOST, PORT)
    async with server:
        await server.serve_forever() # Serve requests until manually stopped.

if __name__ == "__main__":
    # If this script is executed as the main program, run the server.
    asyncio.run(run_server())
