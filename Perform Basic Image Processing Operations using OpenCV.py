import cv2
import matplotlib.pyplot as plt
image=cv2.imread(r"C:\Users\GAMER\Downloads\puppy.png")
if image is None:
    print("Image is not found")
else:
    print("Image is found successfully")
    image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    resized=cv2.resize(image_rgb,(400,300))
    gray=cv2.cvtColor(resized,cv2.COLOR_RGB2GRAY)
    filtered=cv2.GaussianBlur(gray,(5,5),0)
    plt.figure(figsize=(10,7))
    
    plt.subplot(2,2,1)
    plt.imshow(image_rgb)
    plt.title("Orginal image")
    plt.axis("OFF")
    plt.subplot(2,2,2)
    plt.imshow(resized)
    plt.title("resized image")
    plt.axis("OFF")
    plt.subplot(2,2,3)
    plt.imshow(gray,cmap="gray")
    plt.title("gray filtered image")
    plt.axis("OFF")
    plt.subplot(2,2,4)
    plt.imshow(filtered,cmap="gray")
    plt.title("filtered image")
    plt.axis("OFF")
    plt.tight_layout
    
    plt.show
    