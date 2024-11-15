def est_segment_valide(segment):
    if not segment.isdigit():  
        return False
    
    num = int(segment)
    return 0 <= num <= 255

"""etat = est_segment_valide("")
print(etat)"""

def est_ip_valide(ip):
    if "." in ip:
        point = "."
    else:
        return False   
     
    myListe = ip.split(point)

    if len(myListe) != 4:
        return False
    
    for segment in myListe:
        if not est_segment_valide(segment):
            return False
    return True

"""etat = est_ip_valide("192.168.5.0")
print(etat)"""

def saisir_ip():
    while True: 
        ip = input("Entre une adresse IP: ")
        if est_ip_valide(ip):
            print("Adresse IP valide")
            break
            
        else:
            print("Adresse IP invalide")
    
saisir_ip()