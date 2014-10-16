import Tkinter
from PIL import Image, ImageDraw, ImageTk
from random import randint

class generativeImg:

  def generate(self, urls, q):

    print urls
    generalCount = 0
    countX = 0
    countY = 0
    savePosX = 0
    savePosY = 0
    pixRange = 1500

    size = (500,200)
    newIm = Image.new('RGB', size, (0,0,0)) # create the image
    draw = ImageDraw.Draw(newIm)

    for items in urls:

      im = Image.open(q+"/"+str(generalCount)+".jpg")
      rgb_im = im.convert('RGB')
      width, height = im.size
      print "Size of image: "+str(im.size)

      for pix in range(pixRange):
        r, g, b = rgb_im.getpixel((randint(1,width-1), randint(1,height-1)))
        print "RGB Values of pixel: "+ str(r),str(g),str(b)
        draw.point((countX,countY), fill=(r,g,b))
        if countX > width:
          countX = 0
          countY +=1
        countX+=1
      generalCount+=1

    newIm.show()
    newIm.save("test", "JPEG")
