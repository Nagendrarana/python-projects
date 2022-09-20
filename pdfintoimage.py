import glob, sys, fitz
def pdfintoimage():


    # To get better resolution
    zoom_x = 4.0  # horizontal zoom
    zoom_y = 4.0  # vertical zoom
    mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

    path = "C:/Users/NagendraRana/Desktop/"
    all_files = glob.glob(path + ".*pdf")
    single_file = glob.glob("Transcript2019")

    for filename in all_files:
        doc = fitz.open(filename)  # open document
        for page in doc:  # iterate through the pages
            pix = page.get_pixmap(matrix=mat)  # render page to an image
            print("page-%i.png" % page.number)
            pix.save("page-%i.png" % page.number)  # store image as a PNG




if __name__ == "__main__":
    pdfintoimage()
    

