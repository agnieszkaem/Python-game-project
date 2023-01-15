import time

from PIL import Image

def read_img(name):
    """
    Function responsible for reading and showing the image at the end of the game
    """
    im = Image.open(name, "r")
    im.show()



def read_file(name):
    """
    Function reads the file with the game introduction
    """
    f = open(name,"r")
    lines = f.readlines()
    for line in lines:
        print(line)
        time.sleep(2.5)
        
    f.close()