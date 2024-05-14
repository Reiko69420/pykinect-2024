import ctypes
import pygame
import cv2
import numpy as np
from pykinect import com
from pykinect import runtime

def get_depth_data(kinect):
    depth_frame = kinect.get_last_depth_frame()
    depth_frame_data = depth_frame.reshape((kinect.depth_frame_desc.Height, kinect.depth_frame_desc.Width)).astype(np.uint8)
    return depth_frame_data

def display_with_opencv(depth_data):
    cv2.imshow('Depth Image', depth_data)
    cv2.waitKey(1)

def main():
    pygame.init()
    pygame.display.set_caption("Kinect Depth Display")

    # Initialize Kinect
    kinect = runtime.PyKinectRuntime(com.FrameSourceTypes_Depth)

    # Set up Pygame display
    #screen = pygame.display.set_mode((kinect.depth_frame_desc.Width, kinect.depth_frame_desc.Height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE, 32)

    # Main loop
    while True:
        if kinect.has_new_depth_frame():
            # Get depth data
            depth_data = get_depth_data(kinect)

            # Display using Pygame
            #display_with_pygame(depth_data, screen)

            # Display using OpenCV
            display_with_opencv(depth_data)

        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kinect.close()
                pygame.quit()
                return

if __name__ == "__main__":
    main()