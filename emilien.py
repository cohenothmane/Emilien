import sys
from PyQt6.QtWidgets import QApplication, QWidget

# 1. Créer l'application
app = QApplication(sys.argv)

# 2. Créer une fenêtre (widget de base)
fenetre = QWidget()
fenetre.setWindowTitle("Ma première fenêtre PyQt")
fenetre.resize(400, 300)  # largeur, hauteur

# 3. Afficher la fenêtre
fenetre.show()

# 4. Lancer la boucle d'événements
sys.exit(app.exec())
