import cv2
import numpy as np
import sys


kernel = np.ones((5, 5), np.uint8)


class ImageEdition:

    def img_to_gray_scale(self):
        """ Recibe un objeto imagen y devuleve la imagen en blanco y negro"""
        gray_img = cv2.cvtColor(self, cv2.COLOR_BGR2GRAY)
        return gray_img

    def img_to_erosion(self, iteration):
        try:
            erosion_img = cv2.erode(self, kernel, iterations=iteration)
            return erosion_img
        except:
            print("Erosion:", sys.exc_info()[0])
            return None

    def img_to_gradient(self):
        gradient = cv2.morphologyEx(self, cv2.MORPH_GRADIENT, kernel)
        return gradient

    def img_to_opening(self):
        opening = cv2.morphologyEx(self, cv2.MORPH_OPEN, kernel)
        return opening

    def img_to_blackhat(self):
        blackhat = cv2.morphologyEx(self, cv2.MORPH_BLACKHAT, kernel)
        return blackhat

    def img_to_tophat(self):
        tophat = cv2.morphologyEx(self, cv2.MORPH_TOPHAT, kernel)
        return tophat
