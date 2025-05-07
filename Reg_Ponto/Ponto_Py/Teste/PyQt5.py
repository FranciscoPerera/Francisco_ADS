from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt5")

layout = QVBoxLayout()
label = QLabel("Olá, mundo!")
button = QPushButton("Clique aqui")
button.clicked.connect(lambda: label.setText("Você clicou!"))

layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
