import asyncio

HOST = "localhost"
PORT = 9999

async def handle_echo(reader:asyncio.StreamReader,writer:asyncio.StreamWriter) ->None:
    data = None

    while data != b"quit":
        data = await reader.read(1024)
        msg = data.decode()

        addr = writer.get_extra_info('peername')

        print(f"Message from {addr} --> {msg!r}")

        writer.write(b"Hello Buddy")
        await writer.drain()

    writer.close()
    await writer.wait_closed()

async def run_server()->None:
    server = await asyncio.start_server(handle_echo,HOST,PORT)
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_server())