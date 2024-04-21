import cv2
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('image.png',0)

# Calculate histogram using cv2.calcHist()
hist = cv2.calcHist([img],[0],None,[256],[0,256])

# plot the original image in grayscale
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

# Plot the histogram
plt.subplot(1, 2, 2)
plt.plot(hist)
plt.title('Histogram')
plt.xlabel('Pixel Values')
plt.ylabel('Frequency')
plt.show()
