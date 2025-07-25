import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit,
    QLabel, QScrollArea, QPushButton
)
from PyQt6.QtGui import QTextCursor, QTextBlockFormat
from PyQt6.QtCore import Qt

# Liste des anciens chats (non utilisée ici, mais gardée si tu veux t'en servir plus tard)
chats_enregistres = []

# 1. Créer l'application
app = QApplication(sys.argv)

# 2. Créer une fenêtre
fenetre = QWidget()
fenetre.setWindowTitle("EMILIEN alpha")
fenetre.resize(600, 400)

# 3. Zone d'affichage du chat
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
    cursor.insertText(f"👤 {text}")
    zone_affichage.setTextCursor(cursor)

def append_left(text: str):
    cursor = zone_affichage.textCursor()
    cursor.movePosition(QTextCursor.MoveOperation.End)
    block_format = QTextBlockFormat()
    block_format.setAlignment(Qt.AlignmentFlag.AlignLeft)
    cursor.insertBlock(block_format)
    cursor.insertText(f"🤖 {text}")
    zone_affichage.setTextCursor(cursor)

def ajouter_chat(nom="Sans titre"):
    bouton = QPushButton(nom)
    bouton.clicked.connect(lambda _, n=nom: on_element_click(n))
    contenu_gauche.addWidget(bouton)
    chats_enregistres.append(nom)


# 6. Fonction principale pour envoyer message + réponse auto
def envoyer_message():
    texte = zone_texte.text().strip()
    if not texte:
        return

    append_right(texte)  # texte utilisateur à droite
    zone_texte.clear()

    # Réponse automatique simple
    reponse = "Salut, je suis Emilien. Une IA d'assistance, malheureusement je suis encore en developement, mais je pourrais bientot vous aider"
    append_left(reponse)

# 7. Zone latérale gauche avec boutons
contenu_gauche = QVBoxLayout()

def on_element_click(nom: str):
    if nom == "+ Nouveau Chat":
        zone_affichage.clear()
        append_left("🆕 Nouveau chat lancé.")
        ajouter_chat()  # 👈 ajoute le bouton "Sans titre"
    
    elif nom == "🔍 Rechercher Chat":
        append_left("🔍 Recherche non implémentée.")
    
    else:
        append_left(f"🤖 Tu as cliqué sur : {nom}")


# Boutons de base
for nom in ["+ Nouveau Chat", "🔍 Rechercher Chat"]:
    bouton = QPushButton(nom)
    bouton.clicked.connect(lambda _, n=nom: on_element_click(n))
    contenu_gauche.addWidget(bouton)

# 8. Scroll à gauche
zone_gauche_widget = QWidget()
zone_gauche_widget.setLayout(contenu_gauche)

zone_scroll = QScrollArea()
zone_scroll.setWidgetResizable(True)
zone_scroll.setWidget(zone_gauche_widget)
zone_scroll.setFixedWidth(180)

# 9. Layouts finaux
layout_droite = QVBoxLayout()
layout_droite.addWidget(zone_affichage)
layout_droite.addWidget(zone_texte)
zone_texte.returnPressed.connect(envoyer_message)

layout_principal = QHBoxLayout()
layout_principal.addWidget(zone_scroll)
layout_principal.addLayout(layout_droite)

fenetre.setLayout(layout_principal)
fenetre.show()
sys.exit(app.exec())
