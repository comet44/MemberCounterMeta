
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import asyncio
from datetime import datetime , timedelta
import pytz
from texts.texts_teletips import *

MemberCounterMeta = Client(
    name = "membercountermeta",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)

CHANNEL_OR_GROUP_LIST = [i.strip() for i in os.environ.get("CHANNEL_OR_GROUP_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
BOT_CHANNEL_OR_GROUP_ID = int(os.environ["BOT_CHANNEL_OR_GROUP_ID"])
BOT_MESSAGE_ID = int(os.environ["BOT_MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]
C_MESSAGE_ID = int(os.environ["C_MESSAGE_ID"])



async def main_MemberCounterMeta():
    async with MemberCounterMeta:
        try:
            while True:
                print(text_2)
                

                for CHANNEL_OR_GROUP in CHANNEL_OR_GROUP_LIST:
                    try:
                        time = datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                        last_update = time.strftime(f"%Y-%m-%d %H:%M:%S")
                        xxx_teletips += f"\n\n⌛️ Last checked on: {last_update} ({TIME_ZONE})\n\n<i>♻️ Refreshes automatically Every 45 Minutues</i>"
                        await MemberCounterMeta.edit_message_text(int(BOT_CHANNEL_OR_GROUP_ID), BOT_MESSAGE_ID, xxx_teletips)
                        print(f"Last checked on: {last_update}")
                        await MemberCounterMeta.send_message(int(bot_admin_id), f"Last checked on: {last_update}")
                        await asyncio.sleep(7)
                        print(f"trying to do countdown")
                        desired_timezone_c = 'Asia/Kolkata'
                        target_date = datetime(2024, 5, 4, 23, 59, 59 , tzinfo=pytz.timezone(desired_timezone_c))
                        current_time_c = datetime.now(pytz.timezone(desired_timezone_c))
                        remaining_time = target_date - current_time_c  # Use 'Asia/Kolkata' for Indian Standard Time

                        if remaining_time.total_seconds() <= 0:
                            print("Countdown reached zero.")
                        else: 
                            total_seconds = remaining_time.total_seconds()
                            days, seconds_remaining = divmod(total_seconds, 86400)
                            hours, seconds_remaining = divmod(seconds_remaining, 3600)
                            minutes, seconds = divmod(seconds_remaining, 60)
                        countdown_message = (f"🌀**COUNTDOWN FOR NEET 2024 to 5 May, 2024** \n\n **Time Left**: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds \n\n  \n\n <i>♻️ Refreshes automatically  </i>")
                        await MemberCounterMeta.edit_message_text(int(BOT_CHANNEL_OR_GROUP_ID), C_MESSAGE_ID, countdown_message)
                        print(f"COUNTDOWN FOR NEET 2024 to 5 May, 2024 \n\n Time Left: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds \n\n  ")
                        await asyncio.sleep(10)  # 15 minutes = 900 seconds # 15 minutes = 900 seconds
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
        except Exception as e:
            print(f"An error occurred: {e}")
@MemberCounterMeta.on_message(filters.command("status", "!") & filters.me)
async def alive(_, message: Message):
    await message.edit("Your MemberCounter is alive!")
    await asyncio.sleep(10)
    await message.delete()               


MemberCounterMeta.run(main_MemberCounterMeta())
