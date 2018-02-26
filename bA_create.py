from PIL import Image, ImageColor, ImageSequence
import numpy as np
import cv2

video_path = 'badApple.mp4'

# def img_process(img_array):
#     results = ''
#     for x in range(0, img_array.shape[0], 4):
#         for y in range(0, img_array.shape[1], 4):
#             if (img_array[x][y][1] == 0 or img_array[x][y][0] > 200):
#                 results += '++'
#             else:
#                 results += '##'
#         results += '\n'
#     return results
    

# def init():
#     im = Image.open(im_path)
#     index = 1
#     f = open('text.txt', 'w+')
#     all = []
#     for frame in ImageSequence.Iterator(im):
#         print(type(frame))
#         frame = frame.convert('LA')
#         img_data = img_process(frame)
#         all.append(img_data)
#         index += 1
#         if index > 1:
#             break
#     f.write(all[0])

def main():
    index = 0
    cap = cv2.VideoCapture(video_path)
    while(True):
        ret, frame = cap.read()
        if ret == False:
            break
        # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imwrite('./screenshot/shot_{}.jpg'.format(index), frame)
        index += 1
        print('shot_: {}'.format(index))

if __name__ == '__main__':
    main()