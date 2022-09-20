import zxing


def barcodereader(img):
    
    reader = zxing.BarCodeReader()
    barcode = reader.decode(img)
    print(barcode)


if __name__ == "__main__":


    for i in range(2,5):
        
        
        #print("reading from image no. " +str(i))
       # image = PIL.open("image6.jpg")
        image="Transcript2019_page-000"+str(i)+".jpg"
    # image="SIGNEDINITIALDISCL_page-000"+str(i)+".jpg"
        #image="SIGNEDINITIALDISCL_page-00"+str(i)+".jpg"
       # image = "image"+str(i)+".jpg"
        #pil_image = PIL.open(image)
        
    # image = "image6.jpg"                
        barcodereader(image)
                
	#image="image4.jpg"
	#BarcodeReader(image)
