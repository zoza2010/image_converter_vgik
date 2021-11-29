from PIL import Image
import os
"""
for python 3 only
"""


def convert_image(src_path, out_path):
    try:
        im = Image.open(src_path)
        if os.path.splitext(src_path)[-1].lower() == '.png':
            im = im.convert('RGB')
        current_width, current_height = im.size
        new_width, new_height = convert_res(current_width, current_height)
        im.thumbnail((new_width, new_height), Image.ANTIALIAS)
        im.save(out_path, "JPEG")
    except IOError:
        print("cannot create thumbnail for '%s'" % src_path)


def convert_res(x, y, fit_to = 300):
    biggest = max(x, y)
    if biggest == x:
        coef = x / fit_to
        x = fit_to
        y = y / coef
    else:
        coef = y / fit_to
        x = x / coef
        y = fit_to
    return x, y


def prepare_images_for_vgik(path, ext_to = '.jpg'):
    """
    convert images to x < 300 and y < 300 and extension is jpg
    :return:
    """
    paths = [os.path.join(path, i) for i in os.listdir(path)]
    files = [i for i in paths if os.path.isfile(i)]
    if files:
        converted_files_path = os.path.join(path, 'converted')
        if not os.path.exists(converted_files_path):
            try:
                os.makedirs(converted_files_path)
            except OSError:
                raise Exception('cannot create folder for converted files: {}'.format(converted_files_path))
        for path in files:
            filename = os.path.basename(path)
            filename = os.path.splitext(filename)[0]
            out_path = os.path.join(converted_files_path, filename + ext_to)
            convert_image(path, out_path)

if __name__ == '__main__':
    path = r"C:\Users\i.zuykov\Downloads\img"
    prepare_images_for_vgik(path)