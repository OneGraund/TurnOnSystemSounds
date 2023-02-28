import mouse
import time
import pyautogui

VOLUME_COORDS = (1708, 1601)
OPENMIXER_COORDS = (1800, 970)
MUTE_COORDS = (1620,983)
DELAY = 5

def check_if_muted():
    """Can return either "CustomerReady" or "WhiteScreen\""""
    """Checking color of pixels"""

    r,g,b = pyautogui.pixel(MUTE_COORDS[0], MUTE_COORDS[1])
    if r>=237 and g<=20 and b<=20:
        print('System sounds are muted')
        return True
    else:
        print(
            'System sounds are not muted'
        )
        return False

def unmute_sounds():
    pyautogui.press('win')
    mouse.move(-10000,-10000, absolute=False, duration=0.1)
    mouse.move(VOLUME_COORDS[0], VOLUME_COORDS[1], absolute=False, duration=0.1)
    mouse.click('right')
    # press the volume icon
    time.sleep(1)
    mouse.move(-10000,-10000, absolute=False, duration=0.1)
    mouse.move(OPENMIXER_COORDS[0], OPENMIXER_COORDS[1], absolute=False, duration=0.1)
    mouse.click('left')
    time.sleep(1)
    # press open mixer button
    mouse.move(-10000,-10000, absolute=False, duration=0.1)
    mouse.move(MUTE_COORDS[0], MUTE_COORDS[1],absolute=False, duration=0.1)
    time.sleep(0.5)
    if check_if_muted()==True:
        mouse.click('left')
        mouse.move(-10000,-10000, absolute=False, duration=0.1)
        mouse.move(80, 800, absolute=False,duration=0.1)
        time.sleep(1)
        mouse.click('left')
    else:
        mouse.move(-10000, -10000, absolute=False, duration=0.1)
        mouse.move(80, 800, absolute=False, duration=0.1)
        mouse.click('left')


while True:
    unmute_sounds()
    time.sleep(60*DELAY)