from os import system
import asyncio

from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager


async def get_media_info():
    sessions = await MediaManager.request_async()

    current_session = sessions.get_current_session()

    if current_session:
        info = await current_session.try_get_media_properties_async()
        plyback_info = current_session.get_playback_info()
        timeline = current_session.get_timeline_properties()

        system("cls")
        print(f"TITULO: ", info.title)
        print(f"ARTIST: ", info.artist)
        print(f"ESTADO: ", plyback_info.playback_status)
        print(f"TIEMPO ACTUAL: ", timeline.position.total_seconds(), "segundos")
        print(f"TIEMPO TOTAL: ", timeline.end_time.total_seconds(), "Segundos")

    else:
        print("Sesion no Encontrada")


asyncio.run(get_media_info())