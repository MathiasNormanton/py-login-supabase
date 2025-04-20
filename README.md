
# py-login-supabase 
![Imagem da logo padrão do aplicativo](https://cdn-icons-png.flaticon.com/128/15708/15708987.png)


## Description / Descrição

### English
A modern login application built with PyQt5 for the front-end and Supabase for the back-end. This application features a minimalistic and user-friendly design with a secure user registration and login system. The user data is stored securely in Supabase, providing an easy-to-use solution for authentication.

- **Modern and responsive interface**: Clean design that adjusts to different screen sizes.
- **User login and registration system**: Allows users to sign up and log in with a secure process.
- **Secure data storage**: Utilizes Supabase for handling user credentials safely.
- **Minimalist and user-friendly design**: Focuses on simplicity and ease of use.

### Português
Uma aplicação de login moderna construída com PyQt5 para o front-end e Supabase para o back-end. Esta aplicação apresenta um design minimalista e amigável ao usuário, com um sistema seguro de registro e login de usuários. Os dados dos usuários são armazenados de forma segura no Supabase, oferecendo uma solução prática para autenticação.

- **Interface moderna e responsiva**: Design limpo que se ajusta a diferentes tamanhos de tela.
- **Sistema de login e registro de usuários**: Permite que os usuários se registrem e façam login com um processo seguro.
- **Armazenamento seguro de dados**: Utiliza o Supabase para gerenciar credenciais de usuários de forma segura.
- **Design minimalista e amigável**: Foco na simplicidade e facilidade de uso.

## Requirements / Requisitos

- Python 3.x
- PyQt5
- requests
- supabase-py (Python library for interacting with Supabase)

## Installation / Instalação

### English
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/MathiasNormanton/py-login-supabase.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Replace the placeholders for your Supabase URL and API key in the code.

4. Run the application:
   ```bash
   python main.py
   ```

### Português
1. Clone este repositório para a sua máquina local:
   ```bash
   git clone https://github.com/MathiasNormanton/py-login-supabase.git
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

3. Substitua os espaços reservados para a URL do Supabase e a chave de API no código.

4. Execute a aplicação:
   ```bash
   python main.py
   ```

## Code Overview / Visão Geral do Código

The core of the application consists of three main parts:
- **Login Page**: A simple page where users can enter their credentials to log in.
- **Registration Page**: Allows new users to create an account.
- **Welcome Page**: Displays a welcome message after the user logs in successfully.

The application uses the Supabase client to handle user authentication and stores user data securely in the Supabase database.

Here are some key parts of the code:

1. **Supabase Configuration**:
   ```python
   url = "your_supabase_url"
   key = "your_supabase_anon_key"
   supabase = supabase.create_client(url, key)
   ```

2. **Icon Downloading Function**:
   Downloads and stores icons for the interface.
   ```python
   def download_icon(url, filename):
       if not os.path.exists("icons"):
           os.makedirs("icons")
       ...
   ```

3. **Login Page**:
   A page with fields for username and password, along with login and registration buttons.
   ```python
   def create_login_page(self):
       ...
       login_btn.clicked.connect(self.validar_login)
       criar_conta_btn.clicked.connect(self.mostrar_registro)
       ...
   ```

4. **Registration Page**:
   Allows users to register with a username and password.
   ```python
   def create_register_page(self):
       ...
       registrar_btn.clicked.connect(self.registrar_usuario)
       voltar_btn.clicked.connect(self.mostrar_login)
       ...
   ```

## License / Licença

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
