import mouse
from PIL import ImageGrab
import time
import pyautogui

VOLUME_COORDS = (1708, 1601)
OPENMIXER_COORDS = (1787, 940)
MUTE_COORDS = (1627,981)

def check_if_muted():
    """Can return either "CustomerReady" or "WhiteScreen\""""
    """Checking color of pixels"""

    def getHex(rgb):
        return '%02X%02X%02X' % rgb

    bbox = (MUTE_COORDS[0], MUTE_COORDS[1], MUTE_COORDS[0] + 1, MUTE_COORDS[1] + 1)
    im = ImageGrab.grab(bbox=bbox)
    rgbim = im.convert('RGB')
    r, g, b = rgbim.getpixel((0, 0))
    print(f'COLOR: rgb{(r, g, b)} | HEX #{getHex((r, g, b))}')
    if r>=237 and g<=20 and b<=20:
        return True
    else:
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
        mouse.move(999, 515, absolute=False,duration=0.1)
        time.sleep(1)
        mouse.click('left')
    else:
        mouse.move(-10000, -10000, absolute=False, duration=0.1)
        mouse.move(999, 515, absolute=False, duration=0.1)
        mouse.click('left')


while True:
    unmute_sounds()
    time.sleep(60*5)