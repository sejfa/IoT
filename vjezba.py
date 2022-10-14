from PIL import Image


def get_image(gui_name, image_name):
    root_folder_path = './moj_najbolji_projekt_folder/media'
    return Image.open(f"{root_folder_path}/{gui_name}/{image_name}")


get_image('login', 'basil.jpg')
get_image('hosta', 'hosta.jpg')
