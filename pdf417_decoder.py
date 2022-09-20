from PIL import Image as PIL
from pdf417decoder import PDF417Decoder

def BarcodeReader(image):
    
    

    
    decoder = PDF417Decoder(image)



    if (decoder.decode() > 0):
        
        decoded = decoder.barcode_data_index_to_string(0)
        
        print("===================================" +str(decoded)+"======================================")
    else:
        print(" >>>>>>>>>>>>>>>>>>>>>>>>>>Cannot be scanned with pdf417decoder <<<<<<<<<<<<<<<<<<<<<<<<<<<")


if __name__ == "__main__":

    

    for i in range(2,9):
        
        print("reading from image no. " +str(i))
       # image = PIL.open("image6.jpg")
       # image="Transcript2019_page-000"+str(i)+".jpg"
        image="page-"+str(i)+".png"
      #  image="SIGNEDINITIALDISCL_page-00"+str(i)+".jpg"
      #  image = "image"+str(i)+".jpg"
        pil_image = PIL.open(image)
        
    # image = "image6.jpg"                
        BarcodeReader(pil_image)
                
	#image="image4.jpg"
	#BarcodeReader(image)
    



