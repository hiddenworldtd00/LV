#TCHAD_CYBER_SECURITY

**TCHAD_CYBER_SECURITY** est une plateforme complète de téléchargement de livres informatiques et de cybersécurité. Ce script Python offre une interface en ligne de commande intuitive pour rechercher, télécharger et organiser des ressources éducatives dans le domaine de la cybersécurité et de l'informatique.

## 🚀 Fonctionnalités

- **Recherche avancée** de livres par titre, auteur, catégorie ou sujet
- **Téléchargement** de livres avec barre de progression
- **Organisation automatique** par catégories et sujets
- **Base de données locale** SQLite pour le suivi des téléchargements
- **Mode hors-ligne** avec livres intégrés
- **Génération de rapports** et statistiques
- **Support multilingue** (Français/Anglais)
- **Recommandations personnalisées**
- **Favoris et listes de lecture**
- **Vérification d'intégrité** des fichiers (hash MD5)

## 📚 Catégories Supportées

### Langages de Programmation
Python, Java, C/C++, JavaScript, C#, PHP, Ruby, Go, Rust, Swift, Kotlin, TypeScript, et 50+ autres

### Cybersécurité
- Hacking éthique et pentesting
- Cryptographie et cryptanalyse
- Forensics et investigation numérique
- Sécurité des réseaux
- Reverse engineering
- Steganographie

### Informatique
- Intelligence Artificielle et Machine Learning
- Big Data et Data Science
- Développement Web et Mobile
- Architecture des systèmes
- Bases de données
- Cloud Computing

## 🛠️ Installation

### Prérequis
- Python 3.7+
- pip (gestionnaire de paquets Python)

### Installation des dépendances

```bash
# Cloner ou télécharger le projet
cd TCHAD_CYBER_SECURITY

# Installer les dépendances
pip install -r requirements.txt
```

### Fichier requirements.txt
```
requests>=2.28.0
beautifulsoup4>=4.11.0
colorama>=0.4.5
tqdm>=4.64.0
```

## 🎯 Utilisation

### Lancer l'application
```bash
python tchad_cyber_security.py
```

### Menu Principal
1. **Rechercher des livres** - Recherche par mot-clé, catégorie ou sujet
2. **Télécharger des livres** - Téléchargement avec sélection multiple
3. **Parcourir par catégorie** - Navigation par catégories prédéfinies
4. **Mes téléchargements** - Gestion des livres téléchargés
5. **Favoris** - Liste des livres favoris
6. **Statistiques** - Rapports et analyses
7. **Mode hors-ligne** - Livres intégrés disponibles sans connexion
8. **Paramètres** - Configuration de l'application
9. **Aide** - Documentation intégrée

### Exemples d'utilisation

```bash
# Recherche rapide
python tchad_cyber_security.py --search "python hacking"

# Télécharger par catégorie
python tchad_cyber_security.py --category "Cybersecurity"

# Mode hors-ligne
python tchad_cyber_security.py --offline

# Générer un rapport
python tchad_cyber_security.py --report
```

## 📁 Structure du Projet

```
TCHAD_CYBER_SECURITY/
├── tchad_cyber_security.py    # Script principal
├── config.py                   # Configuration et catégories
├── README.md                   # Documentation
├── requirements.txt            # Dépendances Python
├── downloads/                  # Dossier de téléchargement
│   ├── Computer_and_Programming_Languages/
│   ├── Computer_Science/
│   ├── Cybersecurity/
│   ├── Data_Science/
│   ├── Software_Engineering/
│   ├── Web_Development/
│   ├── Computer_Engineering/
│   ├── Mathematics/
│   ├── Java_Programming/
│   ├── Unix_Linux/
│   ├── Microsoft_NET/
│   ├── Mobile_Computing/
│   ├── Networking/
│   └── Special_Topics/
├── database/
│   └── tchad_cybersec.db      # Base de données SQLite
└── logs/
    └── app.log                 # Fichier de log
```

## 🔧 Configuration

Le fichier `config.py` contient toutes les configurations modifiables :

- **DOWNLOAD_DIR** : Dossier de téléchargement par défaut
- **DATABASE_PATH** : Chemin de la base de données
- **MAX_CONCURRENT_DOWNLOADS** : Nombre max de téléchargements simultanés
- **DEFAULT_LANGUAGE** : Langue par défaut (fr/en)
- **THEME** : Thème de couleur (green/blue/red/yellow/cyan)

## 🌐 Sources de Livres

Le script supporte les sources suivantes :
- IT eBooks (http://it-ebooks.info)
- Free Programming Books (GitHub)
- Open Library
- Livres intégrés (mode hors-ligne)

## 📝 Notes Importantes

- Respectez les droits d'auteur des livres téléchargés
- Utilisez ce logiciel à des fins éducatives uniquement
- Certains livres peuvent nécessiter une connexion Internet
- Le mode hors-ligne utilise une bibliothèque de livres intégrés

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Ajouter de nouvelles catégories
- Traduire l'interface

## 📜 Licence

Ce projet est open source et disponible sous licence MIT.

## 👨‍💻 Auteur

**TCHAD_CYBER_SECURITY** - Plateforme éducative de cybersécurité

Développé avec ❤️ pour la communauté de cybersécurité du Tchad et du monde entier.

---

**⚠️ Avertissement** : Ce logiciel est destiné à des fins éducatives uniquement. L'utilisation illégale de ce logiciel est strictement interdite. Respectez toujours les lois sur le droit d'auteur de votre pays.
