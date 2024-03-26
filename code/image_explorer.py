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

##terminal en couleur
#on utilise la librairie termcolor
from termcolor import colored
def print_colored(text,color):
    print(colored(text,color))
    


def get_date_taken(path):
    exif = Image.open(path)._getexif()




def get_labeled_exif(exif):
    return {
        TAGS.get(key, key): value
        for key, value in exif.items()
    }



def get_info(path):
    exif = Image.open(path)._getexif()
    if exif:
        labeled_exif = get_labeled_exif(exif)
        for key, value in labeled_exif.items():
            print_colored(f'{key}: {value}', 'green')   
    else:
        print_colored('Pas d\'informations Exif', 'red')


def list_images(folder,optExif=None,optionRecursif=None):
    images = []
    for root,dirs,files in os.walk(folder):#os.walk permet de parcourir les dossiers et les fichiers
          
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg'):
                path_image=os.path.join(root, file)
                images.append(path_image)
                if optExif=='--showExif':
                    print_colored(path_image,'blue')
                    get_info(path_image)
                    
        if optionRecursif!='--recursive':
            break
            
                
    return images






def main():
    args=sys.argv
    images=[]
    if len(args)==3:
        images=list_images(args[2],args[1],args[1])
    if len(args)==2:
        images=list_images(args[1])
    if len(args)==1:
        print("Veuillez au moins entrer un dossier (vos options dans l'ordre: --showExif, --recursive)")
    if len (args)==4:
        images=list_images(args[3],args[1],args[2])
    print(images)
  
   
    
main()