```text
   _____                               _
  / ___/_________  ____  ____  _____  (_)___  _____
  \__ \/ ___/ _ \/ __ \/ __ \/ ___/ / / __ \/ ___/
 ___/ / /__/  __/ / / / /_/ / /    / / /_/ (__  )
/____/\___/\___/_/ /_/\__,_/_/    /_/\____/____/

```
> **By Marshall Christ**

# Scénarios d'Utilisation - Aegis-CI

Ce document décrit les cas d'usage principaux du projet **Aegis-CI** et comment il protège le cycle de développement.

## Scénario 1 : Le développeur distrait (Détection de Secrets)
**Contexte** : Un développeur tente de commiter un fichier contenant une clé API AWS en dur oubliée lors de tests locaux.

1.  **Action** : Le développeur exécute `git commit -m "Ajout config AWS"`.
2.  **Réaction (Pre-commit)** :
    *   Le hook `gitleaks` analyse le contenu du commit.
    *   Il détecte le pattern d'une clé AWS.
    *   🚫 **Le commit est bloqué** avec un message d'erreur explicite indiquant le fichier et la ligne incriminés.
3.  **Résultat** : La clé n'a jamais quitté le poste du développeur. Il la retire et re-commit.

## Scénario 2 : La propreté du code (Linting)
**Contexte** : Un fichier YAML de configuration est modifié, mais contient une indentation incorrecte qui ferait planter l'application au déploiement.

1.  **Action** : Le développeur commit le fichier YAML cassé.
2.  **Réaction (Pre-commit)** :
    *   Le hook `check-yaml` détecte l'erreur de syntaxe.
    *   🚫 **Le commit est bloqué**.
3.  **Résultat** : Le développeur corrige l'indentation immédiatement sans casser le build de tout le monde.

## Scénario 3 : Le filet de sécurité ultime (CI Pipeline)
**Contexte** : Un développeur pressé utilise `git commit --no-verify` pour forcer l'envoi d'un code contenant une vulnérabilité (ex: injection SQL potentielle) et une clé API cachée.

1.  **Action** : Le développeur pousse son code sur GitHub (`git push`).
2.  **Réaction (GitHub Actions)** :
    *   La pipeline `Security Pipeline` se déclenche.
    *   **Gitleaks (Job)** : Scan l'historique et trouve la clé API. ❌ **Le job échoue**.
    *   **Semgrep (Job)** : Analyse le code et détecte le pattern d'injection SQL. Une alerte est générée et envoyée dans l'onglet **GitHub Security**.
3.  **Résultat** : La Pull Request est marquée comme échouée (rouge). Le merge est bloqué jusqu'à correction.

## Scénario 4 : Sécurisation de l'Infrastructure (IaC)
**Contexte** : L'équipe ajoute un fichier `Dockerfile` pour conteneuriser l'application, mais l'image de base choisie est obsolète ou le user est `root`.

1.  **Action** : Le développeur pousse le `Dockerfile`.
2.  **Réaction (Checkov - CI)** :
    *   Le job `checkov` scanne le Dockerfile.
    *   Il détecte que le container tourne en tant que root (Security Risk).
    *   Il rapporte l'erreur dans les logs de la CI (et bientôt en SARIF si configuré).
3.  **Résultat** : L'équipe est informée qu'elle doit ajouter une instruction `USER` dans le Dockerfile pour respecter les bonnes pratiques.

## Scénario 5 : Veille de vulnérabilité (SCA)
**Contexte** : Le projet utilise une librairie `npm` ou `pip` qui vient d'avoir une faille critique découverte (CVE).

1.  **Action** : Une pipeline planifiée (ou sur PR) se lance.
2.  **Réaction (Trivy - CI)** :
    *   Le job `trivy` scanne les fichiers de dépendances (`package-lock.json`, `requirements.txt`).
    *   Il identifie la CVE critique.
    *   Une alerte de sécurité est remontée dans GitHub.
3.  **Résultat** : L'équipe reçoit une notification pour mettre à jour la dépendance avant qu'elle ne soit exploitée.
