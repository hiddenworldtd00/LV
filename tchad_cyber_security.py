#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ████████╗ ██████╗██╗  ██╗ █████╗ ██████╗      ██████╗██╗   ██╗██████╗ ███████╗██████╗  ║
║   ╚══██╔══╝██╔════╝██║  ██║██╔══██╗██╔══██╗    ██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗ ║
║      ██║   ██║     ███████║███████║██║  ██║    ██║     ██║   ██║██████╔╝█████╗  ██████╔╝ ║
║      ██║   ██║     ██╔══██║██╔══██║██║  ██║    ██║     ██║   ██║██╔══██╗██╔══╝  ██╔══██╗ ║
║      ██║   ╚██████╗██║  ██║██║  ██║██████╔╝    ╚██████╗╚██████╔╝██║  ██║███████╗██║  ██║ ║
║      ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ║
║                                                                              ║
║                    ███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗████████╗██╗   ██╗          ║
║                    ██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝          ║
║                    ███████╗█████╗  ██║     ██║   ██║██████╔╝██║   ██║    ╚████╔╝           ║
║                    ╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██║   ██║     ╚██╔╝            ║
║                    ███████║███████╗╚██████╗╚██████╔╝██║  ██║██║   ██║      ██║             ║
║                    ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

    TCHAD_CYBER SECURITY - Bibliothèque Numérique Mondiale
    ======================================================
    
    Plateforme de téléchargement et de gestion de livres techniques
    Couvrant : Informatique, Programmation, Cybersécurité, Mathématiques,
    Sciences, Ingénierie, et bien plus encore.
    
    Auteur: TCHAD_CYBER SECURITY Team
    Version: 2.0.0
    Licence: MIT
"""

import os
import sys
import json
import time
import random
import hashlib
import threading
import webbrowser
from datetime import datetime
from urllib.parse import quote, unquote
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Callable
from enum import Enum

# Couleurs pour le terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[35m'
    WHITE = '\033[37m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    @staticmethod
    def print_banner():
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ████████╗ ██████╗██╗  ██╗ █████╗ ██████╗      ██████╗██╗   ██╗██████╗ ███████╗██████╗  ║
║   ╚══██╔══╝██╔════╝██║  ██║██╔══██╗██╔══██╗    ██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗ ║
║      ██║   ██║     ███████║███████║██║  ██║    ██║     ██║   ██║██████╔╝█████╗  ██████╔╝ ║
║      ██║   ██║     ██╔══██║██╔══██║██║  ██║    ██║     ██║   ██║██╔══██╗██╔══╝  ██╔══██╗ ║
║      ██║   ╚██████╗██║  ██║██║  ██║██████╔╝    ╚██████╗╚██████╔╝██║  ██║███████╗██║  ██║ ║
║      ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ║
║                                                                              ║
║                    ███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗████████╗██╗   ██╗          ║
║                    ██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝          ║
║                    ███████╗█████╗  ██║     ██║   ██║██████╔╝██║   ██║    ╚████╔╝           ║
║                    ╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██║   ██║     ╚██╔╝            ║
║                    ███████║███████╗╚██████╗╚██████╔╝██║  ██║██║   ██║      ██║             ║
║                    ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.END}
{Colors.GREEN}{Colors.BOLD}                    Bibliothèque Numérique Mondiale - v2.0.0{Colors.END}
{Colors.YELLOW}                    Votre porte d'accès au savoir mondial{Colors.END}
        """
        print(banner)


class Category(Enum):
    """Catégories de livres disponibles"""
    PROGRAMMING_LANGUAGES = "Langages de Programmation"
    COMPUTER_SCIENCE = "Sciences Informatiques"
    DATA_SCIENCE = "Science des Données"
    SOFTWARE_ENGINEERING = "Génie Logiciel"
    WEB_DEVELOPMENT = "Développement Web"
    COMPUTER_ENGINEERING = "Génie Informatique"
    MATHEMATICS = "Mathématiques"
    JAVA = "Java"
    UNIX_LINUX = "Unix et Linux"
    MICROSOFT = "Microsoft et .NET"
    MOBILE = "Mobile"
    NETWORKING = "Réseaux et Communications"
    SPECIAL_TOPICS = "Sujets Spéciaux"
    SECURITY = "Cybersécurité"
    DATABASES = "Bases de Données"
    ARTIFICIAL_INTELLIGENCE = "Intelligence Artificielle"
    CLOUD_COMPUTING = "Cloud Computing"
    IOT = "Internet des Objets"
    QUANTUM_COMPUTING = "Informatique Quantique"
    BLOCKCHAIN = "Blockchain et Cryptomonnaies"


@dataclass
class Book:
    """Représentation d'un livre"""
    id: str
    title: str
    author: str
    category: str
    subcategory: str
    description: str
    language: str
    pages: int
    year: int
    publisher: str
    isbn: str
    file_size: str
    file_format: str
    download_url: str
    rating: float
    downloads: int
    tags: List[str]
    cover_image: str
    preview_url: str
    
    def to_dict(self) -> Dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Book':
        return cls(**data)


class BookDatabase:
    """Base de données des livres"""
    
    def __init__(self):
        self.books: List[Book] = []
        self.categories: Dict[str, List[str]] = {}
        self._initialize_database()
    
    def _initialize_database(self):
        """Initialise la base de données avec les catégories et livres"""
        self._setup_categories()
        self._load_sample_books()
    
    def _setup_categories(self):
        """Configure les catégories et sous-catégories"""
        self.categories = {
            Category.PROGRAMMING_LANGUAGES.value: [
                "Ada", "Arduino", "Assembly", "BASIC", "C", "C++", "C#", "COBOL",
                "CSS", "Dart", "Delphi", "Eiffel", "Erlang", "Forth", "Fortran",
                "Go", "Haskell", "HTML", "Java", "JavaScript", "Julia", "Kotlin",
                "LISP", "Lua", "MATLAB", "Objective-C", "OCaml", "Pascal", "Perl",
                "PHP", "Prolog", "Python", "R", "Ruby", "Rust", "Scala", "Scheme",
                "Scratch", "Shell", "Smalltalk", "SQL", "Swift", "Tcl/Tk", "TypeScript",
                "UML", "XML", "VHDL", "Verilog", "FPGA"
            ],
            Category.COMPUTER_SCIENCE.value: [
                "Algorithms", "Data Structures", "Artificial Intelligence", "Big Data",
                "Bioinformatics", "Blockchain", "Compiler Design", "Computer Architecture",
                "Computer Graphics", "Computer Vision", "Cryptography", "Cybersecurity",
                "Database Systems", "Deep Learning", "Distributed Systems", "Embedded Systems",
                "Functional Programming", "Game Programming", "Human-Computer Interaction",
                "Information Retrieval", "Machine Learning", "Natural Language Processing",
                "Neural Networks", "Operating Systems", "Parallel Computing", "Quantum Computing",
                "Robotics", "Software Engineering", "Theory of Computation", "Virtual Reality"
            ],
            Category.DATA_SCIENCE.value: [
                "Bayesian Thinking", "Big Data", "Data Analysis", "Data Engineering",
                "Data Mining", "Data Visualization", "Deep Learning", "Machine Learning",
                "Neural Networks", "Probability Theory", "Statistics", "R Programming",
                "Python for Data Science", "SQL", "NoSQL", "Database Theory"
            ],
            Category.SOFTWARE_ENGINEERING.value: [
                "Agile", "DevOps", "Design Patterns", "Microservices", "Cloud Computing",
                "Containers", "Testing", "Version Control", "Software Architecture",
                "Project Management", "CI/CD", "Refactoring", "Clean Code"
            ],
            Category.WEB_DEVELOPMENT.value: [
                "HTML/CSS", "JavaScript", "React", "Angular", "Vue.js", "Node.js",
                "PHP", "Python Web", "Ruby on Rails", "Web APIs", "Web Security",
                "SEO", "Web Design", "Progressive Web Apps", "WebAssembly"
            ],
            Category.COMPUTER_ENGINEERING.value: [
                "Arduino", "Embedded Systems", "FPGA", "HDL", "IoT", "Microcontrollers",
                "VLSI", "Digital Signal Processing", "Computer Architecture", "GPU Programming",
                "Raspberry Pi", "Robotics", "Real-Time Systems"
            ],
            Category.MATHEMATICS.value: [
                "Algebra", "Calculus", "Combinatorics", "Differential Equations",
                "Discrete Mathematics", "Geometry", "Graph Theory", "Linear Algebra",
                "Number Theory", "Numerical Analysis", "Optimization", "Probability",
                "Statistics", "Topology", "Trigonometry", "Mathematical Logic"
            ],
            Category.SECURITY.value: [
                "Cryptography", "Ethical Hacking", "Network Security", "Web Security",
                "Malware Analysis", "Digital Forensics", "Penetration Testing",
                "Security Architecture", "Incident Response", "Risk Management",
                "Steganography", "Reverse Engineering"
            ],
            Category.ARTIFICIAL_INTELLIGENCE.value: [
                "Machine Learning", "Deep Learning", "Neural Networks", "NLP",
                "Computer Vision", "Reinforcement Learning", "Expert Systems",
                "Robotics", "Cognitive Computing", "AI Ethics"
            ],
            Category.CLOUD_COMPUTING.value: [
                "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes",
                "Serverless", "Cloud Architecture", "DevOps", "Microservices",
                "Infrastructure as Code"
            ],
            Category.IOT.value: [
                "Arduino", "Raspberry Pi", "Embedded Systems", "Sensor Networks",
                "Smart Home", "Industrial IoT", "IoT Security", "Edge Computing",
                "Wireless Communications", "RFID"
            ],
            Category.BLOCKCHAIN.value: [
                "Bitcoin", "Ethereum", "Smart Contracts", "DeFi", "NFT",
                "Blockchain Development", "Cryptocurrency", "Consensus Algorithms",
                "Distributed Ledger", "Web3"
            ],
            Category.QUANTUM_COMPUTING.value: [
                "Quantum Algorithms", "Quantum Cryptography", "Quantum Mechanics",
                "Qiskit", "Quantum Hardware", "Quantum Machine Learning",
                "Quantum Information Theory"
            ]
        }
    
    def _load_sample_books(self):
        """Charge des exemples de livres"""
        sample_books = [
            Book(
                id=self._generate_id(),
                title="Python Programming: From Beginner to Expert",
                author="John Smith",
                category=Category.PROGRAMMING_LANGUAGES.value,
                subcategory="Python",
                description="Un guide complet pour maîtriser Python, des bases à l'expertise.",
                language="English",
                pages=450,
                year=2023,
                publisher="Tech Books Inc.",
                isbn="978-3-16-148410-0",
                file_size="15.2 MB",
                file_format="PDF",
                download_url="https://example.com/books/python-expert.pdf",
                rating=4.8,
                downloads=12500,
                tags=["python", "programming", "beginner", "advanced"],
                cover_image="https://example.com/covers/python.jpg",
                preview_url="https://example.com/preview/python"
            ),
            Book(
                id=self._generate_id(),
                title="Cybersecurity Fundamentals",
                author="Alice Johnson",
                category=Category.SECURITY.value,
                subcategory="Network Security",
                description="Les bases essentielles de la cybersécurité pour les professionnels.",
                language="English",
                pages=380,
                year=2023,
                publisher="Security Press",
                isbn="978-1-23-456789-0",
                file_size="12.5 MB",
                file_format="PDF",
                download_url="https://example.com/books/cybersec-fundamentals.pdf",
                rating=4.6,
                downloads=8900,
                tags=["security", "cybersecurity", "network", "fundamentals"],
                cover_image="https://example.com/covers/cybersec.jpg",
                preview_url="https://example.com/preview/cybersec"
            ),
            Book(
                id=self._generate_id(),
                title="Machine Learning avec Python",
                author="Pierre Dupont",
                category=Category.ARTIFICIAL_INTELLIGENCE.value,
                subcategory="Machine Learning",
                description="Apprenez le machine learning avec des exemples pratiques en Python.",
                language="French",
                pages=520,
                year=2023,
                publisher="Éditions Tech",
                isbn="978-2-34-567890-1",
                file_size="18.7 MB",
                file_format="PDF",
                download_url="https://example.com/books/ml-python.pdf",
                rating=4.9,
                downloads=15200,
                tags=["machine learning", "python", "AI", "data science"],
                cover_image="https://example.com/covers/ml-python.jpg",
                preview_url="https://example.com/preview/ml-python"
            ),
            Book(
                id=self._generate_id(),
                title="Deep Learning for Computer Vision",
                author="Sarah Chen",
                category=Category.ARTIFICIAL_INTELLIGENCE.value,
                subcategory="Deep Learning",
                description="Techniques avancées de deep learning pour la vision par ordinateur.",
                language="English",
                pages=480,
                year=2023,
                publisher="AI Press",
                isbn="978-0-12-345678-9",
                file_size="22.3 MB",
                file_format="PDF",
                download_url="https://example.com/books/dl-vision.pdf",
                rating=4.7,
                downloads=9800,
                tags=["deep learning", "computer vision", "AI", "neural networks"],
                cover_image="https://example.com/covers/dl-vision.jpg",
                preview_url="https://example.com/preview/dl-vision"
            ),
            Book(
                id=self._generate_id(),
                title="Blockchain et Cryptomonnaies",
                author="Jean Martin",
                category=Category.BLOCKCHAIN.value,
                subcategory="Bitcoin",
                description="Comprendre la blockchain et les cryptomonnaies de A à Z.",
                language="French",
                pages=340,
                year=2023,
                publisher="Crypto Éditions",
                isbn="978-3-45-678901-2",
                file_size="11.8 MB",
                file_format="PDF",
                download_url="https://example.com/books/blockchain.pdf",
                rating=4.5,
                downloads=7600,
                tags=["blockchain", "bitcoin", "cryptocurrency", "DeFi"],
                cover_image="https://example.com/covers/blockchain.jpg",
                preview_url="https://example.com/preview/blockchain"
            ),
            Book(
                id=self._generate_id(),
                title="Linux System Administration",
                author="Robert Wilson",
                category=Category.UNIX_LINUX.value,
                subcategory="System Administration",
                description="Administration système Linux pour les professionnels.",
                language="English",
                pages=560,
                year=2023,
                publisher="Linux Press",
                isbn="978-4-56-789012-3",
                file_size="19.5 MB",
                file_format="PDF",
                download_url="https://example.com/books/linux-admin.pdf",
                rating=4.8,
                downloads=11200,
                tags=["linux", "administration", "system", "server"],
                cover_image="https://example.com/covers/linux-admin.jpg",
                preview_url="https://example.com/preview/linux-admin"
            ),
            Book(
                id=self._generate_id(),
                title="Cloud Architecture avec AWS",
                author="Marie Dubois",
                category=Category.CLOUD_COMPUTING.value,
                subcategory="AWS",
                description="Concevoir des architectures cloud robustes avec AWS.",
                language="French",
                pages=420,
                year=2023,
                publisher="Cloud Éditions",
                isbn="978-5-67-890123-4",
                file_size="16.2 MB",
                file_format="PDF",
                download_url="https://example.com/books/aws-architecture.pdf",
                rating=4.6,
                downloads=8900,
                tags=["cloud", "AWS", "architecture", "devops"],
                cover_image="https://example.com/covers/aws.jpg",
                preview_url="https://example.com/preview/aws"
            ),
            Book(
                id=self._generate_id(),
                title="IoT: Internet des Objets",
                author="Ahmed Hassan",
                category=Category.IOT.value,
                subcategory="Embedded Systems",
                description="Construire des projets IoT avec Arduino et Raspberry Pi.",
                language="French",
                pages=380,
                year=2023,
                publisher="IoT Press",
                isbn="978-6-78-901234-5",
                file_size="14.8 MB",
                file_format="PDF",
                download_url="https://example.com/books/iot.pdf",
                rating=4.4,
                downloads=6500,
                tags=["IoT", "arduino", "raspberry pi", "embedded"],
                cover_image="https://example.com/covers/iot.jpg",
                preview_url="https://example.com/preview/iot"
            ),
            Book(
                id=self._generate_id(),
                title="Quantum Computing: A Gentle Introduction",
                author="Dr. Emily Brown",
                category=Category.QUANTUM_COMPUTING.value,
                subcategory="Quantum Algorithms",
                description="Introduction accessible à l'informatique quantique.",
                language="English",
                pages=320,
                year=2023,
                publisher="Quantum Press",
                isbn="978-7-89-012345-6",
                file_size="13.5 MB",
                file_format="PDF",
                download_url="https://example.com/books/quantum.pdf",
                rating=4.7,
                downloads=4200,
                tags=["quantum", "computing", "physics", "algorithms"],
                cover_image="https://example.com/covers/quantum.jpg",
                preview_url="https://example.com/preview/quantum"
            ),
            Book(
                id=self._generate_id(),
                title="Data Structures and Algorithms in Java",
                author="Michael Lee",
                category=Category.COMPUTER_SCIENCE.value,
                subcategory="Algorithms",
                description="Structures de données et algorithmes implémentés en Java.",
                language="English",
                pages=580,
                year=2023,
                publisher="Java Press",
                isbn="978-8-90-123456-7",
                file_size="20.1 MB",
                file_format="PDF",
                download_url="https://example.com/books/java-algorithms.pdf",
                rating=4.9,
                downloads=14500,
                tags=["java", "algorithms", "data structures", "programming"],
                cover_image="https://example.com/covers/java-algo.jpg",
                preview_url="https://example.com/preview/java-algo"
            )
        ]
        self.books.extend(sample_books)
    
    def _generate_id(self) -> str:
        """Génère un ID unique pour un livre"""
        return hashlib.md5(str(time.time() + random.random()).encode()).hexdigest()[:12]
    
    def search_books(self, query: str, category: Optional[str] = None) -> List[Book]:
        """Recherche des livres par titre, auteur ou tags"""
        results = []
        query_lower = query.lower()
        
        for book in self.books:
            if category and book.category != category:
                continue
            
            if (query_lower in book.title.lower() or
                query_lower in book.author.lower() or
                query_lower in book.description.lower() or
                any(query_lower in tag.lower() for tag in book.tags)):
                results.append(book)
        
        return results
    
    def get_books_by_category(self, category: str) -> List[Book]:
        """Récupère les livres par catégorie"""
        return [book for book in self.books if book.category == category]
    
    def get_book_by_id(self, book_id: str) -> Optional[Book]:
        """Récupère un livre par son ID"""
        for book in self.books:
            if book.id == book_id:
                return book
        return None
    
    def get_all_categories(self) -> List[str]:
        """Récupère toutes les catégories"""
        return list(self.categories.keys())
    
    def get_subcategories(self, category: str) -> List[str]:
        """Récupère les sous-catégories d'une catégorie"""
        return self.categories.get(category, [])
    
    def get_popular_books(self, limit: int = 10) -> List[Book]:
        """Récupère les livres les plus populaires"""
        return sorted(self.books, key=lambda x: x.downloads, reverse=True)[:limit]
    
    def get_recent_books(self, limit: int = 10) -> List[Book]:
        """Récupère les livres les plus récents"""
        return sorted(self.books, key=lambda x: x.year, reverse=True)[:limit]
    
    def add_book(self, book: Book):
        """Ajoute un nouveau livre"""
        self.books.append(book)
    
    def export_to_json(self, filename: str):
        """Exporte la base de données en JSON"""
        data = {
            "books": [book.to_dict() for book in self.books],
            "categories": self.categories,
            "export_date": datetime.now().isoformat(),
            "total_books": len(self.books)
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def import_from_json(self, filename: str):
        """Importe une base de données depuis JSON"""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        self.books = [Book.from_dict(book_data) for book_data in data.get("books", [])]
        self.categories = data.get("categories", {})


class DownloadManager:
    """Gestionnaire de téléchargements"""
    
    def __init__(self, download_dir: str = "downloads"):
        self.download_dir = download_dir
        self.download_history: List[Dict] = []
        self._ensure_download_dir()
    
    def _ensure_download_dir(self):
        """Crée le répertoire de téléchargement s'il n'existe pas"""
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
    
    def download_book(self, book: Book, progress_callback: Optional[Callable] = None) -> bool:
        """Télécharge un livre"""
        try:
            print(f"\n{Colors.CYAN}Téléchargement de : {Colors.BOLD}{book.title}{Colors.END}")
            print(f"{Colors.YELLOW}Auteur : {book.author}{Colors.END}")
            print(f"{Colors.YELLOW}Format : {book.file_format} | Taille : {book.file_size}{Colors.END}")
            
            # Simulation du téléchargement
            file_path = os.path.join(self.download_dir, f"{book.id}_{book.title.replace(' ', '_')}.pdf")
            
            print(f"\n{Colors.BLUE}Début du téléchargement...{Colors.END}")
            
            # Simulation de la barre de progression
            for i in range(0, 101, 10):
                time.sleep(0.3)
                bar = "█" * (i // 5) + "░" * (20 - i // 5)
                print(f"\r{Colors.GREEN}[{bar}] {i}%{Colors.END}", end="", flush=True)
                if progress_callback:
                    progress_callback(i)
            
            print(f"\n\n{Colors.GREEN}{Colors.BOLD}✓ Téléchargement terminé !{Colors.END}")
            print(f"{Colors.CYAN}Fichier sauvegardé : {file_path}{Colors.END}")
            
            # Enregistrement dans l'historique
            self.download_history.append({
                "book_id": book.id,
                "title": book.title,
                "download_date": datetime.now().isoformat(),
                "file_path": file_path,
                "status": "completed"
            })
            
            return True
            
        except Exception as e:
            print(f"\n{Colors.RED}{Colors.BOLD}✗ Erreur lors du téléchargement : {str(e)}{Colors.END}")
            return False
    
    def get_download_history(self) -> List[Dict]:
        """Récupère l'historique des téléchargements"""
        return self.download_history
    
    def clear_history(self):
        """Efface l'historique des téléchargements"""
        self.download_history.clear()


class UserPreferences:
    """Gestion des préférences utilisateur"""
    
    def __init__(self, config_file: str = "user_config.json"):
        self.config_file = config_file
        self.preferences = {
            "language": "fr",
            "theme": "dark",
            "download_dir": "downloads",
            "items_per_page": 10,
            "auto_download": False,
            "notifications": True,
            "favorite_categories": [],
            "reading_list": []
        }
        self._load_preferences()
    
    def _load_preferences(self):
        """Charge les préférences depuis le fichier"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.preferences.update(json.load(f))
            except Exception:
                pass
    
    def save_preferences(self):
        """Sauvegarde les préférences"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.preferences, f, ensure_ascii=False, indent=2)
    
    def get(self, key: str, default=None):
        """Récupère une préférence"""
        return self.preferences.get(key, default)
    
    def set(self, key: str, value):
        """Définit une préférence"""
        self.preferences[key] = value
        self.save_preferences()


class TchadCyberSecurity:
    """Application principale TCHAD_CYBER SECURITY"""
    
    def __init__(self):
        self.db = BookDatabase()
        self.download_manager = DownloadManager()
        self.preferences = UserPreferences()
        self.running = True
    
    def clear_screen(self):
        """Efface l'écran"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_menu(self):
        """Affiche le menu principal"""
        print(f"\n{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.END}")
        print(f"{Colors.GREEN}{Colors.BOLD}  MENU PRINCIPAL{Colors.END}")
        print(f"{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.END}\n")
        
        menu_items = [
            ("1", "Rechercher un livre", Colors.BLUE),
            ("2", "Parcourir par catégorie", Colors.BLUE),
            ("3", "Livres populaires", Colors.YELLOW),
            ("4", "Livres récents", Colors.YELLOW),
            ("5", "Télécharger un livre", Colors.GREEN),
            ("6", "Historique de téléchargements", Colors.CYAN),
            ("7", "Mes favoris", Colors.MAGENTA),
            ("8", "Préférences", Colors.WHITE),
            ("9", "Exporter la base de données", Colors.GREEN),
            ("10", "Importer une base de données", Colors.GREEN),
            ("11", "Statistiques", Colors.YELLOW),
            ("12", "À propos", Colors.WHITE),
            ("0", "Quitter", Colors.RED)
        ]
        
        for num, text, color in menu_items:
            print(f"  {color}{Colors.BOLD}[{num}]{Colors.END} {text}")
        
        print(f"\n{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.END}\n")
    
    def search_books(self):
        """Recherche de livres"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}RECHERCHE DE LIVRES{Colors.END}\n")
        query = input(f"{Colors.CYAN}Entrez votre recherche (titre, auteur, tag) : {Colors.END}").strip()
        
        if not query:
            print(f"{Colors.RED}Recherche annulée.{Colors.END}")
            return
        
        # Option de filtre par catégorie
        print(f"\n{Colors.YELLOW}Filtrer par catégorie ?{Colors.END}")
        categories = self.db.get_all_categories()
        for i, cat in enumerate(categories, 1):
            print(f"  {Colors.CYAN}[{i}]{Colors.END} {cat}")
        print(f"  {Colors.CYAN}[0]{Colors.END} Toutes les catégories")
        
        try:
            choice = int(input(f"\n{Colors.CYAN}Votre choix : {Colors.END}"))
            category = categories[choice - 1] if 1 <= choice <= len(categories) else None
        except (ValueError, IndexError):
            category = None
        
        results = self.db.search_books(query, category)
        
        if not results:
            print(f"\n{Colors.RED}{Colors.BOLD}Aucun livre trouvé pour '{query}'.{Colors.END}")
            return
        
        print(f"\n{Colors.GREEN}{Colors.BOLD}{len(results)} livre(s) trouvé(s) :{Colors.END}\n")
        self._display_books(results)
    
    def browse_categories(self):
        """Parcourir les catégories"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}CATÉGORIES DISPONIBLES{Colors.END}\n")
        
        categories = self.db.get_all_categories()
        for i, cat in enumerate(categories, 1):
            book_count = len(self.db.get_books_by_category(cat))
            print(f"  {Colors.CYAN}[{i}]{Colors.END} {cat} {Colors.YELLOW}({book_count} livres){Colors.END}")
        
        try:
            choice = int(input(f"\n{Colors.CYAN}Choisissez une catégorie (0 pour retour) : {Colors.END}"))
            if choice == 0:
                return
            
            if 1 <= choice <= len(categories):
                category = categories[choice - 1]
                books = self.db.get_books_by_category(category)
                
                print(f"\n{Colors.GREEN}{Colors.BOLD}Livres dans '{category}' :{Colors.END}\n")
                self._display_books(books)
                
                # Afficher les sous-catégories
                subcategories = self.db.get_subcategories(category)
                if subcategories:
                    print(f"\n{Colors.YELLOW}Sous-catégories :{Colors.END}")
                    for sub in subcategories:
                        print(f"  {Colors.CYAN}•{Colors.END} {sub}")
        
        except (ValueError, IndexError):
            print(f"{Colors.RED}Choix invalide.{Colors.END}")
    
    def popular_books(self):
        """Affiche les livres populaires"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}LIVRES LES PLUS POPULAIRES{Colors.END}\n")
        books = self.db.get_popular_books(10)
        self._display_books(books)
    
    def recent_books(self):
        """Affiche les livres récents"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}LIVRES RÉCENTS{Colors.END}\n")
        books = self.db.get_recent_books(10)
        self._display_books(books)
    
    def download_book(self):
        """Télécharge un livre"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}TÉLÉCHARGEMENT DE LIVRE{Colors.END}\n")
        
        # Rechercher d'abord le livre
        query = input(f"{Colors.CYAN}Rechercher un livre à télécharger : {Colors.END}").strip()
        
        if not query:
            print(f"{Colors.RED}Opération annulée.{Colors.END}")
            return
        
        results = self.db.search_books(query)
        
        if not results:
            print(f"\n{Colors.RED}Aucun livre trouvé.{Colors.END}")
            return
        
        print(f"\n{Colors.GREEN}Livres trouvés :{Colors.END}\n")
        for i, book in enumerate(results, 1):
            print(f"  {Colors.CYAN}[{i}]{Colors.END} {book.title} - {book.author}")
        
        try:
            choice = int(input(f"\n{Colors.CYAN}Choisissez un livre à télécharger (0 pour annuler) : {Colors.END}"))
            if choice == 0:
                return
            
            if 1 <= choice <= len(results):
                book = results[choice - 1]
                self.download_manager.download_book(book)
        
        except (ValueError, IndexError):
            print(f"{Colors.RED}Choix invalide.{Colors.END}")
    
    def download_history(self):
        """Affiche l'historique des téléchargements"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}HISTORIQUE DES TÉLÉCHARGEMENTS{Colors.END}\n")
        
        history = self.download_manager.get_download_history()
        
        if not history:
            print(f"{Colors.YELLOW}Aucun téléchargement effectué.{Colors.END}")
            return
        
        for i, item in enumerate(history, 1):
            print(f"{Colors.CYAN}{i}.{Colors.END} {Colors.BOLD}{item['title']}{Colors.END}")
            print(f"   Date : {item['download_date']}")
            print(f"   Statut : {Colors.GREEN}{item['status']}{Colors.END}")
            print(f"   Fichier : {item['file_path']}\n")
    
    def manage_favorites(self):
        """Gère les favoris"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}MES FAVORIS{Colors.END}\n")
        
        favorites = self.preferences.get("favorite_categories", [])
        
        if favorites:
            print(f"{Colors.YELLOW}Catégories favorites :{Colors.END}")
            for fav in favorites:
                print(f"  {Colors.CYAN}•{Colors.END} {fav}")
        else:
            print(f"{Colors.YELLOW}Aucune catégorie favorite.{Colors.END}")
        
        print(f"\n{Colors.CYAN}[1]{Colors.END} Ajouter une catégorie favorite")
        print(f"{Colors.CYAN}[2]{Colors.END} Retirer une catégorie favorite")
        print(f"{Colors.CYAN}[0]{Colors.END} Retour")
        
        try:
            choice = int(input(f"\n{Colors.CYAN}Votre choix : {Colors.END}"))
            
            if choice == 1:
                categories = self.db.get_all_categories()
                for i, cat in enumerate(categories, 1):
                    print(f"  {Colors.CYAN}[{i}]{Colors.END} {cat}")
                
                cat_choice = int(input(f"\n{Colors.CYAN}Choisissez une catégorie : {Colors.END}"))
                if 1 <= cat_choice <= len(categories):
                    cat = categories[cat_choice - 1]
                    if cat not in favorites:
                        favorites.append(cat)
                        self.preferences.set("favorite_categories", favorites)
                        print(f"\n{Colors.GREEN}✓ '{cat}' ajouté aux favoris !{Colors.END}")
            
            elif choice == 2 and favorites:
                for i, fav in enumerate(favorites, 1):
                    print(f"  {Colors.CYAN}[{i}]{Colors.END} {fav}")
                
                fav_choice = int(input(f"\n{Colors.CYAN}Choisissez une catégorie à retirer : {Colors.END}"))
                if 1 <= fav_choice <= len(favorites):
                    removed = favorites.pop(fav_choice - 1)
                    self.preferences.set("favorite_categories", favorites)
                    print(f"\n{Colors.GREEN}✓ '{removed}' retiré des favoris.{Colors.END}")
        
        except (ValueError, IndexError):
            print(f"{Colors.RED}Choix invalide.{Colors.END}")
    
    def preferences_menu(self):
        """Menu des préférences"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}PRÉFÉRENCES{Colors.END}\n")
        
        print(f"{Colors.CYAN}[1]{Colors.END} Langue actuelle : {Colors.YELLOW}{self.preferences.get('language')}{Colors.END}")
        print(f"{Colors.CYAN}[2]{Colors.END} Thème : {Colors.YELLOW}{self.preferences.get('theme')}{Colors.END}")
        print(f"{Colors.CYAN}[3]{Colors.END} Répertoire de téléchargement : {Colors.YELLOW}{self.preferences.get('download_dir')}{Colors.END}")
        print(f"{Colors.CYAN}[4]{Colors.END} Éléments par page : {Colors.YELLOW}{self.preferences.get('items_per_page')}{Colors.END}")
        print(f"{Colors.CYAN}[5]{Colors.END} Notifications : {Colors.YELLOW}{'Activées' if self.preferences.get('notifications') else 'Désactivées'}{Colors.END}")
        print(f"{Colors.CYAN}[0]{Colors.END} Retour")
        
        try:
            choice = int(input(f"\n{Colors.CYAN}Votre choix : {Colors.END}"))
            
            if choice == 1:
                lang = input(f"{Colors.CYAN}Nouvelle langue (fr/en) : {Colors.END}").strip()
                if lang in ["fr", "en"]:
                    self.preferences.set("language", lang)
                    print(f"{Colors.GREEN}✓ Langue mise à jour !{Colors.END}")
            
            elif choice == 2:
                theme = input(f"{Colors.CYAN}Nouveau thème (dark/light) : {Colors.END}").strip()
                if theme in ["dark", "light"]:
                    self.preferences.set("theme", theme)
                    print(f"{Colors.GREEN}✓ Thème mis à jour !{Colors.END}")
            
            elif choice == 3:
                dir_path = input(f"{Colors.CYAN}Nouveau répertoire : {Colors.END}").strip()
                if dir_path:
                    self.preferences.set("download_dir", dir_path)
                    self.download_manager.download_dir = dir_path
                    print(f"{Colors.GREEN}✓ Répertoire mis à jour !{Colors.END}")
            
            elif choice == 4:
                items = int(input(f"{Colors.CYAN}Nombre d'éléments par page : {Colors.END}"))
                if items > 0:
                    self.preferences.set("items_per_page", items)
                    print(f"{Colors.GREEN}✓ Préférence mise à jour !{Colors.END}")
            
            elif choice == 5:
                current = self.preferences.get("notifications")
                self.preferences.set("notifications", not current)
                status = "activées" if not current else "désactivées"
                print(f"{Colors.GREEN}✓ Notifications {status} !{Colors.END}")
        
        except ValueError:
            print(f"{Colors.RED}Valeur invalide.{Colors.END}")
    
    def export_database(self):
        """Exporte la base de données"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}EXPORT DE LA BASE DE DONNÉES{Colors.END}\n")
        
        filename = input(f"{Colors.CYAN}Nom du fichier (défaut: database_export.json) : {Colors.END}").strip()
        if not filename:
            filename = "database_export.json"
        
        if not filename.endswith('.json'):
            filename += '.json'
        
        try:
            self.db.export_to_json(filename)
            print(f"\n{Colors.GREEN}{Colors.BOLD}✓ Base de données exportée avec succès !{Colors.END}")
            print(f"{Colors.CYAN}Fichier : {filename}{Colors.END}")
            print(f"{Colors.CYAN}Total livres : {len(self.db.books)}{Colors.END}")
        except Exception as e:
            print(f"\n{Colors.RED}{Colors.BOLD}✗ Erreur lors de l'export : {str(e)}{Colors.END}")
    
    def import_database(self):
        """Importe une base de données"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}IMPORT DE BASE DE DONNÉES{Colors.END}\n")
        
        filename = input(f"{Colors.CYAN}Nom du fichier JSON : {Colors.END}").strip()
        
        if not filename or not os.path.exists(filename):
            print(f"{Colors.RED}Fichier non trouvé.{Colors.END}")
            return
        
        try:
            self.db.import_from_json(filename)
            print(f"\n{Colors.GREEN}{Colors.BOLD}✓ Base de données importée avec succès !{Colors.END}")
            print(f"{Colors.CYAN}Total livres : {len(self.db.books)}{Colors.END}")
        except Exception as e:
            print(f"\n{Colors.RED}{Colors.BOLD}✗ Erreur lors de l'import : {str(e)}{Colors.END}")
    
    def show_statistics(self):
        """Affiche les statistiques"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}STATISTIQUES{Colors.END}\n")
        
        total_books = len(self.db.books)
        total_categories = len(self.db.categories)
        total_subcategories = sum(len(subs) for subs in self.db.categories.values())
        total_downloads = sum(book.downloads for book in self.db.books)
        avg_rating = sum(book.rating for book in self.db.books) / total_books if total_books > 0 else 0
        
        print(f"{Colors.CYAN}📚 Total de livres :{Colors.END} {Colors.BOLD}{total_books}{Colors.END}")
        print(f"{Colors.CYAN}📁 Catégories :{Colors.END} {Colors.BOLD}{total_categories}{Colors.END}")
        print(f"{Colors.CYAN}📂 Sous-catégories :{Colors.END} {Colors.BOLD}{total_subcategories}{Colors.END}")
        print(f"{Colors.CYAN}⬇️  Téléchargements totaux :{Colors.END} {Colors.BOLD}{total_downloads:,}{Colors.END}")
        print(f"{Colors.CYAN}⭐ Note moyenne :{Colors.END} {Colors.BOLD}{avg_rating:.2f}/5.0{Colors.END}")
        
        print(f"\n{Colors.YELLOW}{Colors.BOLD}Répartition par catégorie :{Colors.END}\n")
        for category in self.db.get_all_categories():
            count = len(self.db.get_books_by_category(category))
            bar_length = int((count / max(total_books, 1)) * 30)
            bar = "█" * bar_length
            print(f"  {Colors.CYAN}{category:<30}{Colors.END} {Colors.GREEN}{bar}{Colors.END} {count}")
    
    def about(self):
        """Affiche les informations sur l'application"""
        print(f"""
{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.END}
{Colors.GREEN}{Colors.BOLD}
                         TCHAD_CYBER SECURITY
                    Bibliothèque Numérique Mondiale
{Colors.END}
{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.END}

{Colors.YELLOW}Version :{Colors.END} 2.0.0
{Colors.YELLOW}Auteur :{Colors.END} TCHAD_CYBER SECURITY Team
{Colors.YELLOW}Licence :{Colors.END} MIT

{Colors.CYAN}Description :{Colors.END}
  Cette application permet d'accéder à une vaste bibliothèque de livres
  techniques couvrant l'informatique, la programmation, la cybersécurité,
  les mathématiques, les sciences et l'ingénierie.

{Colors.CYAN}Fonctionnalités :{Colors.END}
  • Recherche avancée de livres
  • Navigation par catégories et sous-catégories
  • Téléchargement de livres
  • Gestion des favoris
  • Historique de téléchargements
  • Export/Import de base de données
  • Statistiques détaillées

{Colors.CYAN}Contact :{Colors.END}
  Email : contact@tchad-cyber-security.td
  Web   : www.tchad-cyber-security.td

{Colors.YELLOW}© 2024 TCHAD_CYBER SECURITY. Tous droits réservés.{Colors.END}
        """)
    
    def _display_books(self, books: List[Book]):
        """Affiche une liste de livres"""
        if not books:
            print(f"{Colors.YELLOW}Aucun livre à afficher.{Colors.END}")
            return
        
        for i, book in enumerate(books, 1):
            print(f"{Colors.CYAN}{'─'*70}{Colors.END}")
            print(f"{Colors.GREEN}{Colors.BOLD}[{i}] {book.title}{Colors.END}")
            print(f"  {Colors.YELLOW}Auteur :{Colors.END} {book.author}")
            print(f"  {Colors.YELLOW}Catégorie :{Colors.END} {book.category} > {book.subcategory}")
            print(f"  {Colors.YELLOW}Description :{Colors.END} {book.description}")
            print(f"  {Colors.YELLOW}Langue :{Colors.END} {book.language} | {Colors.YELLOW}Pages :{Colors.END} {book.pages} | {Colors.YELLOW}Année :{Colors.END} {book.year}")
            print(f"  {Colors.YELLOW}Format :{Colors.END} {book.file_format} | {Colors.YELLOW}Taille :{Colors.END} {book.file_size}")
            print(f"  {Colors.YELLOW}ISBN :{Colors.END} {book.isbn}")
            print(f"  {Colors.YELLOW}Éditeur :{Colors.END} {book.publisher}")
            print(f"  {Colors.YELLOW}Note :{Colors.END} {'⭐' * int(book.rating)} {book.rating}/5.0")
            print(f"  {Colors.YELLOW}Téléchargements :{Colors.END} {book.downloads:,}")
            print(f"  {Colors.YELLOW}Tags :{Colors.END} {', '.join(book.tags)}")
            print(f"{Colors.CYAN}{'─'*70}{Colors.END}\n")
    
    def run(self):
        """Boucle principale de l'application"""
        self.clear_screen()
        Colors.print_banner()
        
        print(f"{Colors.GREEN}Bienvenue dans TCHAD_CYBER SECURITY !{Colors.END}")
        print(f"{Colors.YELLOW}Chargement de la base de données...{Colors.END}")
        time.sleep(1)
        
        while self.running:
            self.print_menu()
            
            try:
                choice = input(f"{Colors.CYAN}{Colors.BOLD}Votre choix : {Colors.END}").strip()
                
                if choice == "1":
                    self.search_books()
                elif choice == "2":
                    self.browse_categories()
                elif choice == "3":
                    self.popular_books()
                elif choice == "4":
                    self.recent_books()
                elif choice == "5":
                    self.download_book()
                elif choice == "6":
                    self.download_history()
                elif choice == "7":
                    self.manage_favorites()
                elif choice == "8":
                    self.preferences_menu()
                elif choice == "9":
                    self.export_database()
                elif choice == "10":
                    self.import_database()
                elif choice == "11":
                    self.show_statistics()
                elif choice == "12":
                    self.about()
                elif choice == "0":
                    self.running = False
                    print(f"\n{Colors.GREEN}{Colors.BOLD}Merci d'avoir utilisé TCHAD_CYBER SECURITY !{Colors.END}")
                    print(f"{Colors.YELLOW}À bientôt ! 👋{Colors.END}\n")
                else:
                    print(f"\n{Colors.RED}Choix invalide. Veuillez réessayer.{Colors.END}")
                
                if self.running:
                    input(f"\n{Colors.CYAN}Appuyez sur Entrée pour continuer...{Colors.END}")
                    self.clear_screen()
                    Colors.print_banner()
            
            except KeyboardInterrupt:
                print(f"\n\n{Colors.YELLOW}Interruption détectée. Au revoir !{Colors.END}")
                self.running = False
            except Exception as e:
                print(f"\n{Colors.RED}{Colors.BOLD}Erreur : {str(e)}{Colors.END}")
                input(f"\n{Colors.CYAN}Appuyez sur Entrée pour continuer...{Colors.END}")


def main():
    """Point d'entrée principal"""
    try:
        app = TchadCyberSecurity()
        app.run()
    except Exception as e:
        print(f"{Colors.RED}{Colors.BOLD}Erreur fatale : {str(e)}{Colors.END}")
        sys.exit(1)


if __name__ == "__main__":
    main()
