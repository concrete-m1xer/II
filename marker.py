import cv2
import sys
import os
import numpy as np









def main():

    args = sys.argv[1:]


    if len(args) == 6 and  (args[0] == '-p' or args[0] == '--path') and (args[2] == '-o' or args[2] == '--out') and (args[4] == '-d' or args[4] == '--dir'):

        mark_pics_in_dir(args[1], args[3], args[5])

    else:

        print('\nUsage: II.py [option]\n\n  -p\t--path\t\tspecifies a path to dir, you need to cropp pics in - required')
        print('  -o\t--out\t\tspecifies a path to output file - required')
        print('  -d\t--dir\t\tspecifies a directory to save cropped photos - required')


    return









def rec_selection(event, x, y, flags, param):

    global init_x, init_y, fin_x, fin_y, img, clone, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        img = clone.copy()
        cv2.imshow("image", img)
        drawing = True
        init_x, init_y = x, y

    if drawing:
        img = clone.copy()
        cv2.rectangle(img, [init_x, init_y], [x, y], (0, 0, 0), 1)
        cv2.imshow("image", img)
    
    if event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, [init_x, init_y], [x, y], (0, 255, 0), 2)
        cv2.imshow("image", img)
        fin_x, fin_y = x, y

    return








def mark_pics_in_dir(in_path, out_path, out_dir):

    global img, clone, counter, init_x, init_y, fin_x, fin_y

    files = os.listdir(in_path)
    out_file = open(out_path, 'w')

    for index, file in enumerate(files):
        try:
            img = cv2.imread(in_path + file)
            clone = img.copy()
            b = True
            while b:
                cv2.imshow("image", img)   
                key = cv2.waitKey(1)
                if key == 27:
                    return

                # n stands for next
                elif key == ord('n'):
                    b = False

                # s stands for save
                elif key == ord('s'):
                    img = img[init_y : fin_y, init_x : fin_x]
                    cv2.imwrite(out_dir + str(counter) + ".jpg", img)
                    # check filename
                    output: str
                    outline = out_dir.split('/')
                    if outline[-1] == "":
                        output = outline[-2]
                    else:
                        output = outline[-1]
                    # write into .dat
                    line = output + '/' + str(counter) + '.jpg' + '  1  ' + '0 ' + '0 ' + str(fin_x - init_x) + ' ' + str(fin_y - init_y) + '\n'
                    out_file.write(line)
                    out_file.flush()
                    img = clone.copy()
                    counter += 1

                # r for reset
                elif key == ord('r'):
                    img = clone.copy()
        except:
            print(file, '- not a pictire')


    out_file.close()






init_x, init_y = 0, 0

fin_x, fin_y = 0, 0

# pseudoimage to start with
img = np.zeros((512,512,3), np.uint8)
clone = None

cv2.namedWindow('image')

cv2.setMouseCallback('image', rec_selection)

counter = 0

drawing = False








# enter point 
if __name__=='__main__':
    main()