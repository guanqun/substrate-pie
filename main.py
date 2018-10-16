import aiohttp
import logging
import asyncio as ai
import aiotk
import json

logger = logging.getLogger(__name__)


class Rpc:
    def __init__(self):
        self.ws = None

    async def run(self):
        async with aiohttp.ClientSession() as sess:
            self.ws = await sess.ws_connect(url="ws://127.0.0.1:9944",
                                            autoclose=True,
                                            autoping=True)
            print("connected.")

            msg = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "state_getMetadata",
                "params": []
            }
            print(json.dumps(msg))
            await self.ws.send_json(msg)

            msg = await ai.wait_for(self.ws.receive(), timeout=None)

            print(msg)

    async def get_messages(self):

        msg = await ai.wait_for(self.ws.receive(), timeout=None)

        print(msg)

        # await self.ws.send_str()


if __name__ == '__main__':
    rpc = Rpc()
    aiotk.run_until_complete(rpc.run())
