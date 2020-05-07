from PIL import Image
import math

def start(cell_size, source, dest, ds_value, saving, show):    
    # load image and 
    orig = Image.open(source)
    # increase contrast for better differntiation between colors
    orig = change_contrast(orig, 100)

    # convert to ("L")=greyscale for simpler output
    orig = orig.convert("L")
    # resize image to reduce pixel number
    width, height = orig.size
    # convert image in bitmap with pixel pattern
    new_size = (round(width * ds_value), round(height * ds_value))
    orig = orig.resize(new_size)
    ret_img = btmp(cell_size, orig)

    if (saving):
        ret_img.save(dest)

    # show image
    if show: ret_img.show()

def change_contrast (image, level):
    """
    enhances contrast, for better color distinction
    """
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return image.point(contrast)

def color_distribution(img):
    """
    
    """
    pixels = img.load()
    color = [0] * 256
    total = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            index = pixels[i,j]
            color[index] += 1
            total += 1

    part_size = total / 7 
    part_bounds = 7*[0]

    index = 0
    u_bound = 0
    for i in range (7):
        
        while (u_bound < part_size and index < len(color)):
            u_bound += color[index]
            index += 1

        
        if (index >= len(color)):
            part_bounds[i] = 256
        else:
            u_dif = u_bound % part_size
            d_dif = (u_bound + color[index + 1]) % part_size

            if (u_dif <= d_dif): part_bounds[i] = index
            else: part_bounds[i] = index+1

        u_bound = 0
    return part_bounds

def color_map(color, cs, color_code):   # cs = cell_size
    """
    maps a color to a corresponding pixel pattern depending on the cell_size
    """

    if (len(color_code)==0):
        color_code = [61,98,121,139,155,178,256]

    # short lambda function for dividing a cell into the black and white parts
    # namely the x-index of the first element of every color block
    div = lambda x, cs: (round((cs-x)/2),x + round((cs-x)/2), cs)

    if (color < color_code[0]):
        return div(3,cs)
    elif (color < color_code[1]):
        return div(5,cs)
    elif (color < color_code[2]):
        return div(7,cs)
    elif (color < color_code[3]):
        return div(9,cs)
    elif (color < color_code[4]):
        return div(11,cs)
    elif (color < color_code[5]):
        return div(13,cs)
    else:
        return div(15,cs)

def btmp(cell_size, image):
    """
    creates new image, by applaying a pixel 
    pattern over each and every pixel of the original image
    """
    # loads pixelarray from original image
    pixels_orig = image.load()

    color_code = color_distribution(image)
    #color_code = []
    #print(color_code)

    # assign dimensions of image to bitmap
    width, height = image.size
    dim0 = width
    dim1 = height

    # create new bitmap: L = Grayscale (single number values from 0-255), size = dimensions 
    new_img = Image.new(mode = "L", size = (dim0*cell_size, dim1*cell_size))
    # create pixel array corresponding to bitmap
    pixels = new_img.load()

    # loop through every pixel in orig image
    for i in range(dim0):
        for j in range(dim1):
            # loop cell_size - times in y direction
            for j1 in range(cell_size):
                # map color to color distribution
                col = color_map(pixels_orig[i,j], cell_size, color_code)
                # create pixel pattern in black-white-black, width of cell_size
                for i1 in range(col[0]):
                    pixels[i * cell_size + i1, j * cell_size + j1] = 0
                for i1 in range(col[0], col[1]):
                    pixels[i * cell_size + i1, j * cell_size + j1] = 255
                for i1 in range(col[1], col[2]):
                    pixels[i * cell_size + i1, j * cell_size + j1] = 0
    return new_img
