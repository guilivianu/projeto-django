# AutoFix - Sistema de Gestão de Oficinas (ECAA09 Parte 2)

Segunda parte do projeto Django para a disciplina ECAA09. O sistema conecta clientes com problemas mecânicos a oficinas especializadas.

## 📋 Funcionalidades Implementadas

- [x] **Cadastro Personalizado**: Registro de usuários com distinção entre "Cliente" e "Oficina".
- [x] **Cadastro de Problemas**: Clientes podem registrar problemas com descrição e **upload de imagem**.
- [x] **Dashboard do Cliente**:
  - Listagem de problemas cadastrados.
  - Visualização do status e da oficina interessada.
- [x] **Dashboard da Oficina**:
  - Visualização de problemas em aberto (com fotos).
  - Seleção de problemas para atendimento.
  - Gestão de serviços em andamento.

## 🚀 Como Rodar o Projeto

### Pré-requisitos

- Python 3.x
- Virtualenv (recomendado)

### Instalação

1. **Clone o repositório** (se aplicável) ou baixe os arquivos.

2. **Crie e ative o ambiente virtual**:

   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

   _Nota: Isso instalará o Django, Gunicorn e Pillow (necessário para imagens)._

4. **Configure o Banco de Dados**:

   ```bash
   # Criar migrações do app core
   python manage.py makemigrations core

   # Aplicar migrações
   python manage.py migrate
   ```

5. **Crie um Superusuário**:

   ```bash
   python manage.py createsuperuser
   ```

6. **(Opcional) Popule o Banco de Dados**:

   O projeto conta com um script para criar dados fictícios de teste.

   ```bash
   python manage.py popular_banco
   ```

7. **Inicie o Servidor**:

   ```bash
   python manage.py runserver
   ```

   Acesse em: `http://127.0.0.1:8000/`

## 🛠️ Tecnologias Utilizadas

- **Django 5**: Framework web principal.
- **Bootstrap 5**: Estilização das páginas.
- **SQLite**: Banco de dados padrão.
- **Pillow**: Manipulação de imagens.
