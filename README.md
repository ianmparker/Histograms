# Histogram Analysis: A Python Implementation for Grayscale Images

My LinkedIn: https://www.linkedin.com/in/ianmp

-----------------------------------------------------------

# Overview

This project is aimed at interpreting the pixel intensity distribution of grayscale images via histogram analysis.

In digital image processing, a histogram serves as a graphical representation of the tonal distribution in a digital image. It plots the number of pixels for each tonal value, with the horizontal axis denoting the pixel intensities and the vertical axis representing the corresponding frequency of each intensity.

For grayscale images, the pixel intensity values range from 0 to 255. The left side of the histogram corresponds to the darker areas (shadows), the middle section represents mid-tone values (grays), and the right-hand side depicts the lighter areas (highlights).

A histogram skewed towards the left indicates an abundance of darker tones, suggesting an underexposed image. Conversely, a histogram leaning towards the right signifies lighter tones, indicative of an overexposed image.

-----------------------------------------------------------
# Sample Input

![image](https://github.com/ianmparker/Histograms/assets/18231849/44fc74d2-900e-4a73-a883-86c7e1051efb)

# Sample Output
![image](https://github.com/ianmparker/Histograms/assets/18231849/30a52041-02d9-4bdc-9b1b-b1a69f87f3fc)

-----------------------------------------------------------

# Next Steps

As I continue to develop my real-time basketball event detection project (https://github.com/ianmparker/basket-event-detection) I will apply histogram analysis to improve image processing. 

A few ways this can be applied:
  - Image Segmentation
  - Contrast Enhancement
  - Feature Extraction 
  - Brightness/Gamma Adjustment ([https://github.com/ianmparker/Auto-Exposure/blob/main/README.md](https://github.com/ianmparker/Auto-Exposure/tree/main))

-----------------------------------------------------------

# Refrerences: 
  - Auto Exposure Calibration using Gamma Detection: https://github.com/ianmparker/Auto-Exposure/tree/main
  - Auto Exposure FLIR: https://www.flir.com/support-center/iis/machine-vision/application-note/using-auto-exposure/
  - Histogram Equalization in Digital Image Processing: https://www.geeksforgeeks.org/histogram-equalization-in-digital-image-processing/
  - basket-event-detection: https://github.com/ianmparker/basket-event-detection
