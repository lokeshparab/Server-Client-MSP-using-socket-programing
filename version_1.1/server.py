import asyncio

HOST = "localhost"
PORT = 9999

async def handle_echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    data = True  # Initialize with a truthy value to enter the loop
    while data :
        data = await reader.read(1024)
        if not data:
            break  # Exit if connection closed/no data
        msg = data.decode()

        addr = writer.get_extra_info('peername')
        print(f"Received from {addr}: {msg!r}")

        response = b"Hello Buddy"
        writer.write(response)
        await writer.drain()

    print("Closing connection")
    writer.close()
    await writer.wait_closed()

async def run_server() -> None:
    server = await asyncio.start_server(handle_echo, HOST, PORT)
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(run_server())
