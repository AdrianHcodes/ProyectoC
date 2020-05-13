from Class.ImageStorage import ImageStorage
from Class.ImageEdition import ImageEdition
import sys

if __name__ == '__main__':

    img1 = ImageStorage.read_image("Images/cat.jpg")
    img2 = ImageStorage.read_image("Images/spider.jpg")
    img3 = ImageStorage.read_image("Images/simpsons.jpg")
    img4 = ImageStorage.read_image("Images/la-casa-de-papel.jpg")
    img5 = ImageStorage.read_image("Images/cat2.jpg")
    img6 = ImageStorage.read_image("Images/toy-story.jpg")
    try:
        gray = ImageEdition.img_to_gray_scale(img1)
        erosion = ImageEdition.img_to_erosion(img2, 3)
        gradient = ImageEdition.img_to_gradient(img3)
        opening = ImageEdition.img_to_opening(img4)
        blackhat = ImageEdition.img_to_blackhat(img5)
        tophat = ImageEdition.img_to_tophat(img6)
        ImageStorage.save_img(img=gray, name_img="gray_cat")
        ImageStorage.save_img(img=erosion, name_img="erosion_spider")
        ImageStorage.save_img(img=gradient, name_img="gradient_simpsons")
        ImageStorage.save_img(img=opening, name_img="opening_papel")
        ImageStorage.save_img(img=blackhat, name_img="blackhat_cat2")
        ImageStorage.save_img(img=tophat, name_img="tophat_toystory")
        print("El proyecto corrio exitosamente")
    except:
        print("Error! de:", sys.exc_info()[0])
