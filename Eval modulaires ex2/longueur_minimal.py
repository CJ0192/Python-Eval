def est_longueur_valide(mot_de_passe):

    mot_de_passe = input("Verification de mot de passe (au moins 8 et 16 caractères) : ")

    longueur = len(mot_de_passe)

    if 8 <= longueur <= 16:
        return True
    else:
        return False

est_longueur_valide(mot_de_passe="")