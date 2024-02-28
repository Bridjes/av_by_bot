import aiohttp
from .local_settings import *

# запрос на обновление данных пользователя
async def get_access(data):
    async with aiohttp.ClientSession() as session:
        async with session.post(API_GET_ACCESS, data=data) as response:
            return await response.json()

async def user_update(data, pk, headers):
    async with aiohttp.ClientSession() as session:
        async with session.patch(API_USER_UPDATE + pk, data=data, headers=headers) as response:
            return response.status
