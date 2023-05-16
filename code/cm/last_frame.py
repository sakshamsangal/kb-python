# Importing all necessary libraries
import glob

import cv2
import os


def mov_to_jpg(fp, fn):
    # Read the video from specified path
    cam = cv2.VideoCapture(fp)

    try:

        # creating a folder named data
        if not os.path.exists('data'):
            os.makedirs('data')

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    # frame
    currentframe = 0
    ls = []

    while True:
        ret, frame = cam.read()
        if ret:
            ls.append(frame)
        else:
            break

    mid = len(ls) // 2
    cv2.imwrite(fn, ls[mid])
    print(fn)
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    for fp in glob.glob('F:/kerela/mov/ok3/*'):
        fn = fp.rsplit('\\', 1)[1]
        mov_to_jpg(fp, 'data/'+fn.split('.')[0] + '.jpg')
