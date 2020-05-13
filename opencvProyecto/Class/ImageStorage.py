import cv2


class ImageStorage:

    @staticmethod
    def read_image(path_img):
        """Leer una imagen desde el disco y devolver in objeto imagen"""
        if isinstance(path_img, str):
            img = cv2.imread(path_img)
            return img
        else:
            print("Formato no valido")
            return None

    @staticmethod
    def save_img(img, name_img):
        # write image on disk
        if isinstance(name_img, str):
                name_img = name_img + ".jpg"
                cv2.imwrite(name_img, img)
        else:
            print("Formato no valido")


