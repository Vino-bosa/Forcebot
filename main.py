from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

api_id = 21301308
api_hash = "6732b981f6febcf8312ee2fe560b48af"
bot_token = "7994001764:AAHf_gIj5O2rvscO7BvYlYH6wC0ikFkb4LU"

CHANNEL_USERNAME = "forgeutamaa"  # tanpa @

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    user = message.from_user.id
    try:
        member = await client.get_chat_member(CHANNEL_USERNAME, user)
        if member.status in ["member", "administrator", "creator"]:
            await message.reply_video(
                video="https://file-examples.com/wp-content/uploads/2018/04/file_example_MP4_480_1_5MG.mp4",
                caption="✅ Berikut videomu, terima kasih sudah join!"
            )
        else:
            raise Exception()
    except:
        buttons = InlineKeyboardMarkup([[
            InlineKeyboardButton("🔔 Join Channel", url=f"https://t.me/{CHANNEL_USERNAME}")
        ]])
        await message.reply(
            "❗ Kamu harus join channel dulu sebelum bisa akses video!",
            reply_markup=buttons
        )

app.run()
