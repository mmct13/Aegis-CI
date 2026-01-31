# BSIC Payment Gateway (Exemple Aegis)

Ce dossier contient un microservice de paiement exemple pour démontrer la protection d'Aegis-CI.

## Comment tester la protection ?

1.  Ouvrez `main.py`.
2.  Décommentez la ligne contenant `test_pan = "453201511283036"`.
3.  Tentez de commiter :
    ```bash
    git add main.py
    git commit -m "Test DLP"
    ```
4.  🚫 **Aegis-CI bloquera le commit** car il détecte un numéro de carte valide (Luhn check) dans le code source.

## Structure
*   `main.py`: L'API Flask.
*   `requirements.txt`: Dépendances de l'exemple.
