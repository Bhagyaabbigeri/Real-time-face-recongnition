import cv2
import numpy as np

# Create a simple image
image = np.zeros((500, 500, 3), dtype="uint8")
image[:] = (0, 255, 0)  # Green background

# Display the image
cv2.imshow("Test Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
