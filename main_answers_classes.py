from PIL import Image
from PIL import ImageFilter

class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = list()

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('¡No se encuentra el archivo!')
        self.original.show()

    def do_left(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)

    #prima. Denominación automática para imágenes editadas
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'

        rotated.save(new_filename)

#prima. recortó la imagen del bebé koala
    def do_cropped(self):
        box = (250, 100, 600, 400) #izquierda, arriba, derecha, abajo
        cropped = self.original.crop(box)
        self.changed.append(cropped)

#prima. Denominación automática para imágenes editadas
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'

        cropped.save(new_filename)

MyImage = ImageEditor('original.jpg')
MyImage.open()

MyImage.do_left()
MyImage.do_cropped()

for im in MyImage.changed:
    im.show()