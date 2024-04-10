import asyncio
import argparse
import json
from setting import HOST, PORT, MESSAGE_SIZE

""" Central Machine """
"""
HOST = "localhost"
PORT = 9999
MESSAGE_SIZE = 1024
"""
# Command line argument parsing
parser = argparse.ArgumentParser(description='Asyncio Server')
parser.add_argument('--h', type=str, default=HOST, help='Host address')
parser.add_argument('-p', '--port', type=int, default=PORT, help='Port number')
parser.add_argument('--message_size', type=int, default=MESSAGE_SIZE, help='Size of the message buffer')

args = parser.parse_args()

HOST = args.h
PORT = args.port
MESSAGE_SIZE = args.message_size

# This section imports necessary modules and variables.
# asyncio for asynchronous IO operations,
# json for serializing and deserializing data,
# and HOST, PORT, MESSAGE_SIZE from the setting.py file for configuration.

async def run_client():
    # Establishes a connection to the server using the host and port specified in the settings.
    reader, writer = await asyncio.open_connection(HOST, PORT)
    
    for a,b in [(1,2),(3,4)]:
        # Create a message dictionary and serialize it to a JSON string
        message = {"a": a ,"b":b,  "content": f"Hello world!"}
        writer.write(json.dumps(message).encode())
        await writer.drain() # Ensures the message is sent.

        # Await and print server response
        # Reads data from the connection up to MESSAGE_SIZE bytes.
        data = await reader.read(MESSAGE_SIZE)
        
        # Deserialize the incoming data from JSON format to a dictionary.
        response = json.loads(data.decode())  
        print(f"Received: {response}")

        print("Closing the connection")
    writer.close()  # Close the connection.
    await writer.wait_closed() # Wait until the connection is fully closed.

if __name__ == "__main__":
    # If this script is executed as the main program, the run_client coroutine is run.
    asyncio.run(run_client())
