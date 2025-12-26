# 🚀 FastAPI Zero

> **Backend moderno em FastAPI** — Base escalável para APIs robustas, pronto para evoluir com CRUD e muito mais.

<div align="center">

[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=for-the-badge)](https://github.com/Pedrofeliixx/fastapi_zero)
[![Python](https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Poetry](https://img.shields.io/badge/Poetry-managed-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)](https://python-poetry.org/)

[🔗 Demo](https://github.com/Pedrofeliixx/fastapi_zero) • [📖 Docs](#documentação) • [🐳 Docker](#executar-com-docker) • [🤝 Contribuir](#como-contribuir)

</div>

---

## 📚 Índice

<table class="data-table">
  <thead>
    <tr>
      <th scope="col">🎯 Essencial</th>
      <th scope="col">⚙️ Configuração</th>
      <th scope="col">🛠️ Desenvolvimento</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        • <a href="#-visão-geral">Visão Geral</a><br>
        • <a href="#-funcionalidades">Funcionalidades</a><br>
        • <a href="#-stack--ferramentas">Stack & Ferramentas</a>
      </td>
      <td>
        • <a href="#-pré-requisitos">Pré-requisitos</a><br>
        • <a href="#-instalação-rápida">Instalação Rápida</a><br>
        • <a href="#-executar-localmente">Executar Localmente</a><br>
        • <a href="#-executar-com-docker">Docker Setup</a>
      </td>
      <td>
        • <a href="#-testes--linting">Testes & Linting</a><br>
        • <a href="#-estrutura-do-projeto">Estrutura do Projeto</a><br>
        • <a href="#-como-contribuir">Como Contribuir</a><br>
        • <a href="#-roadmap">Roadmap</a>
      </td>
    </tr>
  </tbody>
</table>

---

## 🎯 Visão Geral

**FastAPI Zero** é um backend moderno construído com FastAPI, projetado para ser uma **base sólida e escalável** para desenvolvimento de APIs. 

### 🌟 Por que escolher este projeto?

- ⚡ **Performance**: FastAPI é uma das frameworks Python mais rápidas
- 🔄 **Desenvolvimento Ágil**: Hot reload e documentação automática
- 🧪 **Testável**: Estrutura preparada para testes desde o início
- 📦 **Containerizado**: Ready-to-deploy com Docker
- 🏗️ **Escalável**: Arquitetura pensada para crescer

> 🔥 **Status atual**: Estrutura base completa com endpoints iniciais e testes. O próximo grande marco é a **implementação completa de CRUD** e integração com banco de dados.

---

## ✨ Funcionalidades

### 🎯 Disponível Agora
- ✅ **Endpoint raiz** (`GET /`) com resposta de status
- ✅ **Documentação automática** via Swagger UI (`/docs`) e Redoc (`/redoc`)
- ✅ **Estrutura de testes** com pytest configurado
- ✅ **Containerização** com Docker pronta
- ✅ **Linting e formatação** com Ruff

### 🔜 Em Desenvolvimento
- 🔄 CRUD completo para recursos principais
- 🔄 Integração com banco de dados
- 🔄 Sistema de autenticação/autorização
- 🔄 Middleware de logging e monitoramento

---

## 🛠️ Stack & Ferramentas

<div align="center">

### Core Technologies
| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| **Python** | 3.13+ | Linguagem principal |
| **FastAPI** | Latest | Framework web moderno |
| **Uvicorn** | Latest | Servidor ASGI |

### Development Tools
| Ferramenta | Uso |
|------------|-----|
| **Poetry** | Gerenciamento de dependências |
| **pytest** | Framework de testes |
| **Ruff** | Linting e formatação |
| **Docker** | Containerização |

</div>

---

## 📋 Pré-requisitos

> ⚠️ **Importante**: Certifique-se de ter todas as dependências instaladas antes de prosseguir.

### 🔧 Ferramentas Necessárias

| Ferramenta | Versão | Status | Instalação |
|------------|--------|--------|------------|
| **Git** | Latest | ✅ Obrigatório | [Download](https://git-scm.com/) |
| **Python** | 3.11+ | ✅ Obrigatório | [Download](https://www.python.org/) |
| **Docker** | Latest | 🔶 Opcional | [Download](https://www.docker.com/) |

### 🐍 Setup do Python

**1. Instalar pipx** (recomendado para isolamento de ferramentas):
```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

**2. Instalar Poetry via pipx**:
```bash
pipx install poetry
```

**3. Verificar instalação**:
```bash
poetry --version
```

---

##  💻 Instalação Rápida

### 📥 Clone e Setup

```bash
# 1. Clone o repositório
git clone https://github.com/Pedrofeliixx/fastapi_zero.git
cd fastapi_zero

# 2. Instale dependências com Poetry
poetry install

# 3. Ative o ambiente virtual (opcional)
poetry shell
```

### 🔄 Alternativa com pip

Se preferir usar pip tradicional:

```bash
# 1. Criar ambiente virtual
python -m venv .venv

# 2. Ativar ambiente
# Linux/Mac:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# 3. Instalar dependências
pip install -U pip
poetry export -f requirements.txt --output requirements.txt --without-hashes
pip install -r requirements.txt
```

---

## 🏃‍♂️ Executar Localmente

### 🔥 Modo Desenvolvimento (com hot reload)

```bash
# Usando Poetry
poetry run uvicorn fastapi_zero.app:app --reload --host 0.0.0.0 --port 8000

# Ou dentro do shell Poetry
poetry shell
uvicorn fastapi_zero.app:app --reload --host 0.0.0.0 --port 8000
```

### 🌐 Acessar a Aplicação

<div align="center">

| Recurso | URL | Descrição |
|---------|-----|-----------|
| **API Principal** | [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) | Endpoint raiz da API |
| **Swagger UI** | [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) | Documentação interativa |
| **ReDoc** | [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc) | Documentação alternativa |

</div>

> 💡 **Dica**: O `--reload` observa mudanças no código e reinicia automaticamente o servidor.

---

## 🐳 Executar com Docker

### 📝 Dockerfile

Crie este `Dockerfile` na raiz do projeto:

```dockerfile
# Multi-stage build para otimização
FROM python:3.13-slim as builder

WORKDIR /app

# Instalar Poetry
RUN pip install --no-cache-dir poetry

# Configurar Poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VENV_IN_PROJECT=1 \
    POETRY_CACHE_DIR=/opt/poetry_cache

# Copiar arquivos de dependência
COPY pyproject.toml poetry.lock* ./

# Instalar dependências
RUN poetry install --only=main && rm -rf $POETRY_CACHE_DIR

# Stage de produção
FROM python:3.13-slim as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Copiar ambiente virtual
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

# Copiar código da aplicação
COPY fastapi_zero ./fastapi_zero

# Expor porta
EXPOSE 8000

# Comando padrão
CMD ["uvicorn", "fastapi_zero.app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 🏗️ Build & Run

```bash
# Build da imagem
docker build -t fastapi-zero .

# Executar container
docker run -d -p 8000:8000 --name fastapi-zero-container fastapi-zero
```

### 🐙 Docker Compose

Crie um `docker-compose.yml`:

```yaml
version: "3.8"

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - PYTHONUNBUFFERED=1
      - ENVIRONMENT=development
    volumes:
      - .:/app
    command: uvicorn fastapi_zero.app:app --host 0.0.0.0 --port 8000 --reload
    restart: unless-stopped

  # Placeholder para banco de dados futuro
  # db:
  #   image: postgres:15
  #   environment:
  #     POSTGRES_DB: fastapi_zero
  #     POSTGRES_USER: user
  #     POSTGRES_PASSWORD: password
  #   ports:
  #     - "5432:5432"
```

**Executar com Docker Compose**:
```bash
# Subir serviços
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar serviços
docker-compose down
```

---

## 🧪 Testes & Linting

### ✅ Executar Testes

```bash
# Testes simples
poetry run pytest

# Testes com mais detalhes
poetry run pytest -v

# Testes com coverage
poetry run pytest --cov=fastapi_zero

# Testes em modo watch (desenvolvimento)
poetry run pytest --watch
```

### 🎯 Linting e Formatação

```bash
# Verificar código
poetry run ruff check .

# Aplicar formatação automática
poetry run ruff format .

# Checar e fixar problemas
poetry run ruff check . --fix
```

### 🔄 Scripts Automatizados

Adicione no `pyproject.toml`:
```toml
[tool.poetry.scripts]
test = "pytest"
lint = "ruff check ."
format = "ruff format ."
dev = "uvicorn fastapi_zero.app:app --reload"
```

Então execute:
```bash
poetry run test
poetry run lint
poetry run format
poetry run dev
```

---

## 📁 Estrutura do Projeto

```
fastapi_zero/
├── 📁 fastapi_zero/           # 📦 Pacote principal da aplicação
│   ├── 📄 __init__.py         # Inicializador do pacote
│   ├── 🚀 app.py              # Instância FastAPI e rotas principais
│   ├── 📁 routers/            # 🛣️ Módulos de rotas (futuro)
│   ├── 📁 models/             # 🗄️ Modelos de dados (futuro)
│   ├── 📁 services/           # ⚙️ Lógica de negócios (futuro)
│   └── 📁 utils/              # ⚙️ Utilitários e helpers (futuro)
├── 📁 tests/                  # 🧪 Testes da aplicação
│   ├── 📄 __init__.py
│   ├── 🧪 test_app.py         # Testes da aplicação principal
│   └── 📁 unit/               # Testes unitários (futuro)
├── 📁 docker/                 # 🐳 Arquivos Docker (futuro)
├── 📄 pyproject.toml          # ⚙️ Configurações Poetry/Python
├── 📄 poetry.lock             # 🔒 Lock de dependências
├── 📄 Dockerfile             # 🐳 Containerização
├── 📄 docker-compose.yml     # 🐙 Orquestração de containers
├── 📄 .gitignore             # 👁️‍🗨️ Arquivos ignorados pelo Git
├── 📄 .env.example           # 🔐 Exemplo de variáveis de ambiente
└── 📄 README.md              # 📖 Documentação principal
```

### 🎯 Convenções de Código

> 📋 **Padrões adotados**:
> - **Nomenclatura**: `snake_case` para arquivos e funções
> - **Imports**: Ordenados alfabeticamente e por categoria
> - **Docstrings**: Formato Google/Numpy
> - **Type hints**: Obrigatório em funções públicas

---

## 🤝 Como Contribuir

### 🚀 Processo de Contribuição

1. **📋 Discussão**: Abra uma [issue](https://github.com/Pedrofeliixx/fastapi_zero/issues) para discutir funcionalidades ou reportar bugs
2. **🍴 Fork**: Faça um fork do repositório
3. **🌿 Branch**: Crie uma branch descritiva
   ```bash
   git checkout -b feature/implementar-crud-users
   git checkout -b fix/corrigir-endpoint-root
   git checkout -b docs/atualizar-readme
   ```
4. **💻 Develop**: Implemente suas mudanças
5. **🧪 Test**: Execute testes e linting
6. **📤 PR**: Crie um Pull Request detalhado

### ✅ Checklist para Pull Request

<table class="data-table">
  <thead>
    <tr>
      <th scope="col">Categoria</th>
      <th scope="col">Requisitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>🧪 Testes</strong></td>
      <td>
        ☐ Testes passando (<code>poetry run pytest</code>)<br>
        ☐ Coverage mantido ou melhorado<br>
        ☐ Testes para novas funcionalidades
      </td>
    </tr>
    <tr>
      <td><strong>🎯 Qualidade</strong></td>
      <td>
        ☐ Linting passando (<code>poetry run ruff check .</code>)<br>
        ☐ Formatação aplicada (<code>poetry run ruff format .</code>)<br>
        ☐ Type hints onde apropriado
      </td>
    </tr>
    <tr>
      <td><strong>📖 Documentação</strong></td>
      <td>
        ☐ README atualizado se necessário<br>
        ☐ Docstrings para funções públicas<br>
        ☐ Comentários em código complexo
      </td>
    </tr>
  </tbody>
</table>

### 🏷️ Padrão de Commits

Use [Conventional Commits](https://www.conventionalcommits.org/):

```bash
feat: adicionar endpoint de CRUD para usuários
fix: corrigir validação de email no registro
docs: atualizar README com exemplos de uso
test: adicionar testes para autenticação
refactor: reorganizar estrutura de modelos
```

---

## 🗺️ Roadmap

### 🎯 Fase 1: Foundation (Concluída ✅)
- ✅ Estrutura inicial da API
- ✅ Documentação automática
- ✅ Testes básicos
- ✅ Containerização Docker
- ✅ Pipeline de linting

### 🔥 Fase 2: Core Features (Em Andamento 🔄)
- 🔄 **CRUD completo** para recursos principais
- 🔄 **Integração com banco** (PostgreSQL + SQLModel/Asyncpg)
- 🔄 **Migrations** com Alembic
- 🔄 **Validações** avançadas com Pydantic V2

### 🚀 Fase 3: Production Ready (Planejado 📋)
- 📋 **Autenticação/Autorização** (JWT + OAuth2)
- 📋 **Middleware** de logging e monitoramento
- 📋 **Rate limiting** e throttling
- 📋 **Cache** com Redis
- 📋 **Background tasks** com Celery

### 🏗️ Fase 4: DevOps & Scale (Futuro 🔮)
- 🔮 **CI/CD** completo (GitHub Actions)
- 🔮 **Health checks** e métricas
- 🔮 **Deploy automatizado** (AWS/GCP/Azure)
- 🔮 **Monitoring** com Prometheus/Grafana
- 🔮 **Documentação** estendida

### 📊 Progresso Atual

```
Foundation     ████████████████████████████████ 100%
Core Features  ████████░░░░░░░░░░░░░░░░░░░░░░░░ 25%
Production     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0%
DevOps         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0%
```

---

## 📄 Licença

Este projeto está sob discussão para definição de licença.

**Opções consideradas**:
- 📋 **MIT License** - Máxima flexibilidade
- 📋 **Apache 2.0** - Proteção contra patentes
- 📋 **GPL v3** - Copyleft forte

> 💬 **Feedback welcome**: Abra uma issue para discutir qual licença seria mais adequada para o projeto.

---

## 📞 Contato & Suporte

<div align="center">

### 👨‍💻 Desenvolvedor Principal
**Pedro Felix**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Pedrofeliixx)
[![Repository](https://img.shields.io/badge/Repository-FastAPI_Zero-blue?style=for-the-badge&logo=fastapi)](https://github.com/Pedrofeliixx/fastapi_zero)


### 💬 Como entrar em contato

| Tipo | Canal | Quando Usar |
|------|-------|-------------|
| 🐛 **Bug Reports** | [Issues](https://github.com/Pedrofeliixx/fastapi_zero/issues) | Problemas e erros |
| ✨ **Feature Requests** | [Issues](https://github.com/Pedrofeliixx/fastapi_zero/issues) | Novas funcionalidades |
| 🤝 **Contribuições** | [Pull Requests](https://github.com/Pedrofeliixx/fastapi_zero/pulls) | Código e melhorias |
| ❓ **Dúvidas Gerais** | [Discussions](https://github.com/Pedrofeliixx/fastapi_zero/discussions) | Perguntas e discussões |

</div>

---

<div align="center">

### 🌟 Se este projeto te ajudou, considere dar uma estrela!

[![GitHub stars](https://img.shields.io/github/stars/Pedrofeliixx/fastapi_zero?style=social)](https://github.com/Pedrofeliixx/fastapi_zero)


</div>
