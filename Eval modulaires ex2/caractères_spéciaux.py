def contient_caractere_special(mot_de_passe):
    
    mot_de_passe = input("Verification de mot de passe (au moins 8 et 16 caractères) : ")

    if mot_de_passe != ("@#$%&"):
        return False
    else:
        return True
contient_caractere_special(mot_de_passe = "")
