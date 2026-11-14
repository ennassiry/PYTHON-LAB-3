class Document:
    def __init__(self, titre, annee):
        self.titre = titre
        self.annee = annee

    def afficher(self):
        print(f"{self.titre} ({self.annee})")

class Livre(Document):
    def __init__(self, titre, annee, auteur):
        super().__init__(titre, annee)
        self.auteur = auteur

    def afficher(self):
        print(f"Livre: {self.titre} par {self.auteur} ({self.annee})")

class Magazine(Document):
    def __init__(self, titre, annee, numero):
        super().__init__(titre, annee)
        self.numero = numero

    def afficher(self):
        print(f"Magazine: {self.titre} No. {self.numero} ({self.annee})")

documents = [
    Livre("La Boite a merveilles", 1954, "Ahmed Sefrioui"),
    Magazine("Science & Vie", 2023, 456),
    Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupery"),
    Magazine("National Geographic", 2024, 120),
    Livre("L'Etranger", 1942, "Albert Camus"),
    Magazine("Geo", 2024, 530),
    Livre("Les Miserables", 1862, "Victor Hugo")
]

for doc in documents:
    doc.afficher()