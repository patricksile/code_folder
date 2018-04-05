# -*- coding: cp1252 -*-
# Import des noms des fichiers dans prank
import os
# junior_path = "C:\Users\Nouboussi\Desktop\prank"
patrick_path = "/home/choupi/Downloads/prank/prank"
liste_des_photos = os.listdir("/home/choupi/Downloads/prank/prank")



renamed_files_list = []                   # => list  : je crée la liste où je vais mettre les objets str deja renommés

compteur = 0   # => int   : j'initialise le compteur

while compteur < len(liste_des_photos): 
    

    number_image = liste_des_photos[compteur]  # => str   je prends l'objet str en position compteur+1 dans la premiere liste créee
    
    
    no_number_image = number_image.translate(None, '0123456789') # =>str   je retire les chiffres dans l'objet str représentant le nom...
    
    renamed_files_list.append(no_number_image)   # je mets cet objet str représentant le nom d'un fichier renommé dans la liste créee plus haut

    # maintenant j'associe chaque objets str avec chiffres à son objet str renommé dans le but de renommer definitivement les photos

    old_file = "/home/choupi/Downloads/prank/prank/" + number_image
    new_file = "/home/choupi/Downloads/prank/prank/" + no_number_image

    os.rename(old_file, new_file)

    compteur = compteur + 1
    
