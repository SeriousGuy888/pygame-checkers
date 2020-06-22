import __main__ as main

def show_text(font_file, font_size, text_colour, coords, string):
    font = main.pygame.font.Font(font_file, font_size)

    text = font.render(string, True, text_colour)
    text_rect = text.get_rect()
    text_rect.center = (x, y) = coords

    return {"text": text, "rect": text_rect}