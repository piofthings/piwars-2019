import asyncio


class Timer:

    is_running = False

    def __init__(self, timeout, callback):
        self._timeout = timeout
        self._callback = callback

    def start(self):
        self.is_running = True
        self._task = asyncio.ensure_future(self._job())

    async def _job(self):
        await asyncio.sleep(self._timeout)
        await self._callback()

    def cancel(self):
        self.is_running = False
        self._task.cancel()
        self._task = None
