import os, sys
from PIL import Image, ImageColor
import numpy as np
import glob
import html
from math import floor

pixels_ramp = '@%#*+=-:. '

class TextAnimation:
    def __init__(self, dir, vwidth, vheight):
        self.picFile = glob.glob(sys.argv[1]+'/*.jpg')
        self.resultList = ''
        self.width = int(vwidth)
        self.height = int(vheight)
        self.file = open('index.html', 'w+')
        self.count = 0
    
    def pic2Text(self, img):
        string = ''
        for row in range(1, img.shape[0]-1):
            for col in range(1, img.shape[1]-1):
                pixel = np.sum(img[row-1:row+2, col-1:col+2])
                pixel = pixel/9
                string += pixels_ramp[int(floor(pixel/25.6))]
            string += '\n'
        return string


    def convert(self):
        self.picFile = sorted(self.picFile, key=lambda x: int(x.split('.')[0].split('_')[1]))
        self.writeToHTML_head()
        for im_path in self.picFile:
            img = Image.open(im_path)
            size = (self.width+2, self.height+2)
            img = img.resize(size)
            img = img.convert('L')
            text = html.escape(self.pic2Text(np.asarray(img)))
            self.file.write('<pre id = "frame{}">'.format(self.count))
            self.file.write(text)
            self.file.write('</pre>')
            self.count += 1
            print('{} complete!'.format(im_path))
        self.writeToHTML_foot()
        return
    
    def writeToHTML_head(self):
        head = \
        '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Document</title>
            <style>
                pre {display: none}
            </style>
        </head>
        <body>
            <div style="float:left; padding-right: 30px;">
        '''
        self.file.write(head)

    def writeToHTML_foot(self):
        self.file.write('<pre id="num">{}</pre>\n</div>'.format(self.count))
        foot = \
        '''
        <video id="vid" width="480" height="320" style="padding: 10px">
             <source src="./static/badApple.mp4" type="video/mp4">
        </video>
        <script type="text/javascript" src="./static/run.js"></script>
        </body>
        </html>
        '''
        self.file.write(foot)
        self.file.close()

def error_handler(error_code):
    if error_code == 0:
        print("Argument number not correct!")
    elif error_code == 1:
        print("Something wrong with the arguments")

def main():
    if not len(sys.argv) == 4:
        error_handler(0)
        return
    if not os.path.isdir(sys.argv[1]):
        error_handler(1)
        return
    myHTML = TextAnimation(sys.argv[1], sys.argv[2], sys.argv[3])
    myHTML.convert()

if __name__=='__main__':
    main()