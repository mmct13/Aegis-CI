import os

# Faille SAST (Semgrep devrait la voir)
# L'utilisation de eval() sur une entrée utilisateur est une faille critique (RCE)
user_input = input("Entrez une commande : ")
eval(user_input)

# Faille potentielle (Hardcoded path)
os.system("rm -rf /tmp/test")
