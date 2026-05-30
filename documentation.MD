# 💊 MedTimer — Documentação do Projeto

> Aplicação Django para controle e agendamento de medicamentos, doses e tratamentos médicos.

---

## Índice

1. [Visão Geral](#visão-geral)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Arquitetura e Estrutura de Pastas](#arquitetura-e-estrutura-de-pastas)
4. [Configuração do Ambiente](#configuração-do-ambiente)
5. [Variáveis de Ambiente](#variáveis-de-ambiente)
6. [Banco de Dados](#banco-de-dados)
7. [Módulos da Aplicação](#módulos-da-aplicação)
8. [Filas e Tarefas Assíncronas (Celery)](#filas-e-tarefas-assíncronas-celery)
9. [Executando o Projeto](#executando-o-projeto)
10. [Painel Administrativo](#painel-administrativo)
11. [Contribuindo com o Projeto](#contribuindo-com-o-projeto)

---

## Visão Geral

O **MedTimer** é uma aplicação web desenvolvida com o framework **Django** que tem como objetivo auxiliar pacientes e cuidadores no controle de medicamentos, tratamentos médicos e doses. A aplicação oferece funcionalidades de agendamento com notificações, gerenciamento de usuários e um painel completo para administração.

**Principais funcionalidades:**

- Cadastro e gerenciamento de medicamentos
- Criação e acompanhamento de tratamentos médicos
- Controle de dosagens por horário
- Sistema de notificações e alertas
- Gestão de usuários com autenticação

---

## Tecnologias Utilizadas

| Tecnologia | Versão | Finalidade |
|---|---|---|
| Python | 3.10+ | Linguagem principal |
| Django | 6.0.4 | Framework web |
| PostgreSQL | — | Banco de dados relacional |
| psycopg2-binary | 2.9.12 | Driver Python para PostgreSQL |
| python-dotenv | 1.2.2 | Gerenciamento de variáveis de ambiente |


---

## Arquitetura e Estrutura de Pastas

```
medtimer/
├── core/               # Configurações principais do projeto Django
├── medications/        # Módulo de gerenciamento de medicamentos
├── treatments/         # Módulo de gestão de tratamentos médicos
├── doses/              # Módulo de controle de dosagens
├── notifications/      # Módulo de alertas e notificações
├── users/              # Módulo de usuários e autenticação
├── templates/          # Templates HTML globais
├── manage.py           # Utilitário de linha de comando do Django
├── requirements.txt    # Dependências do projeto
├── .env.example        # Exemplo de configuração de variáveis de ambiente
└── .gitignore          # Arquivos ignorados pelo Git
```

### Descrição dos módulos

**`core/`** — Configurações centrais do Django: `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`. É o ponto de entrada e orquestração de toda a aplicação.

**`medications/`** — Responsável pelo cadastro, listagem, edição e remoção de medicamentos. Contém models, views, URLs e formulários relacionados aos remédios cadastrados pelos usuários.

**`treatments/`** — Gerencia os tratamentos médicos vinculados a um usuário. Um tratamento pode agrupar múltiplos medicamentos e doses ao longo de um período específico.

**`doses/`** — Controla as dosagens de cada medicamento dentro de um tratamento, incluindo quantidade, frequência e horários de administração.

**`notifications/`** — Lógica de envio de alertas e lembretes ao usuário, possivelmente integrada ao Celery para agendamento assíncrono de notificações nos horários corretos.

**`users/`** — Gerenciamento de contas de usuário, registro, login, logout e perfil. Também controla permissões de acesso às funcionalidades da plataforma.

**`templates/`** — Templates HTML base e parciais reutilizados por todos os módulos da aplicação.

---

## Configuração do Ambiente

Siga os passos abaixo para preparar o ambiente de desenvolvimento local.

### Pré-requisitos

Certifique-se de ter instalado em sua máquina:

- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [PostgreSQL](https://www.postgresql.org/download/)

### Passo 1 — Clonar o repositório

```bash
git clone https://github.com/Gabriel-Amorim-dev/medtimer.git
cd medtimer
```

### Passo 2 — Criar e ativar um ambiente virtual

É fortemente recomendado usar um ambiente virtual para isolar as dependências do projeto.

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Passo 3 — Instalar as dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

---

## Variáveis de Ambiente

O projeto utiliza um arquivo `.env` para armazenar configurações sensíveis. Nunca versione esse arquivo no Git.

### Configuração inicial

Copie o arquivo de exemplo e preencha com suas configurações:

```bash
cp .env.example .env
```

### Descrição das variáveis

| Variável | Descrição | Exemplo |
|---|---|---|
| `SECRET_KEY` | Chave secreta do Django. Gere uma exclusiva para seu ambiente. | `django-insecure-...` |
| `DEBUG` | Modo debug. Use `True` em desenvolvimento e `False` em produção. | `True` |
| `DB_NAME` | Nome do banco de dados PostgreSQL | `medtime_db` |
| `DB_USER` | Usuário do PostgreSQL | `postgres` |
| `DB_PASSWORD` | Senha do banco de dados | `sua_senha` |
| `DB_HOST` | Endereço do servidor do banco de dados | `localhost` |
| `DB_PORT` | Porta do PostgreSQL | `5432` |
| `LOGIN_URL` | URL da página de login | `/login/` |
| `LOGIN_REDIRECT_URL` | Redireciona para essa URL após login bem-sucedido | `/perfil/` |
| `LOGOUT_REDIRECT_URL` | Redireciona para essa URL após logout | `/login/` |

### Gerando uma SECRET_KEY segura

Execute o seguinte comando Python para gerar uma chave aleatória:

```bash
python -c "from django.utils.crypto import get_random_string; print(get_random_string(50))"
```

Cole o resultado gerado no campo `SECRET_KEY` do seu `.env`.

---

## Banco de Dados

O MedTimer utiliza **PostgreSQL** como banco de dados principal.

### Criar o banco de dados

Acesse o terminal do PostgreSQL e execute:

```sql
CREATE DATABASE medtime_db;
```

> Certifique-se de que o usuário e a senha definidos no `.env` tenham permissão de acesso a esse banco.

### Aplicar as migrações

Com o `.env` configurado, execute as migrações para criar as tabelas:

```bash
python manage.py migrate
```

Para criar novas migrações após alterar um model:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Módulos da Aplicação

### Medicamentos (`medications`)

Gerencia os medicamentos cadastrados na plataforma. Cada medicamento possui atributos como nome, descrição, fabricante e outras informações relevantes para o controle do tratamento.

**Operações principais:** criar, listar, editar e remover medicamentos.

### Tratamentos (`treatments`)

Um tratamento representa um ciclo terapêutico de um usuário — podendo ter data de início, data de término e um conjunto de medicamentos associados.

**Operações principais:** criar e acompanhar tratamentos vinculados ao perfil do usuário.

### Doses (`doses`)

Controla quando e como cada medicamento deve ser tomado dentro de um tratamento: quantidade por dose, intervalo entre doses e horários específicos.

**Operações principais:** definir e editar o esquema posológico de cada medicamento em um tratamento.

### Notificações (`notifications`)

Responsável por alertar os usuários nos horários corretos para que tomem seus medicamentos. Integra-se ao Celery e Redis para agendamento assíncrono de lembretes.

**Operações principais:** disparar notificações nos horários configurados para cada dose.

### Usuários (`users`)

Gerencia o ciclo de vida das contas: cadastro, autenticação, perfil e permissões de acesso às funcionalidades da aplicação.

**Operações principais:** registro, login, logout e edição de perfil.

---


---

## Executando o Projeto

Com todas as configurações realizadas, inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

Acesse a aplicação em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Checklist rápido antes de subir o servidor

- [ ] Ambiente virtual ativado
- [ ] Arquivo `.env` configurado
- [ ] Banco de dados PostgreSQL em execução
- [ ] Migrações aplicadas (`python manage.py migrate`)
- [ ] Redis em execução (se for usar notificações)
- [ ] Workers do Celery iniciados (se for usar notificações)

---

## Painel Administrativo

O Django oferece um painel administrativo nativo para gerenciar os dados da aplicação diretamente pelo navegador.

### Criar um superusuário

```bash
python manage.py createsuperuser
```

Siga as instruções no terminal para definir nome de usuário, e-mail e senha.

### Acessar o painel

Com o servidor em execução, acesse:

```
http://127.0.0.1:8000/admin/
```

---

## Contribuindo com o Projeto

Contribuições são bem-vindas! Siga as orientações abaixo antes de enviar alterações:

1. Faça um fork do repositório
2. Crie uma branch para sua funcionalidade: `git checkout -b feature/minha-feature`
3. Faça suas alterações e certifique-se de que o servidor inicia corretamente
4. Faça o commit: `git commit -m "feat: descrição da funcionalidade"`
5. Envie para o seu fork: `git push origin feature/minha-feature`
6. Abra um **Pull Request** no repositório original

> Antes de subir qualquer alteração, verifique se o servidor inicia corretamente com `python manage.py runserver`.

---

Desenvolvido por [Gabriel Amorim](https://github.com/Gabriel-Amorim-dev)
