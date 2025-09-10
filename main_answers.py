from PIL import Image
from PIL import ImageFilter
#for bonus task
from PIL import ImageEnhance

with Image.open('original.jpg') as pic_original:
    print('Image is open\nSize:', pic_original.size)
    print('Format:', pic_original.format)
    print('Type:', pic_original.mode) #colored
    pic_original.show()

    pic_gray = pic_original.convert('L')    
    pic_gray.save('gray.jpg')
    print('Image is created\nSize:', pic_gray.size)
    print('Format:', pic_gray.format)
    print('Type:', pic_gray.mode) #black and white
    pic_gray.show()

    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save('blured.jpg')
    pic_blured.show()

    pic_up = pic_original.transpose(Image.ROTATE_180)
    pic_up.save('up.jpg')
    pic_up.show()


    #бонус 1. Mirror reflection
    pic_mirrow = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    pic_mirrow.save('mirrow.jpg')
    pic_mirrow.show()

    #бонус 2. Increasing contrast 
    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(1.5)
    pic_contrast.save('contr.jpg')
    pic_contrast.show()