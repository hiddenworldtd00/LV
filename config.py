"""
Configuration pour TCHAD_CYBER SECURITY
"""

# Couleurs ANSI
COLORS = {
    'green': '\033[92m',
    'red': '\033[91m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'cyan': '\033[96m',
    'magenta': '\033[95m',
    'white': '\033[97m',
    'bold': '\033[1m',
    'underline': '\033[4m',
    'reset': '\033[0m'
}

# Sources de livres
BOOK_SOURCES = {
    "1": {"name": "IT eBooks", "url": "https://it-ebooks.info"},
    "2": {"name": "Free Programming Books (GitHub)", "url": "https://github.com/EbookFoundation/free-programming-books"},
    "3": {"name": "PDF Drive", "url": "https://www.pdfdrive.com"},
    "4": {"name": "Library Genesis", "url": "http://libgen.rs"},
    "5": {"name": "Z-Library", "url": "https://z-lib.org"},
    "6": {"name": "Open Library", "url": "https://openlibrary.org"},
    "7": {"name": "Project Gutenberg", "url": "https://www.gutenberg.org"},
    "8": {"name": "O'Reilly Open Books", "url": "https://www.oreilly.com/openbook/"},
    "9": {"name": "Packt Free Learning", "url": "https://www.packtpub.com/free-learning"},
    "10": {"name": "Springer Free Books", "url": "https://link.springer.com"}
}

# Catégories de livres
BOOK_CATEGORIES = {
    "1": "Computer and Programming Languages",
    "2": "Computer Science",
    "3": "Data Science, Data Analysis and Databases",
    "4": "Software Engineering",
    "5": "Web Design and Programming",
    "6": "Computer Engineering",
    "7": "Mathematics",
    "8": "Java Programming",
    "9": "Unix and Linux",
    "10": "Microsoft and .NET",
    "11": "Mobile Computing and Programming",
    "12": "Networking and Communications",
    "13": "Special Topics"
}

# Sous-catégories
SUBCATEGORIES = {
    "Computer and Programming Languages": [
        "Python", "Java", "C++", "C#", "JavaScript", "HTML/CSS", "PHP", "Ruby",
        "Go", "Rust", "Swift", "Kotlin", "TypeScript", "SQL", "R", "MATLAB",
        "Arduino", "Assembly", "BASIC", "COBOL", "Fortran", "LISP", "Prolog",
        "Scala", "Haskell", "Lua", "Perl", "Dart", "Julia", "Objective-C"
    ],
    "Computer Science": [
        "Algorithms", "Data Structures", "Artificial Intelligence", "Machine Learning",
        "Deep Learning", "Neural Networks", "Computer Graphics", "Computer Vision",
        "Operating Systems", "Computer Architecture", "Compiler Design", "Cryptography",
        "Information Security", "Computer Networks", "Database Systems", "Software Engineering"
    ],
    "Data Science": [
        "Big Data", "Data Analysis", "Data Mining", "Data Visualization", "Machine Learning",
        "Deep Learning", "Statistics", "Probability", "R Programming", "Python for Data Science",
        "SQL", "NoSQL", "Data Engineering", "Business Intelligence"
    ],
    "Software Engineering": [
        "Agile", "Scrum", "DevOps", "Design Patterns", "Software Testing", "Version Control",
        "Microservices", "Cloud Computing", "Containerization", "CI/CD", "Software Architecture"
    ],
    "Web Design and Programming": [
        "HTML5", "CSS3", "JavaScript", "React", "Angular", "Vue.js", "Node.js",
        "PHP", "Python Web", "Ruby on Rails", "Web API", "RESTful Services", "Web Security"
    ],
    "Computer Engineering": [
        "Embedded Systems", "FPGA", "VLSI", "Digital Design", "Computer Architecture",
        "Robotics", "IoT", "GPU Programming", "Signal Processing", "Control Systems"
    ],
    "Mathematics": [
        "Algebra", "Calculus", "Linear Algebra", "Discrete Mathematics", "Probability",
        "Statistics", "Numerical Analysis", "Optimization", "Graph Theory", "Topology"
    ],
    "Java Programming": [
        "Core Java", "Java EE", "Spring Framework", "Android Development", "JavaFX",
        "Java Web Services", "Java Design Patterns", "Java Performance"
    ],
    "Unix and Linux": [
        "Linux Administration", "Shell Scripting", "System Programming", "Network Administration",
        "Linux Security", "Ubuntu", "CentOS", "Debian", "Kali Linux"
    ],
    "Microsoft and .NET": [
        "C#", "ASP.NET", ".NET Core", "Azure", "Windows Server", "PowerShell",
        "SQL Server", "Office Development", "Xamarin"
    ],
    "Mobile Computing": [
        "Android Development", "iOS Development", "React Native", "Flutter",
        "Mobile Security", "Mobile Game Development", "Swift", "Kotlin Mobile"
    ],
    "Networking": [
        "Network Security", "TCP/IP", "Wireless Networks", "Network Administration",
        "Cisco", "VPN", "Firewall", "Network Protocols", "IoT Networks"
    ],
    "Special Topics": [
        "Blockchain", "Cryptocurrency", "Quantum Computing", "Ethical Hacking",
        "Digital Forensics", "Game Development", "Virtual Reality", "Augmented Reality"
    ]
}

# Outils de sécurité
SECURITY_TOOLS = {
    "1": {"name": "Nmap", "description": "Scanner de ports et découverte réseau"},
    "2": {"name": "Metasploit", "description": "Framework de test d'intrusion"},
    "3": {"name": "Wireshark", "description": "Analyseur de protocoles réseau"},
    "4": {"name": "Aircrack-ng", "description": "Suite de sécurité WiFi"},
    "5": {"name": "Burp Suite", "description": "Test de sécurité des applications web"},
    "6": {"name": "John the Ripper", "description": "Craqueur de mots de passe"},
    "7": {"name": "Sqlmap", "description": "Injection SQL automatique"},
    "8": {"name": "Hydra", "description": "Craquage de mots de passe en ligne"}
}

# Niveaux de difficulté
DIFFICULTY_LEVELS = {
    "1": "Débutant",
    "2": "Intermédiaire",
    "3": "Avancé",
    "4": "Expert"
}
