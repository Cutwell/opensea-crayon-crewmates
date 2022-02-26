# python
"""
Opensea Crayon AmongUs series.
A unique series of ~24 suspicious characters. HIGHLY COLLECTIBLE. LIMITED EDITION.
"""
from PIL import Image
import os

def get_paths(dir_path):
    paths = []

    for roots, dirs, files in os.walk(dir_path):
        for f in files:
            paths.append(f)

    return paths

def mutate(fg_paths, bg_paths, save_dir):
    """ generate all permutations of foregrounds and backgrounds """
    
    for a, fg in enumerate(fg_array):
        fg_img = Image.open(fg)
        for b, bg in enumerate(bg_array):
            bg_img = Image.open(bg)

            bg_img.paste(fg_img)
            bg_img.save(f'{save_dir}/{a}_{b}.png')

def holo(img_path, holo_path, save_dir):
    """ generate a single holo for a given image/holo """

    # run mutate function, but for single fg/bg set, not multiple paths
    mutate([holo_path], [img_path], save_dir)

if __name__ == "__main__":
    bg_paths = get_paths("/assets/bg")
    fg_paths = get_paths("/assets/fg")
    holo_paths = get_paths("/assets/holo")
    
    save_dir = "/assets/assets"

    mutate(bg_paths, fg_paths, save_dir)
