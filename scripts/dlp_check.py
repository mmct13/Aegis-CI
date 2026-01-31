#!/usr/bin/env python3
import sys
import re
import argparse

def luhn_check(card_number):
    """Vérifie si une suite de chiffres est une carte bancaire valide (Algo de Luhn)"""
    digits = [int(d) for d in str(card_number)]
    checksum = 0
    double = False
    for digit in reversed(digits):
        if double:
            digit *= 2
            if digit > 9: digit -= 9
        checksum += digit
        double = not double
    return (checksum % 10) == 0

def scan_file(filepath):
    """Scanne un fichier à la recherche de numéros de carte bancaire potentiels."""
    potential_pans = []
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Regex simple pour trouver des séquences de 13 à 19 chiffres
            # On cherche des suites de chiffres qui pourraient être des PANs
            # Cela supporte les espaces ou tirets éventuels s'ils sont nettoyés avant check, 
            # mais pour ce POC on cherche des suites contiguës ou séparées courantes.
            
            # Cette regex cherche des groupes de 13 à 19 chiffres consécutifs
            matches = re.finditer(r'\b(?:\d[ -]*?){13,19}\b', content)
            
            for match in matches:
                candidate = match.group(0).replace(' ', '').replace('-', '')
                if candidate.isdigit() and luhn_check(candidate):
                    potential_pans.append(match.group(0))
                    
    except Exception as e:
        print(f"⚠️ Erreur lors de la lecture de {filepath}: {e}")
        return []

    return potential_pans

def main():
    parser = argparse.ArgumentParser(description='Aegis DLP Scanner: Détecte les numéros de carte bancaire.')
    parser.add_argument('filenames', nargs='*', help='Fichiers à scanner')
    args = parser.parse_args()

    found_violation = False

    print("🛡️  Aegis DLP: Analyse en cours...")

    for filename in args.filenames:
        # On peut filtrer les extensions ici si pre-commit ne le fait pas déjà, 
        # mais pre-commit passe généralement les fichiers matchant le pattern hook.
        pans = scan_file(filename)
        if pans:
            print(f"❌ CRITICAL: Numéros de carte bancaire potentiels trouvés dans {filename}:")
            for pan in pans:
                print(f"   - {pan} (Validé par Luhn)")
            found_violation = True
    
    if found_violation:
        print("\n⛔ COMMIT BLOQUÉ : Veuillez supprimer les données sensibles avant de commiter.")
        sys.exit(1)
    else:
        print("✅ Aegis DLP: Aucun numéro de carte détecté.")
        sys.exit(0)

if __name__ == '__main__':
    main()
