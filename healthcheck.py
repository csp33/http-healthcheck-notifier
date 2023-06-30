import asyncio
import os

import requests
import telegram

telegram_token = os.environ["TELEGRAM_TOKEN"]
telegram_chat_id = os.environ["TELEGRAM_DESTINATION_CHAT_ID"]
endpoint_url = os.environ["URL_TO_CHECK"]


async def send_telegram_message(message):
    bot = telegram.Bot(token=telegram_token)
    await bot.send_message(chat_id=telegram_chat_id, text=message)


async def check_remote_server():
    try:
        response = requests.get(endpoint_url, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        await send_telegram_message(f"Unable to connect to {endpoint_url}")
        print("Server is not available. Telegram message sent.")


if __name__ == "__main__":
    asyncio.run(check_remote_server())
