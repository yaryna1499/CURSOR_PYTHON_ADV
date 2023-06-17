import telegram
import base64
import tempfile
import os
from asgiref.sync import async_to_sync
import httpx
from django.conf import settings
from .celery import app


def save_image(encoded_image):
    decoded_image = base64.b64decode(encoded_image)
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_filename = temp_file.name
        temp_file.write(decoded_image)
    return temp_filename


url = "https://c900-188-163-32-188.ngrok-free.app/api/v2/products/"
username = "root"
password = "root"


@app.task
def run():
    async_to_sync(post_event_on_telegram)()


async def fetch_data():
    async with httpx.AsyncClient(auth=(username, password)) as client:
        response = await client.get(url)
        return response.json()


latest_data = None


async def post_event_on_telegram():
    global latest_data

    data = await fetch_data()

    if data != latest_data:
        text = f"{data[-1]['title']}\n{data[-1]['description']}\n{data[-1]['discount_price'] if data[-1]['discount_price'] is not None else data[-1]['price']}$"
        image = save_image(data[-1]["image_field"])
        bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
        await bot.send_photo(
            chat_id="@%s" % settings.TELEGRAM_CHANNEL_ID,
            photo=open(image, "rb"),
            caption=text,
        )
        os.remove(image)
        latest_data = data
