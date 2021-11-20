import cv2
import sys
"""
programm searches on webcamera image for whatever u want & faces
"""


# main func to specify cascade path
def main():

    args = sys.argv[1:]



    if len(args) == 2 and  (args[0] == '-p' or args[0] == '--path'):

        determinator(args[1])

    else:

        print('\nUsage: II.py [option]\n\n-p\t--path\t\tspecifies a path to Haar cascade - required')



# func to determinate things on webcamera
def determinator(path: str):

    # new cam object
    cam = cv2.VideoCapture(0)

    # path to cascade

    # get my own xml-filed cascade
    my_cascade = cv2.CascadeClassifier(path)

    # this gets standart-over-32-thousands-lined cascade with human frontal faces data
    # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    b = True
    while b:
        # read image from camera
        ret, image = cam.read()
        if (ret):
            # 1) make image black-and-white 
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # search for faces
            # faces = face_cascade.detectMultiScale(image_gray, 1.1, 6)

            glasses = my_cascade.detectMultiScale(image_gray, 1.1, 1)

            # for face draw a blue rectangle
            # for x, y, width, height in faces:
            #     cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=4)

            for x, y, width, height in glasses:
                cv2.rectangle(image, (x, y), (x + width, y + height), color=(0, 255, 0), thickness=3)

            # show image to user
            cv2.imshow('image', image)

        # exit on escape button pressed  
        if cv2.waitKey(1) == 27:
            b = False


    # no needed camera releasing and closing windows because distructors are occurred 
    # cam.release()
    # cv2.destroyAllWindows()



# enter point check
if __name__=='__main__':
    main()