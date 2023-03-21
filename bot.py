
from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Basics
APP_ID = "23753568"
API_HASH = "2ed47ef64c16e55d6047c7b23fccd5ee"
SESSION = "1BJWap1wBuzf62IeNuaIiFkaiL-bom2kLqHhMxw5rodxtv1fDILUw_dq2hzkXaUUCui0Z5oMI91JdmfUe5wLPfpB3BcmazTfiqPyVLOqvZST2EsEBCBGiONTHQMW16B_qULI_yRWd6_p2COk1dwWljtiM7Y_2KtHoucJq4BqT6G5chbSjjHIYqusKG8rQ3distaTSmyPTBWFXVIHpmY2sjarnQ7Lc-JfN_0UscJupcbOdo3RY6bUX7enL31c37SoGK-uU_049O-l45KyIVnnmTSfQF5ZZUrEtGQM1aJL0vH6XSm942tXfCXQyDbwc0EGm9mjSUVBbGwmUL4jyahTMezQDQa5bJQE="
FROM_ = "-1001547964535 -1001849764929 -1001519087950 -1001219958536 -1001375911408 -1001547913290 -1001439594878 -1001342400398 -1001555098724 -1001219293084 -1001231818713 -1001251058940 -1001625691880"
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
