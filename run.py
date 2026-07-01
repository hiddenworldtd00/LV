#!/usr/bin/env python3
"""
TCHAD_CYBER SECURITY - Script de lancement
"""

import sys
import os

# Ajouter le répertoire courant au path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tchad_cyber_security import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Interrompu par l'utilisateur")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Erreur: {e}")
        sys.exit(1)