import os
from PIL import Image

def make_background_transparent(img_path, output_path, bg_color=(255, 255, 255)):
    img = Image.open(img_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        if item[0] >= bg_color[0] and item[1] >= bg_color[1] and item[2] >= bg_color[2]:
            new_data.append((255, 255, 255, 0))  # transparente
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path)

input_folder = '.'  # carpeta actual
output_folder = './run_frames_transparent'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.png'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        make_background_transparent(input_path, output_path)
        print(f'Procesado {filename}')
