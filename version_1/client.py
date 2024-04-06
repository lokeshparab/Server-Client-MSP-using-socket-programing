import asyncio

HOST = "localhost"
PORT = 9999

async def run_client():
    reader, writer = await asyncio.open_connection(HOST,PORT)


    # Send command and arguments to the server
    writer.write(b"Hello world!")
    await  writer.drain()

    while True:
        data = await reader.read(1024)

        if not data:
             raise Exception("socket closed")
        
        print(f"Received: {data.decode()!r}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_client())
