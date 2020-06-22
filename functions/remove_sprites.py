import __main__ as main

def remove_sprites():
    sprites = [main.pieces, main.king_pieces, main.ghost_pieces, main.squares, main.red_jumped_pieces, main.black_jumped_pieces]

    for sprite in sprites:
        sprite.clear()