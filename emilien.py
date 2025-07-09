import os
os.environ["QT_OPENGL"] = "software"

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit
from PyQt6.QtGui import QTextCursor, QTextBlockFormat
from PyQt6.QtCore import Qt

# 1. Créer l'application
app = QApplication(sys.argv)

# 2. Créer une fenêtre
fenetre = QWidget()
fenetre.setWindowTitle("EMILIEN alpha")
fenetre.resize(400, 300)

# 3. Zone d'affichage back end
zone_affichage = QTextEdit()
zone_affichage.setReadOnly(True)

# 4. Zone d'entrée utilisateur
zone_texte = QLineEdit()
zone_texte.setPlaceholderText("Tape ton message ici...")

# 5. Fonctions d'affichage
def append_right(text: str):
    cursor = zone_affichage.textCursor()
    cursor.movePosition(QTextCursor.MoveOperation.End)
    block_format = QTextBlockFormat()
    block_format.setAlignment(Qt.AlignmentFlag.AlignRight)
    cursor.insertBlock(block_format)
    cursor.insertText(text)
    zone_affichage.setTextCursor(cursor)

def append_left(text: str):
    cursor = zone_affichage.textCursor()
    cursor.movePosition(QTextCursor.MoveOperation.End)
    block_format = QTextBlockFormat()
    block_format.setAlignment(Qt.AlignmentFlag.AlignLeft)
    cursor.insertBlock(block_format)
    cursor.insertText(text)
    zone_affichage.setTextCursor(cursor)

def envoyer_message():
    texte = zone_texte.text().strip()
    if texte:
        append_right(f"👤 Vous : {texte}")
        append_left("🤖 Emilien : Bonjour, je suis Emilien une IA aplha en dev, malheureusement je ne peut pas vous aider pour le momment")
        zone_texte.clear()


# 6. Affichage ia
pass #le temps le mettre en place l'ia

# 7. Layout principal (⚠️ un seul layout)
layout = QVBoxLayout()
layout.addWidget(zone_affichage)
layout.addWidget(zone_texte)
zone_texte.returnPressed.connect(envoyer_message)
fenetre.setLayout(layout)  # ← on le pose ici, une seule fois

# 8. Afficher la fenêtre
fenetre.show()
sys.exit(app.exec())
