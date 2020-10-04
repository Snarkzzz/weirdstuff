import os
import cv2
import pytesseract
output_dir = './'
def get_string(img_path):
    # Read image using opencv
    img = cv2.imread(img_path)
    # Extract the file name without the file extension
    file_name = os.path.basename(img_path).split('.')[0]
    file_name = file_name.split()[0]
    # Create a directory for outputs
    output_path = os.path.join(output_dir, file_name)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    print(output_path)
    # Rescale the image, if needed.
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    """
    print("4")
    # Apply threshold to get image with only b&w (binarization)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    """
    method = 'mymthd'
    # Save the filtered image in the output directory
    save_path = os.path.join(output_path, file_name + "_filter_" + str(method) + ".jpg")
    cv2.imwrite(save_path, img)
    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(img, lang="eng")
    return result
s = get_string('165795.tif')
print(s)
