```text
    ____       __                       __  _
   /  _/____  / /____  ____ __________ / /_(_)___  ____
   / // __ \/ __/ _ \/ __ `/ ___/ __ `/ __/ / __ \/ __ \
 _/ // / / / /_/  __/ /_/ / /  / /_/ / /_/ / /_/ / / / /
/___/_/ /_/\__/\___/\__, /_/   \__,_/\__/_/\____/_/ /_/
                   /____/
```
> **By Marshall Christ**

# Guide d'Intégration d'Aegis-CI

Ce guide explique comment utiliser **Aegis-CI** pour sécuriser vos autres projets, qu'ils soient nouveaux ou déjà existants.

## Option 1 : Pour un Nouveau Projet (GitHub Template)
La méthode la plus simple est d'utiliser ce repository comme "Modèle".

1.  Allez sur la page GitHub d'Aegis-CI.
2.  Cliquez sur le bouton vert **"Use this template"** > **"Create a new repository"**.
3.  Nommez votre nouveau projet.
4.  Une fois créé, clonez-le :
    ```bash
    git clone https://github.com/votre-user/mon-nouveau-projet.git
    cd mon-nouveau-projet
    ```
5.  Activez les protections locales :
    ```bash
    pip install pre-commit
    pre-commit install
    ```
    *Et voilà ! Votre nouveau projet est sécurisé par défaut.*

---

## Option 2 : Pour un Projet Existant ("Greffe")
Si vous avez déjà un projet (ex: une API Node.js ou un script Python) et que vous voulez lui ajouter la sécurité d'Aegis-CI.

### Étape 1 : Copier les fichiers de configuration
Copiez les fichiers suivants depuis Aegis-CI vers la racine de votre projet cible :

*   [`.pre-commit-config.yaml`](file:///c:/Users/MARSHALL/Documents/Projets/Aegis-CI/.pre-commit-config.yaml)
*   [`.github/workflows/security.yml`](file:///c:/Users/MARSHALL/Documents/Projets/Aegis-CI/.github/workflows/security.yml) (Créez les dossiers `.github/workflows` si nécessaire)

### Étape 2 : Installer Pre-commit
Dans votre projet cible, ouvrez un terminal :

```bash
# 1. Installer l'outil (si vous ne l'avez pas déjà)
pip install pre-commit

# 2. Installer les scripts dans le dossier .git/hooks
pre-commit install
```

### Étape 3 : Premier Scan (Baseline)
Lancez une vérification immédiate pour voir l'état actuel de votre projet :

```bash
pre-commit run --all-files
```
*Attendez-vous à quelques rougeurs au début (erreurs de formatage, trailing whitespace...). Corrigez-les, puis commitez.*

### Étape 4 : Activer la CI
Pushez simplement les nouveaux fichiers sur votre branche `main` ou `master`.
```bash
git add .pre-commit-config.yaml .github/workflows/security.yml
git commit -m "chore: add Aegis-CI security layer"
git push
```
La pipeline GitHub Actions se déclenchera automatiquement.

---

## 🌍 Adaptation Multi-Langages
Aegis-CI est **agnostique** : il fonctionne avec tous les langages majeurs, car ses outils (Semgrep, Gitleaks, Trivy) savent analyser de nombreux formats.

### Ce qui fonctionne sans rien toucher (Universel)
*   **Secrets** (Gitleaks) : Détecte les clés API quel que soit le fichier.
*   **Infrastructure** (Checkov/Trivy) : Dockerfile, Kubernetes, Terraform, AWS SAM.
*   **Dépendances** (Trivy) : `package.json`, `pom.xml`, `go.sum`, `requirements.txt`, etc.

### Configuration spécifique par langage (Linting & SAST)
Pour aller plus loin, vous pouvez ajouter des "Linters" spécifiques dans le fichier `.pre-commit-config.yaml`.

#### 🐍 Python
Ajoutez `black` (formatage) et `flake8` (qualité) :
```yaml
-   repo: https://github.com/psf/black
    rev: 23.9.1
    hooks:
    -   id: black
```

#### 🌐 JavaScript / TypeScript / Node.js
Ajoutez `prettier` (formatage) et `eslint` (qualité) :
```yaml
-   repo: https://github.com/pre-commit/mirrors-prettier
    rev: v3.0.3
    hooks:
    -   id: prettier
-   repo: https://github.com/pre-commit/mirrors-eslint
    rev: v8.49.0
    hooks:
    -   id: eslint
```

#### ☕ Java / Kotlin
Semgrep détectera automatiquement les failles de sécurité. Pour le formatage, vous pouvez ajouter `google-java-format` :
```yaml
-   repo: https://github.com/maczam/google-java-format-pre-commit-hook
    rev: 1.17.0
    hooks:
    -   id: google-java-format
```

#### 🐹 Go (Golang)
Ajoutez `golangci-lint` :
```yaml
-   repo: https://github.com/golangci/golangci-lint
    rev: v1.54.2
    hooks:
    -   id: golangci-lint
```

#### 🐘 PHP
Ajoutez `php-cs-fixer` :
```yaml
-   repo: https://github.com/shivammathur/pre-commit-php
    rev: 2.26.0
    hooks:
    -   id: php-cs-fixer
```

### Note sur Semgrep (SAST)
L'action GitHub `semgrep-action` configurée dans `security.yml` utilise le ruleset `p/default`. Ce "pack" contient déjà des règles de sécurité pour :
*   Python, Go, Java, JavaScript, TypeScript, PHP, Ruby, C#, Scala, Rust, et plus.
*   **Vous n'avez pas besoin de changer la configuration CI pour supporter un nouveau langage.**
