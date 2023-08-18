import numpy as np
import cv2

# Create a blank white image with dimensions 500x500
height, width = 500, 500
blank = np.ones((height, width, 3), dtype='uint8') * 255

# Define Swastika parameters
center = (width // 2, height // 2)
arm_length = 100
thickness = 5
color = (0, 0, 0)  # Black color

# Draw the Swastika
cv2.line(blank, (center[0] - arm_length, center[1]), (center[0] + arm_length, center[1]), color, thickness)
cv2.line(blank, (center[0], center[1] - arm_length), (center[0], center[1] + arm_length), color, thickness)
cv2.line(blank, (center[0] - arm_length // 2, center[1] - arm_length // 2), (center[0] + arm_length // 2, center[1] + arm_length // 2), color, thickness)
cv2.line(blank, (center[0] - arm_length // 2, center[1] + arm_length // 2), (center[0] + arm_length // 2, center[1] - arm_length // 2), color, thickness)

# Display the Swastika
cv2.imshow('Swastika', blank)
cv2.waitKey(0)
cv2.destroyAllWindows()
