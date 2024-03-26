


#le fichier se trouve dans le dossier code
#les images à tester se trouvent dans le dossier image_png

import os

def list_images(folder):
    images = []
    for root,dirs,files in os.walk(folder):#os.walk permet de parcourir les dossiers et les fichiers   
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg'):
                images.append(os.path.join(root, file))
                
    return images


def main():
    
    images=list_images('image_png')
    print(images)
    
main()