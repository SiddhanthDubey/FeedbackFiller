from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


def pressTab():
    keyboard.press(Key.tab)

    keyboard.release(Key.tab)


def pressDown():
    keyboard.press(Key.down)

    keyboard.release(Key.down)


def fill_feedback():
    pressDown()
    time.sleep(2.5)
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressTab()


def fill_text():
    keyboard.press('N')
    keyboard.release('N')
    keyboard.press('A')
    keyboard.release('A')
    pressTab()
    pressTab()
    pressTab()


theory_count = int(input("Tell the amount of theory classes : "))
lab_count = int(input("Tell the amount of lab (practical) classes : "))

print("Get ready, and point your cursor at the first index position...")
time.sleep(3)


for a in range(theory_count):
    for i in range(14):
        fill_feedback()
    fill_text()

pressTab()
pressTab()

for a in range(lab_count):
    for i in range(13):
        fill_feedback()
    fill_text()
