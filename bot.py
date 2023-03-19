
from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Basics
APP_ID = "27301339"
API_HASH = "a86efc0ff4a2a6ee01e4cf3c0825d9ed"
SESSION = "1BJWap1wBuxFnehTAW1FHdsyKfYxDN1p5dZzwVVTuV-_Y-npp30Bi3utc7MS-9dL5LQIFwaMI94y_BP-kqwHGLDDLTbw_dD3wh1UmHjdLaTQXvVPgk0yWnZYV-6dIGrePvwWaaRndTREA760e-1X8PKeFLjVha_341rSLZbd2IQrHGHrwltXXMtJ1D4sSjfcPWZ0-w_4hWcsTX9Nrtjjo6eQ1aIkvuVW3PXQ50X0_5ewkOA2LXUHYdbpCIJhrOQmNDqMc7Lc6iOV14ES9W_WTshMlZuqtVvcJkQpVqphM8Yz3u2C9rOULQosYIKy5ySav0CIoEI4DF6BBvlcyp-QBceZQ9OmttwU="
#first two ids for trial
FROM_ = "-1001519087950 -1001219958536 -1001375911408 -1001547913290 -1001439594878 -1001342400398 -1001555098724 -1001219293084 -1001231818713 -1001251058940 -1001625691880"
TO_ = "-1001962040653"

FROM = [int(i) for i in FROM_.split()]
TO = [int(i) for i in TO_.split()]

try:
    BotzHubUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    BotzHubUser.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

@BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    for i in TO:
        try:
            await BotzHubUser.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)

print("Bot has started.")
BotzHubUser.run_until_disconnected()
