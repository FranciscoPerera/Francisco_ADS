from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QTextEdit, QMessageBox
)
from datetime import datetime
import pytz
import sys

# Dados e lógica
fuso_horario = pytz.timezone("America/Sao_Paulo")

codigo = {
    "01": "Francisco",
    "02": "Aguado",
    "03": "Luiza",
    "04": "Gabriel",
    "05": "Ana"
}

registros_ponto = {k: [] for k in codigo.keys()}

def adiciona_ponto(cod, tipo):
    agora = datetime.now(fuso_horario)
    registros_ponto[cod].append((tipo, agora.strftime("%d/%m/%Y %H:%M:%S")))
    return agora.strftime("%d/%m/%Y %H:%M:%S")

# Interface Gráfica
class FolhaPontoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folha de Ponto")
        self.setFixedSize(400, 400)

        self.usuario = None
        self.cod = ""

        self.layout = QVBoxLayout()

        self.label_info = QLabel("Digite seu código de funcionário:")
        self.input_cod = QLineEdit()
        self.btn_entrar = QPushButton("Entrar")
        self.btn_entrar.clicked.connect(self.verificar_usuario)

        self.label_usuario = QLabel("")

        self.botoes_layout = QHBoxLayout()
        self.btns = {}
        for i, nome in enumerate(["Entrada", "Saída intervalo", "Retorno intervalo", "Saída"]):
            btn = QPushButton(nome)
            btn.clicked.connect(self.registrar_ponto)
            btn.setEnabled(False)
            self.btns[nome] = btn
            self.botoes_layout.addWidget(btn)

        self.btn_ver_registros = QPushButton("Ver Registros")
        self.btn_ver_registros.setEnabled(False)
        self.btn_ver_registros.clicked.connect(self.ver_registros)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)

        self.layout.addWidget(self.label_info)
        self.layout.addWidget(self.input_cod)
        self.layout.addWidget(self.btn_entrar)
        self.layout.addWidget(self.label_usuario)
        self.layout.addLayout(self.botoes_layout)
        self.layout.addWidget(self.btn_ver_registros)
        self.layout.addWidget(self.text_area)

        self.setLayout(self.layout)

    def verificar_usuario(self):
        cod = self.input_cod.text().strip()
        if cod in codigo:
            self.usuario = codigo[cod]
            self.cod = cod
            self.label_usuario.setText(f"Bem-vindo(a), {self.usuario}!")
            for btn in self.btns.values():
                btn.setEnabled(True)
            self.btn_ver_registros.setEnabled(True)
        else:
            QMessageBox.warning(self, "Erro", "Usuário inexistente!")

    def registrar_ponto(self):
        sender = self.sender()
        tipo = sender.text()
        horario = adiciona_ponto(self.cod, tipo)
        QMessageBox.information(self, "Ponto Registrado", f"{tipo} registrado às {horario}")

    def ver_registros(self):
        self.text_area.clear()
        if registros_ponto[self.cod]:
            self.text_area.append("----- Registros de Ponto -----")
            for tipo, horario in registros_ponto[self.cod]:
                self.text_area.append(f"{tipo}: {horario}")
            self.text_area.append("------------------------------")
        else:
            self.text_area.setText("Nenhum ponto registrado ainda.")

# Executa a aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = FolhaPontoApp()
    janela.show()
    sys.exit(app.exec())
