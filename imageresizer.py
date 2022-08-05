from PIL import Image
import os

def resize():
    resolution = int(input("Enter Resolution: "))
    dpi = int(input("Enter Dpi: "))
    directory = 'images'
    i = 0
    for file in os.listdir(directory):
        i += 1
        os.chdir(r'/home/navneet/Documents/Python Projects/ImageResizer/images')
        im = Image.open(file)
        rgb_im = im.convert("RGB")
        wpercent = (resolution/float(rgb_im.size[0]))
        hsize = int((float(rgb_im.size[1])*float(wpercent)))
        rgb_im = rgb_im.resize((resolution, hsize), Image.ANTIALIAS)
        os.chdir(r'/home/navneet/Documents/Python Projects/ImageResizer/resized_images')
        rgb_im.save(f"{file}_resized.jpg", dpi=(dpi, dpi))
        
    print(f'{i} images resized.')

resize()