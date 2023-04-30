from telethon.sync import TelegramClient
import pandas as pd

from config import teleConfig

client = TelegramClient('session_name', teleConfig.API_ID, teleConfig.API_HASH)
data = [] 

async def fetch_messages():
    await client.connect()

    async for dialog in client.iter_dialogs():
        if dialog.name == teleConfig.CHANNEL_NAME:
            entity = dialog.entity
            async for message in client.iter_messages(entity):
                data.append([message.sender_id, message.text, message.date, message.id, message.post_author, message.views, message.peer_id.channel_id ])

    await client.disconnect()

with client:
    client.loop.run_until_complete(fetch_messages())

df = pd.DataFrame(data, columns=["message.sender_id", "message.text"," message.date", "message.id",  "message.post_author", "message.views", "message.peer_id.channel_id" ])
df['simplify'] = df["message.text"].str.split('\n').str.get(2)

df.to_csv('result.csv', encoding='utf-8')