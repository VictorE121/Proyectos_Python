from os import system
import asyncio
import time
import keyboard as kb

from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager

async def get_media_info():

    sessions = await MediaManager.request_async()

    current_sesion = sessions.get_current_session()

    Break = False

    if current_sesion:

        info = await current_sesion.try_get_media_properties_async()
        playback_info = current_sesion.get_playback_info()
        timeline = current_sesion.get_timeline_properties()

    while True:
        if kb.is_pressed("Q") and not Break:
            print(f"La Rompimo")
            Break = True
            break
        
        print(f"Hola...")
        time.sleep(1)
#        while True:
#
#            actual_time = timeline.position.total_seconds()
#            time_end = timeline.end_time.total_seconds()        
#
#            system("cls")
#            while actual_time < time_end:
#                print(f"Tiempo: ",actual_time, "Segundos")
#                time.sleep(2)
#            
#            if kb.is_pressed("q"):
#                break
#            else:
#                continue
        


    else:
        print("No se encontro Sesion...")

asyncio.run(get_media_info())