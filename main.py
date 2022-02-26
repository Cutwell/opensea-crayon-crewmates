# python
"""
Opensea Crayon AmongUs series.
A unique series of ~24 suspicious characters. HIGHLY COLLECTIBLE. LIMITED EDITION.
"""
from PIL import Image, ImageSequence
import os

def get_paths(dir_path):
    paths = []

    absolute_dir_path = os.getcwd() + dir_path

    print(f"! Gathering files within {absolute_dir_path}")

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

def holo(bg_paths, fg_paths, save_dir):
    """ generate a single holo for a given image/holo """

    print(f"! Applying {len(fg_paths)} holos to {len(bg_paths)} images")

    absolute_save_dir = os.getcwd() + save_dir

    for a, bg in enumerate(bg_paths):
        bg_img = Image.open(bg)
        bg_img = bg_img.convert("RGBA")

        img_w, img_h = bg_img.size
            
        for b, fg in enumerate(fg_paths):
            fg_img = Image.open(fg)

            frames = []

            base_frame = fg_img.copy().convert("RGBA")
            base_frame.putalpha(64)

            for frame in ImageSequence.Iterator(fg_img):
                frame = frame.convert("RGBA")
                frame.putalpha(64)
            
                layer = Image.new('RGBA', (img_w, img_h), (0, 0, 0, 0))
                
                layer.paste(bg_img, (0,0), mask=bg_img)

                layer.paste(base_frame, (0,0), mask=base_frame)
            
                layer.paste(frame, (0,0), mask=frame)

                #layer = Image.blend(bg_img, frame, alpha=0.5)
            
                frames.append(layer)

            frames[0].save(
                f'{absolute_save_dir}/{a}_{b}.gif',
                save_all=True,
                append_images=frames[1:],
                duration=80,
                loop=1,
                optimize=False
            )
    
            print(f'* Created: {absolute_save_dir}/{a}_{b}.gif')

def resize(asset_paths, save_dir, size):
    """ Resize images to set image size and export to new directory """
    
    print("! Resizing images")

    w, h = size

    absolute_save_dir = os.getcwd() + save_dir

    for path in asset_paths:

        img = Image.open(path).convert("RGBA").resize((w, h))
        
        img_basename = os.path.basename(path)
    
        img.save(f'{absolute_save_dir}/{img_basename}', format="png")
    
        print(f'* Resized: {absolute_save_dir}/{img_basename}')
    

if __name__ == "__main__":
    #bg_paths = get_paths("/assets/bg")
    #fg_paths = get_paths("/assets/fg")
    holo_paths = get_paths("/assets/holo")
    #asset_paths = get_paths("/assets/assets")
    resize_paths = get_paths("/assets/resize")
    
    #save_dir = "/assets/assets"
    #save_dir = "/assets/resize"
    save_dir = "/assets/shiny"

    #mutate(fg_paths, bg_paths, save_dir)
    #resize(asset_paths, save_dir, (560, 560))
    holo(resize_paths, holo_paths, save_dir)
