import __main__ as main

user32 = main.ctypes.windll.user32

main.SCREEN_WIDTH = user32.GetSystemMetrics(0)
main.SCREEN_HEIGHT = user32.GetSystemMetrics(1)