# python
"""
Opensea Crayon AmongUs series.
A unique series of ~24 suspicious characters. HIGHLY COLLECTIBLE. LIMITED EDITION.
"""
from PIL import Image
import os

def get_paths(dir_path):
    paths = []

    absolute_dir_path = os.getcwd() + dir_path

    for roots, dirs, files in os.walk(absolute_dir_path):
        for f in files:
            paths.append(f"{absolute_dir_path}/{f}")

    print(f"* Found {len(paths)} files in {absolute_dir_path}")

    return paths

def mutate(fg_paths, bg_paths, save_dir):
    """ generate all permutations of foregrounds and backgrounds """

    print(f"! Mutating {len(fg_paths)} foregrounds and {len(bg_paths)} backgrounds")

    absolute_save_dir = os.getcwd() + save_dir
    
    for a, fg in enumerate(fg_paths):
        fg_img = Image.open(fg)
        fg_img = fg_img.convert("RGBA")
        
        for b, bg in enumerate(bg_paths):
            bg_img = Image.open(bg)
            bg_img = bg_img.convert("RGBA")

            bg_img.paste(fg_img, (0,0), fg_img)
            
            bg_img.save(f'{absolute_save_dir}/{a}_{b}.png', format="png")

            print(f'* Created: {absolute_save_dir}/{a}_{b}.png')

def holo(img_path, holo_path, save_dir):
    """ generate a single holo for a given image/holo """

    print("! Running mutate() with Holo wrapper")

    # run mutate function, but for single fg/bg set, not multiple paths
    mutate([holo_path], [img_path], save_dir)

if __name__ == "__main__":
    bg_paths = get_paths("/assets/bg")
    fg_paths = get_paths("/assets/fg")
    holo_paths = get_paths("/assets/holo")
    
    save_dir = "/assets/assets"

    mutate(fg_paths, bg_paths, save_dir)
