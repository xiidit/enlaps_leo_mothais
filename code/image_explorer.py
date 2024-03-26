# Il vous est demandé de faire une application python en ligne de commande
# > > qui est capable de lister les images (jpg, png) d’un dossier et en option
# > > d’afficher les informations exif de “DateTimeOriginal” et celles
# > relatives
# > > aux donnée GPS de ces images sur la sortie standard de la console.
# > >
# > > Prototype minimal:
# > >
# > > python image_explorer.py [—-showExif] INPUT_FOLDER
# > >
# > > Le candidat est libre d’ajouter des options.
# > >
# > > Exemples d’options:
# > >
# > >    -
# > >
# > >    lister le dossier de manière récursive
# > >    -
# > >
# > >    spécifier les champ exifs que l’on veut afficher
# > >    -clear
# > >
# > >    affichage d’une sortie standard en couleur
# > >
# > >
# > > Modalités d’évaluation:
# > >
# > >    -
# > >
# > >    Vous aurez 2h maximum à accorder à ce test (en auto-gestion).
# > >    -
# > >
# > >    La créativité ainsi que toute initiative seront valorisées lors de
# > >    l’entretien.



#le fichier se trouve dans le dossier code
#les images à tester se trouvent dans le dossier image_png

import os
# on prend en comptes les options -showExif
import sys
##on cherche les informations exif de l'image
#on utilise la librairie PIL



from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
def get_date_taken(path):
    exif = Image.open(path)._getexif()




def get_labeled_exif(exif):
    return {
        TAGS.get(key, key): value
        for key, value in exif.items()
    }



    


def list_images(folder,options):
    images = []
    for root,dirs,files in os.walk(folder):#os.walk permet de parcourir les dossiers et les fichiers
        print('nous sommes dans le dossier',root)   
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg'):
                path_image=os.path.join(root, file)
                images.append(path_image)
                if options=='--showExif':
                    print('Informations Exif de l\'image',file)
                    exif = Image.open(path_image)._getexif()
                    if exif:
                        labeled_exif = get_labeled_exif(exif)
                        for key, value in labeled_exif.items():
                            print(f'{key}: {value}')
                    else:
                        print('pas de données exif')
                    

                
    return images


def main():
    args=sys.argv
    images=list_images(args[2],args[1])
    print(images)
   
    
main()