```text
    ___               _          ______ ____
   /   |  ___  ____ _(_)____    / ____//  _/
  / /| | / _ \/ __ `/ / ___/___/ /     / /
 / ___ |/  __/ /_/ / (__  )___/ /___ _/ /
/_/  |_|\___/\__, /_/____/            /____/
```
> **By Marshall Christ**

# Aegis-CI

**Aegis-CI** est un template de projet **DevSecOps** conçu pour intégrer la sécurité dès le début du cycle de développement (*Shift-Left Security*). Il fournit une configuration prête à l'emploi pour valider la qualité du code et détecter les vulnérabilités avant même qu'elles n'atteignent la production.

## 🚀 Fonctionnalités

### 🔒 Contrôles Locaux (Pre-commit)
Avant chaque commit, des hooks git vérifient automatiquement :
- **Absence de secrets** (clés API, mots de passe) via `gitleaks`.
- **Validité syntaxique** des fichiers YAML et JSON.
- **Propreté du code** (suppression des espaces inutiles, fin de fichiers correctes).
- **Taille des fichiers** pour éviter les commits de binaires volumineux.

### 🤖 Pipeline CI/CD (GitHub Actions)
À chaque push ou Pull Request, une pipeline de sécurité analyse le code :
- **SAST (Semgrep)** : Analyse statique pour détecter les failles de sécurité et bugs logiques.
- **SCA (Trivy)** : Scan des vulnérabilités dans les dépendances et fichiers de configuration.
- **Détéction de Secrets (Gitleaks)** : Vérification de l'historique git complet.
- **IaC Scanning (Checkov)** : Audit de sécurité pour Terraform, Docker, Kubernetes.

## 🛠️ Pré-requis

- [Python 3.x](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

## 📦 Installation

1. **Cloner le projet**
   ```bash
   git clone https://github.com/mmct13/Aegis-CI.git
   cd Aegis-CI
   ```

2. **Installer Pre-commit**
   ```bash
   pip install pre-commit
   ```

3. **Activer les hooks**
   ```bash
   pre-commit install
   ```
   *Désormais, les vérifications se lanceront à chaque `git commit`.*

## 🤝 Intégration dans d'autres projets

Vous voulez utiliser cette sécurité sur vos autres repos ?
👉 **Lisez le [Guide d'Intégration](INTEGRATION_GUIDE.md)** pour savoir comment l'installer sur un projet existant ou l'utiliser comme template.

## ⚙️ Utilisation

### Lancer les vérifications manuellement
Pour scanner tous les fichiers sans attendre un commit :
```bash
pre-commit run --all-files
```

### Ignorer une vérification (Déconseillé ⚠️)
En cas d'urgence absolue, vous pouvez bypasser les hooks (à utiliser avec précaution) :
```bash
git commit -m "Message" --no-verify
```

## 📄 Structure du Projet

```
Aegis-CI/
├── .github/
│   └── workflows/
│       └── security.yml    # Pipeline CI/CD de sécurité
├── .pre-commit-config.yaml # Configuration des hooks locaux
└── README.md               # Documentation
```
