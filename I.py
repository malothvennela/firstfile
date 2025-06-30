import cv2
import pytesseract
import numpy as np

# Configure path to tesseract executable
# Example for Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load image
image_path = 'car.jpg'  # Replace with your image path
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply bilateral filter to reduce noise and keep edges sharp
filtered = cv2.bilateralFilter(gray, 11, 17, 17)

# Detect edges
edged = cv2.Canny(filtered, 30, 200)

# Find contours
contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

# Initialize license plate contour
plate_contour = None

for contour in contours:
    # Approximate the contour
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.018 * peri, True)

    # License plate is usually a rectangle (4 corners)
    if len(approx) == 4:
        plate_contour = approx
        break

if plate_contour is not None:
    # Create mask and extract plate region
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [plate_contour], 0, 255, -1)
    new_image = cv2.bitwise_and(image, image, mask=mask)

    # Crop the bounding rect
    (x, y) = np.where(mask == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    cropped = gray[topx:bottomx+1, topy:bottomy+1]

    # OCR
    text = pytesseract.image_to_string(cropped, config='--psm 8')
    print("Detected License Plate Number:", text.strip())

    # Optional: Show result
    cv2.imshow("Plate", cropped)
    cv2.imshow("Original", image)
    cv2.waitKey(0)
else:
    print("No license plate detected.")

cv2.destroyAllWindows()
