#!/usr/bin/env python3
import sys
import subprocess
import json
import os

def check_requirements_file():
    if not os.path.exists('requirements.txt'):
        print("ℹ️  Pas de requirements.txt trouvé. Audit ignoré.")
        return True
    return False

def run_safety_check():
    """Exécute safety check et analyse le résultat."""
    print("🛡️  Aegis Compliance: Audit des dépendances (Safety)...")
    
    try:
        # On utilise --json pour parser facilement, mais safety payant a changé ça récemment.
        # La version gratuite (old) supporte --json.
        # Si safety n'est pas installé, ça va lever une exception.
        result = subprocess.run(
            [sys.executable, '-m', 'safety', 'check', '-r', 'requirements.txt', '--json'], 
            capture_output=True, 
            text=True
        )
    except FileNotFoundError:
        print("⚠️  ERREUR: L'outil 'safety' n'est pas installé.")
        print("   Installez-le avec: pip install safety")
        sys.exit(1)

    if result.returncode != 0:
        # Safety retourne un code != 0 si vulns trouvées ou erreur
        try:
            vulnerabilities = json.loads(result.stdout)
        except json.JSONDecodeError:
            # Si pas de JSON (peut-être version différente ou erreur texte), on affiche la sortie brute
            print("⚠️  Erreur parsing JSON ou sortie texte Safety:")
            print(result.stdout)
            print(result.stderr)
            sys.exit(1)

        if vulnerabilities:
            print(f"❌ CRITICAL: {len(vulnerabilities)} vulnérabilités trouvées !")
            for vuln in vulnerabilities:
                # Structure typique de safety json (peut varier selon version)
                # [["django", "<1.11.10", "4.0", "Description...", "ID"]]
                # ou dict list. Adaptabilité requise.
                package = vuln[0] if isinstance(vuln, list) else vuln.get('package_name', 'Unknown')
                version = vuln[2] if isinstance(vuln, list) else vuln.get('installed_version', 'Unknown')
                desc = vuln[3] if isinstance(vuln, list) else vuln.get('advisory', 'See details')
                
                print(f"   - {package} ({version}): {desc[:100]}...")
            
            print("\n⛔ DEPLOYMENT REFUSED: Mettez à jour vos dépendances.")
            sys.exit(1)
            
    print("✅ Aegis Compliance: Aucune vulnérabilité connue détectée.")
    sys.exit(0)

def main():
    if check_requirements_file():
        sys.exit(0)
    run_safety_check()

if __name__ == '__main__':
    main()
