import os
import cv2
import sys

def main():

    args = sys.argv[1:]


    if len(args) == 2 and  (args[0] == '-p' or args[0] == '--path'):

        rename_files_in_dir(args[1])

    else:

        print('\nUsage: II.py [option]\n\n  -p\t--path\t\tspecifies a path to dir, you need to change files in - required')


def rename_files_in_dir(path):


	files = os.listdir(path)


	for index, file in enumerate(files):

		# Load color image, convert to gray
		try:
			img = cv2.imread(path + file)
			
			gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

			resized_gray_image = cv2.resize(gray_img, (800, 800), interpolation = cv2.INTER_AREA)

			cv2.imwrite(path + file, resized_gray_image)
		except:
			print(file, '- not a pictire')



		try:
			ext = os.path.splitext(path + file)[1]
			os.rename(path + file, path + str(index) + ext)

		except:
			pass







# enter point check
if __name__=='__main__':


    main()