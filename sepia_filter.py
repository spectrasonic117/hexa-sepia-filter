from PIL import Image
import os

def apply_sepia_filter(image_path):
    img = Image.open(image_path)
    # convert img to RGBA if its not
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    # define sepia filter color
    sepia_filter = (
        (0.393, 0.769, 0.189),
        (0.349, 0.686, 0.168),
        (0.272, 0.534, 0.131)
    )

    # Apply filter
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b, a = img.getpixel((x, y))
            if a != 0:  # alpha channel is not 0
                new_r = min(int(r * sepia_filter[0][0] + g * sepia_filter[0][1] + b * sepia_filter[0][2]), 255)
                new_g = min(int(r * sepia_filter[1][0] + g * sepia_filter[1][1] + b * sepia_filter[1][2]), 255)
                new_b = min(int(r * sepia_filter[2][0] + g * sepia_filter[2][1] + b * sepia_filter[2][2]), 255)
                img.putpixel((x, y), (new_r, new_g, new_b, a))

    # save image
    # sepia_image_path = os.path.splitext(image_path)[0]+"_sepia.png"
    img.save(image_path)
    print(f"Se ha aplicado el filtro sepia a: {image_path}")

def main():
    # get current dir and walk through all files in dir
    current_directory = os.getcwd()
    for root, dirs, files in os.walk(current_directory):
        for file in files:
            if file.endswith(".png"):
                image_path = os.path.join(root, file)
                apply_sepia_filter(image_path)

if __name__ == "__main__":
    main()
