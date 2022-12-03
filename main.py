import asyncio
from pyrogram import Client
import mylast
from mylast import lastfm_network, lastfm_username

api_id = xx
api_hash = "xx"


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        last_played = None
        while True:
            try:
                now_playing = lastfm_network.get_user(lastfm_username).get_now_playing()
            except:
                pass
            if now_playing != last_played:
                last_played = now_playing
                if now_playing:
                    print(now_playing)
                    await app.update_profile(last_name="| ♪ "
                                                       + str(now_playing).split(" - ")[1]
                                                       + " - "
                                                       + str(now_playing).split(" - ")[0])

asyncio.run(main())
