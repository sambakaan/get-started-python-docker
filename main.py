from os.path import exists

print("BIENVENUE SAMA APP")

etudiant = {
    'nom': '',
    'prenom' :'',
    'classe': '',
    'etat': 'non payé',
    'notes' : []
}

print("===================")

if(exists('enregistrement.txt')):
    old_file = open('enregistrement.txt','r')
    print("Dernier Enregistrement")
    print(old_file.read())
    old_file.close()
else:
    print("Aucune information n'a été enregistré au par avant ")

print("===================")

print("Enregistrement Informations etudiants")
etudiant['nom'] = input("Entrez votre nom : ")
etudiant['prenom'] = input("Entrez votre prénom : ")
etudiant['classe'] = input("Entrez votre classe : ")
etudiant['etat'] = input("Entrez votre etat payement  : ")

etudiant['notes'].append(int(input("Entrez la première note : ")))
etudiant['notes'].append(int(input("Entrez la deuxième note : ")))
etudiant['notes'].append(int(input("Entrez la troisième note : ")))
etudiant['notes'].append(int(input("Entrez la quartirème note : ")))
etudiant['notes'].append(int(input("Entrez la cinquième note : ")))

moyenne = sum(etudiant['notes']) / len(etudiant['notes'])

information = f"L'apprenant {etudiant['prenom']} {etudiant['nom']} s'est inscrit en classe {etudiant['classe']} avec une moyenne de {moyenne}"


file = open('enregistrement.txt','w')
file.write(information)
file.close()

old_file = open('enregistrement.txt','r')
print("Vous venez de saisir")
print(old_file.read())
old_file.close()































# moyenne = (etudiant['notes'][0] + etudiant['notes'][1] + etudiant['notes'][2]) / 3
# etudiant['nom'] = input("Entrez votre nom : ")
# etudiant['prenom'] = input("Entrez votre prénom : ")
# etudiant['classe'] = input("Entrez votre classe : ")
# etudiant['etat'] = input("Entrez votre etat payement  : ")
# etudiant['notes'].append(int(input("Entrez votre  premiere note  : ")))
# etudiant['notes'].append(int(input("Entrez votre  deuxième note  : ")))
# etudiant['notes'].append(int(input("Entrez votre  troisieme note  : ")))
# etudiant['notes'].append(int(input("Entrez votre  quatrieme note  : ")))

# print("Inscription Apprenant")

# moyenne = sum(etudiant['notes']) / len(etudiant['notes'])

# print(f"L'apprenant {etudiant['nom']} {etudiant['prenom']} s'est inscrit en classe de  {etudiant['classe']} avec une moyenne de {moyenne}")
