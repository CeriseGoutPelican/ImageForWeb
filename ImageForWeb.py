"""
" Permet de preparer vos images pour la publication web
"
" Auteur : Shining Paradox 
" Version : 0.1
"""

import glob
import os.path
import sys

try:
    import PIL
    from PIL import Image
except ImportError:
    sys.exit("""Vous devez installer PIL avec son module Image!
                $ pip install Image.""")

# RECUPERATION DES FICHIERS JPG DANS LE DOSSIER
files = glob.glob('*.jpg')

print "Bienvenue sur le logiciel de publication de Shining Paradox ! Ce logiciel permet de reduire la taille de vos fichiers et de mettre une watermark en bas a gauche de vos photos !"
print "Avant de commencer voici quelques instructions :"
print "1/ Lancez le logiciel dans le dossier contenant vos images"
print "2/ Si vous souhaitez ajouter une watermak, rajoutez un fichier 'watermak.png' avec vos autres images"
print "3/ Toutes vos images seront enregistrees dans un nouveau dossier 'web'"
print "4/ N'hesitez pas a me suivre sur Twitter @ShiningParadox et a partager mon travail !\n"
print "CONFIGURATION :"

# VARIABLES UTILISATEUR
maxSize   = raw_input("Taille maximum de la reduction, en pixels : ")
maxSize   = int(maxSize)
watermark = raw_input("Ajouter une watermark ? (y/n) : ")

if watermark == 'y':
    # VERIFIE SI UNE WATERMARK EST DANS LE DOSSIER
    if os.path.isfile("watermark.png"):
        watermarkImage = Image.open("watermark.png")
    else:
        sys.exit("""Le fichier 'watermark.png' n'existe pas dans le dossier !""")

# CREATION DU DOSSIER WEB
directory = r'web'
if not os.path.exists(directory):
    os.makedirs(directory)

# LISTE DES FICHIERS
print "\nTRAITEMENT EN COURS..."
for fileName in files:

    sys.stdout.write("  " + fileName + "...")
    sys.stdout.flush()
    img = Image.open(fileName)

    # WATERMARK
    if watermark == 'y':
        img.paste(watermarkImage, (10, 10), watermarkImage)

    # RESIZE
    # Largeur max
    wpercent = (maxSize / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    # Hauteur max
    if hsize > maxSize:
        hpercent = (maxSize / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, maxSize), PIL.Image.ANTIALIAS)
    else:
        img = img.resize((maxSize, hsize), PIL.Image.ANTIALIAS)
    img.save('web/'+fileName)
    print " termine !"
