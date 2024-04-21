# Histograms
Simple Project to display a histogram for a grayscale image.

-----------------------------------------------------------

# Overview

In the context of image processing, a histogram represents the distribution of pixel intensities.

A histogram of an image is a 2D bar plot where the horizontal axis represents the pixel intensities, and the vertical axis denotes the frequency of each intensity.
For a grayscale image, this matrix will be made of numbers between 0 and 255.

The left side of the horizontal axis represents the dark areas, the middle represents mid-tone values, and the right-hand side represents light areas.
A histogram for a very dark image will have most of its data points on the left side and center of the graph while a histogram for a very bright image (with few dark areas or shadows) will have most of its data points on the right side and center of the graph.

-----------------------------------------------------------
# Sample Input

![image](https://github.com/ianmparker/Histograms/assets/18231849/44fc74d2-900e-4a73-a883-86c7e1051efb)

# Sample Output
![image](https://github.com/ianmparker/Histograms/assets/18231849/30a52041-02d9-4bdc-9b1b-b1a69f87f3fc)


# Refrerences: 
  - Auto Exposure FLIR: https://www.flir.com/support-center/iis/machine-vision/application-note/using-auto-exposure/
  - Histogram Equalization in Digital Image Processing: https://www.geeksforgeeks.org/histogram-equalization-in-digital-image-processing/
