import __main__ as main

app_id = "cheezydevs.donutcheckers"
main.ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
main.pygame.display.set_icon(main.pygame.image.load("./assets/textures/icon.png"))
main.pygame.display.set_caption("Donut Checkers")