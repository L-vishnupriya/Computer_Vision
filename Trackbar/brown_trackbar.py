import cv2
import numpy as np

def enhance_brown_in_forest(image_path):
    # Load the image
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range for brown color (Adjust if necessary)
    lower_brown = np.array([10, 30, 30])
    upper_brown = np.array([25, 255, 200])

    # Create a mask for the brown color
    brown_mask = cv2.inRange(hsv_image, lower_brown, upper_brown)

    # Extract the brown areas from the original image
    brown_area = cv2.bitwise_and(hsv_image, hsv_image, mask=brown_mask)

    def update_image(x):
        # Get current positions of trackbars
        saturation_value = cv2.getTrackbarPos('Saturation', 'Enhanced Brown Image')
        brightness_value = cv2.getTrackbarPos('Brightness', 'Enhanced Brown Image')

        # Increase saturation and brightness of the brown areas
        hue, saturation, value = cv2.split(brown_area)
        saturation = cv2.add(saturation, saturation_value)  # Increase saturation
        value = cv2.add(value, brightness_value)  # Increase brightness

        # Merge the channels back
        enhanced_brown = cv2.merge([hue, saturation, value])

        # Convert back to BGR color space
        enhanced_image = cv2.cvtColor(enhanced_brown, cv2.COLOR_HSV2BGR)

        # Blend the enhanced brown with the original image
        final_image = cv2.addWeighted(image, 0.5, enhanced_image, 0.5, 0)

        # Display the final image
        cv2.imshow('Enhanced Brown Image', final_image)

    # Create a window to display the image
    cv2.namedWindow('Enhanced Brown Image')

    # Create trackbars for adjusting saturation and brightness
    cv2.createTrackbar('Saturation', 'Enhanced Brown Image', 0, 255, update_image)
    cv2.createTrackbar('Brightness', 'Enhanced Brown Image', 0, 255, update_image)

    # Call the update_image function once to display the initial image
    update_image(0)

    # Wait until the user presses a key to exit
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the paths for your images
image_path1 = r'C:\vishnu\image\image_gr1.jpg'

# Enhance and show the brown color in both images
enhance_brown_in_forest(image_path1)

