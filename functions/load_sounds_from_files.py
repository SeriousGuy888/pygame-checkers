import __main__ as main

def load_sounds_from_files(path_list):
    sounds = []
    for path in path_list:
        sounds.append(main.pygame.mixer.Sound(path))
    return sounds