import asyncio
import json
import logging

from abc import abstractmethod
from asyncio.streams import StreamReader, StreamWriter






async def main():
    # processor = CommandProcessor(MemoryStorage())

    # запускаем сервер на localhost:3333
    server = await asyncio.start_server('localhost', 3333)
    logging.info('Server started')

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    # Logger.configure_logger('tcp_server_example')

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Server stopped')