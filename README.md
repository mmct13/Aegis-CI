```text
    ___               _          ______ ____
   /   |  ___  ____ _(_)____    / ____//  _/
  / /| | / _ \/ __ `/ / ___/___/ /     / /
 / ___ |/  __/ /_/ / (__  )___/ /___ _/ /
/_/  |_|\___/\__, /_/____/   /______/___/
```

> **Aegis-CI**: The Banking-Grade DevSecOps Framework.
> *Protecting Financial Data at the Source.*

![CI Status](https://img.shields.io/github/actions/workflow/status/mmct13/Aegis-CI/security.yml?style=for-the-badge)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Compliance](https://img.shields.io/badge/compliance-PCI--DSS-gold?style=for-the-badge)

## 🛡️ Presentation

**Aegis-CI** is a modular security framework designed to integrate seamlessly into CI/CD pipelines. It acts as a shield, preventing sensitive banking data leaks (PAN, IBAN) and critical software vulnerabilities from ever reaching production.

Built for high-security environments (Banking/Finance), it ensures **Continuous Compliance** with strict security standards like PCI-DSS.

### 🚀 Key Features

*   **💳 Banking DLP (Data Loss Prevention)**: 
    *   Algorithmic detection (Luhn) of Credit Card Numbers (PAN).
    *   Blocks commits containing sensitive data in any file format.
*   **👮 Compliance Gatekeeper**:
    *   **SCA**: Dependency scanning (`safety`) against known CVEs.
    *   **Zero-Trust**: Blocks deployments with critical vulnerabilities.
*   **📊 Executive Reporting (BSIC Standard)**:
    *   Generates professional PDF security certificates.
    *   **BSIC Branded**: Official colors and logo integration for board-level reporting.
*   **🔒 Standard Hygiene**:
    *   Secret detection (API Keys, Tokens) via `gitleaks`.
    *   Code quality & linting enforcement.

## 🛠️ Installation & Usage

### Prerequisites
*   Python 3.8+
*   Git

### Quick Start (For Developers)

1.  **Clone the repository**
    ```bash
    git clone https://github.com/mmct13/Aegis-CI.git
    cd Aegis-CI
    ```

2.  **Install Dependencies**
    ```bash
    pip install .
    # Or for development:
    pip install -r requirements.txt
    ```

3.  **Run Tests**
    ```bash
    pytest
    ```

4.  **Generate a Report**
    ```bash
    python scripts/reporter.py
    ```
    *This will generate `aegis_report.pdf` in the current directory.*

## 🤝 Integration

To use Aegis-CI in **your** project (as a security layer), please refer to the [Integration Guide](INTEGRATION_GUIDE.md).

## 📄 Documentation

*   **[Full Guide (GUIDE.md)](GUIDE.md)**: Detailed instructions on architecture and extending the framework.
*   **[Integration Guide](INTEGRATION_GUIDE.md)**: How to add Aegis-CI to existing repositories.

## 👨‍💻 Contributing

We welcome contributions! Please see `CONTRIBUTING.md` (coming soon) for details.

---
*Built with ❤️ for Secure Banking.*
