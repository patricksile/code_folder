# -*- coding: cp1252 -*-
# Import des noms des fichiers dans prank
import os
# junior_path = "C:\Users\Nouboussi\Desktop\prank"
patrick_path = "/home/choupi/Downloads/prank/prank"
liste_des_photos = os.listdir("/home/choupi/Downloads/prank/prank")



renamed_files_list = []                   # => list  : je cr�e la liste o� je vais mettre les objets str deja renomm�s

compteur = 0   # => int   : j'initialise le compteur

while compteur < len(liste_des_photos): 
    

    number_image = liste_des_photos[compteur]  # => str   je prends l'objet str en position compteur+1 dans la premiere liste cr�ee
    
    
    no_number_image = number_image.translate(None, '0123456789') # =>str   je retire les chiffres dans l'objet str repr�sentant le nom...
    
    renamed_files_list.append(no_number_image)   # je mets cet objet str repr�sentant le nom d'un fichier renomm� dans la liste cr�ee plus haut

    # maintenant j'associe chaque objets str avec chiffres � son objet str renomm� dans le but de renommer definitivement les photos

    old_file = "/home/choupi/Downloads/prank/prank/" + number_image
    new_file = "/home/choupi/Downloads/prank/prank/" + no_number_image

    os.rename(old_file, new_file)

    compteur = compteur + 1
    
