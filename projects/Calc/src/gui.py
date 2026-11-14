import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

import operations

ESTILO = """
QMainWindow, QWidget { background: #17191f; color: #f1f3f5; font-family: 'Segoe UI', sans-serif; }
QLabel#titulo { color: #aeb5c2; font-size: 13px; }
QLineEdit#visor {
    background: #22252d; border: 1px solid #343944; border-radius: 12px;
    padding: 14px; color: #ffffff; font-size: 32px; font-weight: 600;
}
QPushButton {
    background: #30343d; color: #f4f5f7; border: 0; border-radius: 12px;
    min-width: 58px; min-height: 48px; font-size: 18px; font-weight: 600;
}
QPushButton:hover { background: #414652; }
QPushButton#funcao { background: #252932; color: #c6ccd6; font-size: 14px; }
QPushButton#funcao:hover { background: #343944; }
QPushButton#operador { background: #3b4658; color: #c9ddff; }
QPushButton#igual { background: #6d8cff; color: #ffffff; }
QPushButton#limpar { background: #633d46; color: #ffd9df; }
QListWidget { background: #22252d; border: 1px solid #343944; border-radius: 10px; padding: 6px; color: #d6dae1; }
"""


class CalculadoraGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setFixedSize(580, 520)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.valor_atual = "0"
        self.valor_anterior = None
        self.operador_pendente = None
        self.iniciar_novo_numero = True

        raiz = QWidget()
        self.setCentralWidget(raiz)
        layout = QVBoxLayout(raiz)
        layout.setContentsMargins(22, 20, 22, 20)
        layout.setSpacing(10)

        titulo = QLabel("CALCULADORA")
        titulo.setObjectName("titulo")
        layout.addWidget(titulo)

        self.visor = QLineEdit("0")
        self.visor.setObjectName("visor")
        self.visor.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.visor.setReadOnly(True)
        layout.addWidget(self.visor)

        corpo = QHBoxLayout()
        corpo.setSpacing(16)
        layout.addLayout(corpo, 1)

        grelha = QGridLayout()
        grelha.setSpacing(8)
        corpo.addLayout(grelha, 3)

        botoes = [
            ("%", 0, 0, "funcao"), ("CE", 0, 1, "limpar"), ("C", 0, 2, "limpar"), ("⌫", 0, 3, "funcao"),
            ("1/x", 1, 0, "funcao"), ("x²", 1, 1, "funcao"), ("√x", 1, 2, "funcao"), ("÷", 1, 3, "operador"),
            ("7", 2, 0, ""), ("8", 2, 1, ""), ("9", 2, 2, ""), ("×", 2, 3, "operador"),
            ("4", 3, 0, ""), ("5", 3, 1, ""), ("6", 3, 2, ""), ("−", 3, 3, "operador"),
            ("1", 4, 0, ""), ("2", 4, 1, ""), ("3", 4, 2, ""), ("+", 4, 3, "operador"),
            ("±", 5, 0, "funcao"), ("0", 5, 1, ""), (".", 5, 2, ""), ("=", 5, 3, "igual"),
        ]
        for texto, linha, coluna, estilo in botoes:
            botao = QPushButton(texto)
            botao.setFixedSize(64, 48)
            if estilo:
                botao.setObjectName(estilo)
            botao.clicked.connect(lambda _checked=False, tecla=texto: self.pressionar(tecla))
            grelha.addWidget(botao, linha, coluna)

        painel = QVBoxLayout()
        painel.addWidget(QLabel("Científica"))
        corpo.addLayout(painel, 2)
        cientificas = [
            ("xʸ", self.potencia), ("log", self.logaritmo), ("n!", self.fatorial),
            ("Equação quadrática", self.quadratica), ("Divisão inteira", self.divisao_inteira),
        ]
        for texto, acao in cientificas:
            botao = QPushButton(texto)
            botao.setObjectName("funcao")
            botao.setFixedSize(168, 36)
            botao.clicked.connect(acao)
            painel.addWidget(botao)

        painel.addWidget(QLabel("Histórico"))
        self.historico = QListWidget()
        painel.addWidget(self.historico, 1)
        limpar_historico = QPushButton("Limpar histórico")
        limpar_historico.setObjectName("funcao")
        limpar_historico.setFixedSize(168, 32)
        limpar_historico.clicked.connect(self.historico.clear)
        painel.addWidget(limpar_historico)

    def pressionar(self, tecla):
        if tecla.isdigit():
            if self.iniciar_novo_numero or self.valor_atual == "0":
                self.valor_atual = tecla
                self.iniciar_novo_numero = False
            else:
                self.valor_atual += tecla
        elif tecla == ".":
            if self.iniciar_novo_numero:
                self.valor_atual = "0."
                self.iniciar_novo_numero = False
            elif "." not in self.valor_atual:
                self.valor_atual += "."
        elif tecla in ("+", "−", "×", "÷"):
            self.definir_operador(tecla)
        elif tecla == "=":
            self.calcular_pendente()
        elif tecla == "C":
            self.limpar()
        elif tecla == "CE":
            self.valor_atual = "0"
            self.iniciar_novo_numero = True
        elif tecla == "⌫":
            if not self.iniciar_novo_numero and len(self.valor_atual) > 1:
                self.valor_atual = self.valor_atual[:-1]
            else:
                self.valor_atual = "0"
        elif tecla == "±":
            self.valor_atual = str(-float(self.valor_atual))
        elif tecla == "%":
            self.valor_atual = str(float(self.valor_atual) / 100)
        self.atualizar_visor()

    def definir_operador(self, operador):
        if self.operador_pendente and not self.iniciar_novo_numero:
            self.calcular_pendente()
        self.valor_anterior = float(self.valor_atual)
        self.operador_pendente = operador
        self.iniciar_novo_numero = True

    def calcular_pendente(self):
        if self.operador_pendente is None or self.valor_anterior is None:
            return
        a, b = self.valor_anterior, float(self.valor_atual)
        simbolo = self.operador_pendente
        funcoes = {"+": operations.somar, "−": operations.subtrair_valores,
                   "×": operations.multiplicar, "÷": operations.dividir}
        resultado = funcoes[simbolo](a, b)
        self.registar(f"{self.formatar_numero(a)} {simbolo} {self.formatar_numero(b)}", resultado)
        if isinstance(resultado, (int, float)):
            self.valor_atual = str(resultado)
        else:
            self.valor_atual = "0"
            QMessageBox.warning(self, "Não foi possível calcular", str(resultado))
        self.valor_anterior = None
        self.operador_pendente = None
        self.iniciar_novo_numero = True

    def aplicar_unaria(self, nome, funcao):
        valor = float(self.valor_atual)
        resultado = funcao(valor)
        self.registar(f"{nome}({self.formatar_numero(valor)})", resultado)
        if isinstance(resultado, (int, float)):
            self.valor_atual = str(resultado)
            self.iniciar_novo_numero = True
        else:
            QMessageBox.warning(self, "Não foi possível calcular", str(resultado))
        self.atualizar_visor()

    def potencia(self):
        base, ok = QInputDialog.getDouble(self, "Potência", "Expoente:", decimals=6)
        if ok:
            self.aplicar_unaria(f"x^{base:g}", lambda x: operations.calcular_potencia(x, base))

    def logaritmo(self):
        base, ok = QInputDialog.getDouble(self, "Logaritmo", "Base:", value=10, decimals=6)
        if ok:
            self.aplicar_unaria(f"log base {base:g}", lambda x: operations.calcular_logaritmo(base, x))

    def fatorial(self):
        self.aplicar_unaria("fatorial", operations.calcular_fatorial)

    def quadratica(self):
        valores = []
        for nome in ("a", "b", "c"):
            valor, ok = QInputDialog.getDouble(self, "Equação quadrática", f"Valor de {nome}:", decimals=6)
            if not ok:
                return
            valores.append(valor)
        resultado = operations.resolver_quadratica(*valores)
        self.registar(f"Equação quadrática ({', '.join(map(str, valores))})", resultado)
        self.valor_atual = str(resultado) if isinstance(resultado, (int, float)) else "0"
        self.atualizar_visor()
        if not isinstance(resultado, (int, float)):
            QMessageBox.information(self, "Resultado", str(resultado))

    def divisao_inteira(self):
        divisor, ok = QInputDialog.getDouble(self, "Divisão inteira", "Divisor:", decimals=6)
        if ok:
            self.aplicar_unaria(f"divisão inteira por {divisor:g}", lambda x: operations.dividir_inteiros(x, divisor))

    def limpar(self):
        self.valor_atual = "0"
        self.valor_anterior = None
        self.operador_pendente = None
        self.iniciar_novo_numero = True

    def registar(self, expressao, resultado):
        texto = str(resultado)
        self.historico.insertItem(0, f"{expressao} = {texto}")

    def atualizar_visor(self):
        try:
            self.visor.setText(self.formatar_numero(float(self.valor_atual)))
        except ValueError:
            self.visor.setText(self.valor_atual)

    @staticmethod
    def formatar_numero(valor):
        return str(operations.formato(valor))


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(ESTILO)
    janela = CalculadoraGUI()
    janela.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
