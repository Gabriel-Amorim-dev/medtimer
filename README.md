# MedTimer 💊

O **MedTimer** é uma aplicação desenvolvida em Django para auxiliar no controle e agendamento de medicamentos, doses e tratamentos.

## 🚀 Como configurar o projeto localmente

Siga os passos abaixo para preparar o ambiente de desenvolvimento em sua máquina.

### Pré-requisitos

Certifique-se de ter instalado em seu computador:
- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

---

### 1. Clonar o Repositório

Abra o terminal e execute o comando:
```bash
git clone [https://github.com/Gabriel-Amorim-dev/medtimer.git](https://github.com/Gabriel-Amorim-dev/medtimer.git)
cd medtimer

```

### 2. Criar um Ambiente Virtual (venv)

É recomendável usar um ambiente virtual para isolar as dependências do projeto:

**No Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate

```

**No Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate

```

### 3. Instalar Dependências

Com o ambiente virtual ativo, instale os pacotes necessários:

```bash
pip install -r requirements.txt

```

### 4. Configurar Variáveis de Ambiente

O projeto utiliza um arquivo `.env` para configurações sensíveis.

1. Copie o arquivo de exemplo:
```bash
cp .env.example .env

```


2. Abra o arquivo `.env` e preencha as informações necessárias (como `SECRET_KEY`, `DEBUG`, etc).

### 5. Configurar o Banco de Dados

Execute as migrações para criar as tabelas no banco de dados SQLite (padrão):

```bash
python manage.py migrate

```

### 6. Criar um Superusuário (Opcional)

Para acessar o painel administrativo do Django:

```bash
python manage.py createsuperuser

```

### 7. Rodar o Servidor

Agora você pode iniciar o servidor de desenvolvimento:

```bash
python manage.py runserver

```

Acesse em seu navegador: `http://127.0.0.1:8000/`

---

## 📂 Estrutura do Projeto

* `core/`: Configurações principais do projeto Django.
* `medications/`: Gerenciamento de medicamentos.
* `treatments/`: Gestão de tratamentos médicos.
* `doses/`: Controle de dosagens.
* `notifications/`: Lógica de alertas e avisos.
* `users/`: Gestão de usuários e autenticação.

---

## 🤝 Colaboradores

Sinta-se à vontade para abrir *Issues* ou enviar *Pull Requests*. Antes de subir qualquer alteração, verifique se o servidor inicia corretamente.

---

Desenvolvido por [Gabriel Amorim](https://www.google.com/search?q=https://github.com/Gabriel-Amorim-dev)

