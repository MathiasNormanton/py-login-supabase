import sys
import os
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, 
                            QMessageBox, QHBoxLayout, QStackedWidget)
from PyQt5.QtCore import Qt, QSize, QPoint
from PyQt5.QtGui import QPixmap, QIcon, QMouseEvent

# Definir URL e chave de API do Supabase
url = "Digite dentro dos parenteses a sua NEXT_PUBLIC_SUPABASE_URL"
key = "Digite dentro dos parenteses a sua NEXT_PUBLIC_SUPABASE_ANON_KEY"

# Importar supabase
import supabase

# Conectar ao Supabase
supabase = supabase.create_client(url, key)

# Função para baixar ícones
def download_icon(url, filename):
    # Obtém o diretório atual do script main.py
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    # Cria o caminho para a pasta 'icons' no mesmo diretório do main.py
    pasta_icons = os.path.join(dir_atual, 'icons')
    # Verifica se a pasta 'icons' existe, se não, cria ela
    if not os.path.exists(pasta_icons):
        os.makedirs(pasta_icons)
    # Caminho completo do arquivo para salvar
    filepath = os.path.join(pasta_icons, filename)
    # Só baixa se o arquivo não existir
    if not os.path.exists(filepath):
        try:
            response = requests.get(url)
            with open(filepath, 'wb') as f:
                f.write(response.content)
        except Exception as e:
            print(f"Erro ao baixar ícone: {e}")
    return filepath

# Baixar ícones
logo_path = download_icon("https://cdn-icons-png.flaticon.com/128/15708/15708987.png", "dolphin.png")  # Link do golfinho
user_path = download_icon("https://cdn-icons-png.flaticon.com/128/3917/3917711.png", "user.png")
password_path = download_icon("https://cdn-icons-png.flaticon.com/128/3917/3917642.png", "password.png")
close_path = download_icon("https://cdn-icons-png.flaticon.com/128/3917/3917759.png", "close.png")
plus_path = download_icon("https://cdn-icons-png.flaticon.com/128/3917/3917688.png", "plus.png")

class LoginApp(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.oldPos = None  # Para rastrear a posição anterior durante o arrasto
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Py-Login // Loguinzito")
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove a barra de título do sistema
        
        # Estilo para a janela - Tema claro com elementos pretos
        self.setStyleSheet("""
            background-color: #ffffff;
            font-family: 'Segoe UI', Arial, sans-serif;
            color: #333333;
        """)
        
        # Criar páginas
        self.login_page = self.create_login_page()
        self.register_page = self.create_register_page()
        self.welcome_page = self.create_welcome_page()  # Nova página após login
        
        # Adicionar páginas ao stacked widget
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.register_page)
        self.stacked_widget.addWidget(self.welcome_page)
        
        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.setLayout(main_layout)
        self.setFixedSize(380, 420)
    
    # Métodos para permitir arrastar a janela
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.oldPos:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = None
        
    def create_login_page(self):
        login_widget = QWidget()
        layout = QVBoxLayout()
        
        # Barra superior com botão de fechar
        barra_superior = QHBoxLayout()
        barra_superior.addStretch()
        
        # Botão X para fechar à direita
        fechar_btn = QPushButton()
        fechar_btn.setIcon(QIcon(close_path))
        fechar_btn.setIconSize(QSize(16, 16))
        fechar_btn.setStyleSheet("""
            background-color: transparent;
            border: none;
        """)
        fechar_btn.setFixedSize(24, 24)
        fechar_btn.clicked.connect(self.close)
        barra_superior.addWidget(fechar_btn, alignment=Qt.AlignRight)
        
        layout.addLayout(barra_superior)
        
        # Adicionar logo de golfinho (centralizado)
        logo_label = QLabel()
        pixmap = QPixmap(logo_path)
        logo_label.setPixmap(pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(logo_label, alignment=Qt.AlignCenter)
        layout.addSpacing(20)
        
        # Estilo para o Label de Usuário
        usuario_label = QLabel("Usuário")
        usuario_label.setStyleSheet("font-size: 14px; color: #333333; font-weight: bold;")
        layout.addWidget(usuario_label)
        
        # Layout horizontal para adicionar ícone no campo de usuário
        usuario_layout = QHBoxLayout()
        usuario_icon = QLabel()
        usuario_icon.setPixmap(QPixmap(user_path).scaled(16, 16, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        usuario_layout.addWidget(usuario_icon)
        
        self.usuario_input = QLineEdit()
        self.usuario_input.setStyleSheet("""
            background-color: #ffffff;
            color: #333333;
            border: 1px solid #000000;
            border-radius: 10px;
            padding: 8px;
            font-size: 13px;
        """)
        usuario_layout.addWidget(self.usuario_input)
        layout.addLayout(usuario_layout)
        layout.addSpacing(10)
        
        # Estilo para o Label de Senha
        senha_label = QLabel("Senha")
        senha_label.setStyleSheet("font-size: 14px; color: #333333; font-weight: bold;")
        layout.addWidget(senha_label)
        
        # Layout horizontal para adicionar ícone no campo de senha
        senha_layout = QHBoxLayout()
        senha_icon = QLabel()
        senha_icon.setPixmap(QPixmap(password_path).scaled(16, 16, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        senha_layout.addWidget(senha_icon)
        
        self.senha_input = QLineEdit()
        self.senha_input.setEchoMode(QLineEdit.Password)  # Para esconder a senha
        self.senha_input.setStyleSheet("""
            background-color: #ffffff;
            color: #333333;
            border: 1px solid #000000;
            border-radius: 10px;
            padding: 8px;
            font-size: 13px;
        """)
        senha_layout.addWidget(self.senha_input)
        layout.addLayout(senha_layout)
        layout.addSpacing(20)
        
        # Layout para os botões
        botoes_layout = QHBoxLayout()
        
        # Botão de login - Melhorado com estilo mais arredondado
        login_btn = QPushButton("Entrar")
        login_btn.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #000000, stop:1 #333333);
                color: white;
                border: none;
                border-radius: 20px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            
            QPushButton:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #333333, stop:1 #555555);
            }
            
            QPushButton:pressed {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #555555, stop:1 #777777);
            }
        """)
        login_btn.setFixedHeight(40)
        login_btn.clicked.connect(self.validar_login)
        botoes_layout.addWidget(login_btn)
        
        # Botão de criar conta - Melhorado com estilo mais arredondado
        criar_conta_btn = QPushButton(" Criar Conta")
        criar_conta_btn.setIcon(QIcon(plus_path))
        criar_conta_btn.setIconSize(QSize(16, 16))
        criar_conta_btn.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #333333, stop:1 #555555);
                color: white;
                border: none;
                border-radius: 20px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            
            QPushButton:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #444444, stop:1 #666666);
            }
            
            QPushButton:pressed {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #222222, stop:1 #444444);
            }
        """)
        criar_conta_btn.setFixedHeight(40)
        criar_conta_btn.clicked.connect(self.mostrar_registro)
        botoes_layout.addWidget(criar_conta_btn)
        
        layout.addLayout(botoes_layout)
        
        # Status da aplicação
        status_label = QLabel("By: MathiasNormanton on GitHub")
        status_label.setStyleSheet("color: #888888; font-size: 11px;")
        layout.addWidget(status_label, alignment=Qt.AlignRight)
        layout.addSpacing(10)
        
        login_widget.setLayout(layout)
        return login_widget
    
    def create_register_page(self):
        register_widget = QWidget()
        layout = QVBoxLayout()
        
        # Barra superior com botão de fechar e voltar
        barra_superior = QHBoxLayout()
        
        # Botão voltar - Estilizado para ser mais arredondado
        voltar_btn = QPushButton("Voltar")
        voltar_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #333333;
                border: 1px solid #333333;
                border-radius: 15px;
                font-weight: bold;
                padding: 5px 15px;
            }
            
            QPushButton:hover {
                background-color: #f0f0f0;
            }
            
            QPushButton:pressed {
                background-color: #e0e0e0;
            }
        """)
        voltar_btn.clicked.connect(self.mostrar_login)
        barra_superior.addWidget(voltar_btn, alignment=Qt.AlignLeft)
        
        barra_superior.addStretch()
        
        # Botão X para fechar à direita
        fechar_btn = QPushButton()
        fechar_btn.setIcon(QIcon(close_path))
        fechar_btn.setIconSize(QSize(16, 16))
        fechar_btn.setStyleSheet("""
            background-color: transparent;
            border: none;
        """)
        fechar_btn.setFixedSize(24, 24)
        fechar_btn.clicked.connect(self.close)
        barra_superior.addWidget(fechar_btn, alignment=Qt.AlignRight)
        
        layout.addLayout(barra_superior)
        
        # Título
        titulo = QLabel("Criar Nova Conta")
        titulo.setStyleSheet("font-size: 18px; font-weight: bold; color: #333333; margin-bottom: 20px;")
        layout.addWidget(titulo, alignment=Qt.AlignCenter)
        layout.addSpacing(10)
        
        # Usuário
        usuario_label = QLabel("Usuário")
        usuario_label.setStyleSheet("font-size: 14px; color: #333333; font-weight: bold;")
        layout.addWidget(usuario_label)
        
        self.reg_usuario_input = QLineEdit()
        self.reg_usuario_input.setStyleSheet("""
            background-color: #ffffff;
            color: #333333;
            border: 1px solid #000000;
            border-radius: 10px;
            padding: 8px;
            font-size: 13px;
        """)
        layout.addWidget(self.reg_usuario_input)
        layout.addSpacing(10)
        
        # Senha
        senha_label = QLabel("Senha")
        senha_label.setStyleSheet("font-size: 14px; color: #333333; font-weight: bold;")
        layout.addWidget(senha_label)
        
        self.reg_senha_input = QLineEdit()
        self.reg_senha_input.setEchoMode(QLineEdit.Password)
        self.reg_senha_input.setStyleSheet("""
            background-color: #ffffff;
            color: #333333;
            border: 1px solid #000000;
            border-radius: 10px;
            padding: 8px;
            font-size: 13px;
        """)
        layout.addWidget(self.reg_senha_input)
        layout.addSpacing(10)
        
        # Confirmar Senha
        conf_senha_label = QLabel("Confirmar Senha")
        conf_senha_label.setStyleSheet("font-size: 14px; color: #333333; font-weight: bold;")
        layout.addWidget(conf_senha_label)
        
        self.conf_senha_input = QLineEdit()
        self.conf_senha_input.setEchoMode(QLineEdit.Password)
        self.conf_senha_input.setStyleSheet("""
            background-color: #ffffff;
            color: #333333;
            border: 1px solid #000000;
            border-radius: 10px;
            padding: 8px;
            font-size: 13px;
        """)
        layout.addWidget(self.conf_senha_input)
        layout.addSpacing(20)
        
        # Botão registrar - Melhorado com design mais arredondado
        registrar_btn = QPushButton("Registrar")
        registrar_btn.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #000000, stop:1 #333333);
                color: white;
                border: none;
                border-radius: 20px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            
            QPushButton:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #333333, stop:1 #555555);
            }
            
            QPushButton:pressed {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #555555, stop:1 #777777);
            }
        """)    
        registrar_btn.setFixedHeight(40)
        registrar_btn.clicked.connect(self.registrar_usuario)
        layout.addWidget(registrar_btn)
        
        register_widget.setLayout(layout)
        return register_widget
    
    def create_welcome_page(self):
        """Cria a página de boas-vindas após o login"""
        welcome_widget = QWidget()
        layout = QVBoxLayout()
        
        # Barra superior com botão de fechar
        barra_superior = QHBoxLayout()
        
        # Botão de logout - Design arredondado e atraente
        logout_btn = QPushButton("Logout")
        logout_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #333333;
                border: 1px solid #333333;
                border-radius: 15px;
                font-weight: bold;
                padding: 5px 15px;
            }
            
            QPushButton:hover {
                background-color: #f0f0f0;
            }
            
            QPushButton:pressed {
                background-color: #e0e0e0;
            }
        """)
        logout_btn.clicked.connect(self.mostrar_login)
        barra_superior.addWidget(logout_btn, alignment=Qt.AlignLeft)
        
        barra_superior.addStretch()
        
        # Botão X para fechar à direita
        fechar_btn = QPushButton()
        fechar_btn.setIcon(QIcon(close_path))
        fechar_btn.setIconSize(QSize(16, 16))
        fechar_btn.setStyleSheet("""
            background-color: transparent;
            border: none;
        """)
        fechar_btn.setFixedSize(24, 24)
        fechar_btn.clicked.connect(self.close)
        barra_superior.addWidget(fechar_btn, alignment=Qt.AlignRight)
        
        layout.addLayout(barra_superior)
        
        # Mensagem de boas-vindas
        welcome_label = QLabel("Página sem conteúdo.")
        welcome_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #333333;
        """)
        welcome_label.setAlignment(Qt.AlignCenter)
        
        # Adicionar a mensagem ao layout, centralizada verticalmente
        layout.addStretch(1)
        layout.addWidget(welcome_label)
        layout.addStretch(1)
        
        welcome_widget.setLayout(layout)
        return welcome_widget
    
    def mostrar_login(self):
        self.stacked_widget.setCurrentIndex(0)
    
    def mostrar_registro(self):
        self.stacked_widget.setCurrentIndex(1)
        
    def mostrar_welcome(self):
        self.stacked_widget.setCurrentIndex(2)
    
    def validar_login(self):
        usuario_input = self.usuario_input.text()
        senha_input = self.senha_input.text()

        if not usuario_input or not senha_input:
            QMessageBox.warning(self, "Atenção", "Por favor, preencha todos os campos.")
            return

        try:
            res = supabase.table("users").select("*").eq("usuario", usuario_input).eq("senha", senha_input).execute()

            # Verifica se o login foi bem-sucedido
            if res.data:
                # Em vez de exibir mensagem, vamos para a página de boas-vindas
                self.mostrar_welcome()
                # Limpar os campos
                self.usuario_input.clear()
                self.senha_input.clear()
            else:
                # Exibe erro se o login falhar
                QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")
        except Exception as e:
            # Exibe erro de conexão ou outro erro
            QMessageBox.critical(self, "Erro de Conexão", f"Ocorreu um erro ao conectar ao banco de dados: {str(e)}")
    
    def registrar_usuario(self):
        usuario = self.reg_usuario_input.text()
        senha = self.reg_senha_input.text()
        conf_senha = self.conf_senha_input.text()
        
        # Validações básicas
        if not usuario or not senha:
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios.")
            return
        
        if senha != conf_senha:
            QMessageBox.warning(self, "Erro", "As senhas não coincidem.")
            return
        
        try:
            # Verificar se o usuário já existe
            res = supabase.table("users").select("*").eq("usuario", usuario).execute()
            
            if res.data:
                QMessageBox.warning(self, "Erro", "Este nome de usuário já está em uso.")
                return
            
            # Inserir novo usuário
            data = {
                "usuario": usuario,
                "senha": senha
            }
            
            res = supabase.table("users").insert(data).execute()
            
            if res.data:
                QMessageBox.information(self, "Sucesso", "Conta criada com sucesso!")
                self.mostrar_login()  # Volta para a tela de login
                
                # Limpar os campos do formulário
                self.reg_usuario_input.clear()
                self.reg_senha_input.clear()
                self.conf_senha_input.clear()
            else:
                QMessageBox.warning(self, "Erro", "Não foi possível criar a conta.")
                
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro ao registrar: {str(e)}")

# Iniciar aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec_())
