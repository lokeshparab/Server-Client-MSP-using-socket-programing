import asyncio

HOST = "localhost"
PORT = 9999

async def run_client():
    reader, writer = await asyncio.open_connection(HOST, PORT)

    # Send initial message
    writer.write(b"Hello world!")
    await writer.drain()

    # Await and print server response
    data = await reader.read(1024)
    print(f"Received: {data.decode()!r}")

    print("Closing the connection")
    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(run_client())
