#Importing library
import glob, sys, fitz
from turtle import bgcolor
import cv2
from pyzbar.pyzbar import decode
from PIL import Image as PIL
from pdf417_decoder import BarcodeReader
from pdfintoimage import pdfintoimage
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Make one method to decode the barcode
def barcodeReader(image):
	count=0
	# read the image in numpy array using cv2
	img = cv2.imread(image)
	
	# Decode the barcode image
	detectedBarcodes = decode(img)
	
	# If not detected then print the message
	if not detectedBarcodes:
		print(bcolors.WARNING  +"pyzbar cannot scan " )
		print(bcolors.WARNING + "trying with another library",end='\n')
		
		pil_image = PIL.open(image)
		BarcodeReader(pil_image)
	else:
	
		# Traverse through all the detected barcodes in image
		for barcode in detectedBarcodes:

		
			# Locate the barcode position in image
			#(x, y, w, h) = barcode.rect
			
			# Put the rectangle in image using
			# cv2 to heighlight the barcode
			#cv2.rectangle(img, (x-10, y-10),
			#			(x + w+10, y + h+10),
			#			(255, 0, 0), 2)
			
			if barcode.data!="":
			
			# Print the barcode data
                                
				print(bcolors.OKGREEN + "-------------------" +str(barcode.data) +"-----------------------")
				print(bcolors.OKBLUE + "-------------------" +str(barcode.type) +"-----------------------")
				count=count+1
			
                            
		print(bcolors.BOLD +  "detected barcodes = " + str(count))
				
	#Display the image
	#cv2.imshow("Image", img)        
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

if __name__ == "__main__":

	path = "C:/Users/NagendraRana/Desktop/"
	file_name = "barcodes.pdf"
	full_path = path + file_name
	last_index = pdfintoimage(full_path)
	
	print(last_index)

	
	for i in range(0,last_index+1):
		image = "page-"+str(i)+".png"
		print(image)
		barcodeReader(image)
    
# Take the image from user

    # for i in range(2,6):
        
            
    #            # image="Transcript2019_page-000"+str(i)+".jpg"
    #            # image="SIGNEDINITIALDISCL_page-000"+str(i)+".jpg"
    #            # image="SIGNEDINITIALDISCL_page-00"+str(i)+".jpg"
    #     image = "image"+str(i)+".jpg"
    #     print(image)
    #     #image = "image5.jpg"
                        
    #     barcodeReader(image)
    # for i in range(10,97):
        
         
        
            
    #            # image="Transcript2019_page-000"+str(i)+".jpg"
    #            # image="SIGNEDINITIALDISCL_page-000"+str(i)+".jpg"
        
    #     image="SIGNEDINITIALDISCL_page-00"+str(i)+".jpg"
    #            # image = "image"+str(i)+".jpg"
    #     print(image)
        
                        
    #     barcodeReader(image)
    # for i in range(2,4):
    #     image="Transcript2019_page-000"+str(i)+".jpg"
    #     print(image)
    #     barcodeReader(image)

                
	
