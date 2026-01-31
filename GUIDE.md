# Aegis-CI: Le Guide Complet

Ce document détaille le fonctionnement interne d'Aegis-CI et comment l'utiliser au quotidien pour maintenir un haut niveau de sécurité.

## 1. Architecture du Projet

Aegis-CI est conçu autour de scripts Python modulaires situés dans `scripts/` et orchestrés par des hooks `pre-commit` ou une CI GitHub Actions.

```
Aegis-CI/
├── .github/workflows/   # Définition du pipeline CI/CD (GitHub Actions)
├── scripts/             # Cœur du framework
│   ├── dlp_check.py     # Module de détection de fuite de données (DLP)
│   ├── reporter.py      # Module de génération de rapports PDF (Style BSIC)
│   └── compliance_check.py # (À venir) Vérification des dépendances
├── tests/               # Tests unitaires (Pytest)
├── resources/           # Assets graphiques (Logos, Fonts)
├── .pre-commit-config.yaml # Configuration des hooks Git locaux
└── pyproject.toml       # Configuration du projet et des dépendances
```

## 2. Les Modules de Sécurité

### 2.1. Module DLP (`dlp_check.py`)
Ce script analyse les fichiers pour détecter des séquences numériques ressemblant à des cartes de crédit (PAN).
*   **Méthode** : Regex pour l'extraction de candidats + **Algorithme de Luhn** pour la validation.
*   **Usage** : Automatique via pre-commit, ou manuel : `python scripts/dlp_check.py <fichiers>`

### 2.2. Module Reporting (`reporter.py`)
Génère un rapport PDF officiel attestant de la conformité du code.
*   **Style** : Charte graphique BSIC (Bleu/Gris/Noir).
*   **Contenu** : Résumé des scans, badge de conformité PCI-DSS.
*   **Usage** : `python scripts/reporter.py`

## 3. Workflow de Développement

### Installer l'environnement de développement
Pour contribuer à Aegis-CI ou le modifier :

1.  Créer un virtualenv :
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # ou .venv\Scripts\activate sous Windows
    ```
2.  Installer en mode éditable :
    ```bash
    pip install -e .
    pip install pytest
    ```

### Lancer les Tests
Avant tout commit, assurez-vous que les tests passent :
```bash
pytest
```
Les tests couvrent notamment la logique critique de détection des cartes bancaires (`tests/test_dlp.py`).

## 4. Intégration Continue (CI)

Le fichier `.github/workflows/security.yml` définit le pipeline de sécurité. Il s'exécute à chaque `push` ou `pull_request`.

**Étapes du Pipeline :**
1.  **Unit Tests** : Vérifie que le code d'Aegis fonctionne correctement.
2.  **Secret Detection** : Gitleaks scanne l'historique pour trouver des clés API.
3.  **SAST** : Semgrep analyse le code pour trouver des failles de sécurité logiques.
4.  **SCA** : Trivy vérifie les vulnérabilités dans les dépendances.

## 5. FAQ

**Q: Comment changer le logo du rapport ?**
R: Remplacez le fichier `resources/logo-bsic.png`. Le script s'adapte automatiquement, mais un ratio rectangulaire est conseillé.

**Q: Le scan bloque mon commit légitime, que faire ?**
R: Si c'est un faux positif DLP, vérifiez que vous ne commitez pas de vrais numéros de test. Utilisez des numéros factices invalides pour Luhn si besoin. En dernier recours, `git commit --no-verify`.
