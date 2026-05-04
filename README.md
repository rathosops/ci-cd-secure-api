# CI/CD Secure API

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-black)
![Security](https://img.shields.io/badge/Security-DevSecOps-red)

API simples em Python criada para demonstrar um fluxo profissional de **CI/CD com qualidade, testes, Docker e segurança automatizada**.

O objetivo deste projeto não é construir uma API complexa. O objetivo é criar um projeto de portfólio bem organizado, fácil de explicar em entrevistas e com práticas reais de DevOps e DevSecOps.

---

## Objetivo do projeto

Este projeto foi criado para demonstrar que é possível construir uma aplicação pequena, mas com uma base profissional.

Ele cobre:

- criação de uma API em Python;
- organização de projeto com layout `src/`;
- testes automatizados com `pytest`;
- análise de qualidade com `ruff`;
- checagem opcional de tipos com `mypy`;
- empacotamento e execução com Docker;
- pipeline de CI com GitHub Actions;
- pipeline de CD com build, scan e publicação de imagem;
- análise de segurança com Bandit, Semgrep, Gitleaks, Trivy e pip-audit;
- automação local com Makefile;
- hooks locais com pre-commit;
- atualização automatizada de dependências com Dependabot.

A frase principal para explicar este projeto em uma entrevista é:

> Eu construí uma API simples em Python e implementei um pipeline CI/CD com testes, qualidade de código, análise de segurança, scan de dependências, scan de secrets, build Docker e publicação de imagem.

---

## Stack utilizada

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn
- Docker
- GitHub Actions
- pytest
- pytest-cov
- ruff
- mypy
- Bandit
- Semgrep
- Gitleaks
- Trivy
- pip-audit
- pre-commit
- Dependabot
- GitHub Container Registry

---

## Estrutura do projeto

```text
ci-cd-secure-api/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── cd.yml
│   └── dependabot.yml
├── src/
│   └── secure_api/
│       ├── __init__.py
│       ├── main.py
│       ├── api/
│       │   ├── __init__.py
│       │   └── routes.py
│       ├── core/
│       │   ├── __init__.py
│       │   └── config.py
│       └── schemas/
│           ├── __init__.py
│           ├── health.py
│           └── version.py
├── tests/
│   ├── __init__.py
│   └── test_health.py
├── .dockerignore
├── .gitignore
├── .pre-commit-config.yml
├── Dockerfile
├── Makefile
├── pyproject.toml
├── README.md
└── requirements-dev.txt
```

---

## Explicação da estrutura

### `.github/`

Contém arquivos relacionados à automação do GitHub.

#### `.github/workflows/ci.yml`

Pipeline de CI executado em pull requests para a branch `main`.

Ele valida se o código está pronto para entrar na branch principal.

Principais etapas:

- checkout do repositório;
- instalação do Python;
- instalação das dependências;
- lint com ruff;
- verificação de formatação;
- checagem de tipos com mypy;
- testes com pytest;
- relatório de cobertura;
- análise de segurança com Bandit;
- auditoria de dependências com pip-audit;
- SAST com Semgrep;
- detecção de secrets com Gitleaks.

#### `.github/workflows/cd.yml`

Pipeline de CD executado em push para a branch `main`.

Ele transforma o código aprovado em uma imagem Docker publicável.

Principais etapas:

- checkout do repositório;
- configuração do Docker Buildx;
- login no GitHub Container Registry;
- build da imagem Docker;
- scan da imagem com Trivy;
- upload do relatório SARIF;
- publicação da imagem no registry.

#### `.github/dependabot.yml`

Configura o Dependabot para verificar atualizações de:

- dependências Python;
- imagem Docker base;
- GitHub Actions.

Isso ajuda a manter o projeto atualizado e reduz riscos de vulnerabilidades conhecidas.

---

### `src/`

Contém o código-fonte da aplicação.

O projeto usa o layout `src/` porque ele evita imports acidentais durante os testes e deixa mais claro o que é código de produção e o que é código auxiliar.

---

### `src/secure_api/`

Pacote principal da aplicação.

#### `__init__.py`

Define informações básicas do pacote, como a versão da aplicação.

Exemplo:

```python
__version__ = "0.1.0"
```

#### `main.py`

Ponto de entrada da aplicação FastAPI.

Ele cria a aplicação por meio de uma função `create_app()`, o que facilita testes e evita efeitos colaterais desnecessários no momento do import.

Responsabilidades:

- criar a instância do FastAPI;
- configurar nome, versão e descrição;
- registrar as rotas da aplicação.

---

### `src/secure_api/api/`

Contém as rotas HTTP da API.

#### `routes.py`

Define os endpoints da aplicação.

Endpoints recomendados para este projeto:

- `GET /health`
- `GET /version`

O endpoint `/health` permite verificar se a aplicação está rodando.

O endpoint `/version` permite consultar o nome e a versão da aplicação, o que é útil em ambientes containerizados e pipelines de deploy.

---

### `src/secure_api/core/`

Contém configurações centrais da aplicação.

#### `config.py`

Define as configurações da aplicação em uma classe simples.

A proposta é manter a configuração pequena e clara no início do projeto.

Exemplo de responsabilidades:

- nome da aplicação;
- descrição da aplicação;
- status padrão do health check.

---

### `src/secure_api/schemas/`

Contém os modelos de entrada e saída da API.

Os schemas são definidos com Pydantic.

#### `health.py`

Define o modelo de resposta do endpoint `/health`.

Exemplo de resposta:

```json
{
  "status": "ok"
}
```

#### `version.py`

Define o modelo de resposta do endpoint `/version`.

Exemplo de resposta:

```json
{
  "name": "CI/CD Secure API",
  "version": "0.1.0"
}
```

---

### `tests/`

Contém os testes automatizados da aplicação.

#### `test_health.py`

Testa se o endpoint `/health` retorna:

- status HTTP 200;
- corpo JSON esperado.

Os testes são importantes porque o pipeline de CI deve bloquear alterações que quebrem o comportamento básico da API.

---

## Arquivos da raiz

### `.gitignore`

Define arquivos e diretórios que não devem ser versionados.

Exemplos:

- ambientes virtuais;
- cache do Python;
- arquivos de coverage;
- caches de ferramentas;
- arquivos `.env`;
- arquivos temporários do sistema operacional;
- arquivos de IDE.

---

### `.dockerignore`

Define arquivos que não devem ser enviados para o contexto de build Docker.

Isso ajuda a:

- reduzir o tamanho do contexto de build;
- evitar copiar arquivos desnecessários;
- evitar exposição acidental de arquivos locais;
- melhorar a performance do build.

---

### `.pre-commit-config.yml`

Configura hooks locais executados antes de commits.

Esse arquivo ajuda a detectar problemas antes de enviar código para o GitHub.

Ferramentas recomendadas:

- ruff;
- ruff-format;
- gitleaks.

Com isso, problemas de lint, formatação e secrets podem ser detectados antes do pull request.

---

### `Dockerfile`

Define como a imagem Docker da aplicação será construída.

Boas práticas aplicadas:

- uso de imagem base `python:3.12-slim`;
- variáveis para melhorar comportamento do Python em container;
- instalação apenas do necessário;
- usuário não-root;
- cópia seletiva de arquivos;
- exposição da porta 8000;
- execução com Uvicorn;
- healthcheck usando o endpoint `/health`.

---

### `Makefile`

Centraliza comandos comuns do projeto.

Isso evita memorizar vários comandos diferentes e torna o uso local mais simples.

Comandos recomendados:

```bash
make install
make run
make test
make lint
make format
make type-check
make security
make docker-build
make docker-run
make check
```

---

### `pyproject.toml`

Arquivo central de configuração do projeto Python.

Ele concentra:

- metadados do projeto;
- dependências principais;
- dependências de desenvolvimento;
- configuração do pytest;
- configuração do coverage;
- configuração do ruff;
- configuração do mypy;
- configuração do Bandit.

Centralizar essas configurações ajuda a manter o projeto mais limpo e reduz duplicação.

---

### `requirements-dev.txt`

Arquivo simples para instalação das dependências de desenvolvimento.

Conteúdo esperado:

```text
-e .[dev]
```

Isso instala o projeto em modo editável junto com as dependências extras de desenvolvimento.

---

## Como executar o projeto localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/rathosops/ci-cd-secure-api.git
cd ci-cd-secure-api
```

Substitua `SEU_USUARIO` pelo seu usuário do GitHub.

---

### 2. Criar ambiente virtual

Linux ou macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

### 3. Instalar dependências

```bash
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

Ou usando Makefile:

```bash
make install
```

---

### 4. Rodar a API

```bash
uvicorn secure_api.main:app --reload
```

Ou:

```bash
make run
```

A aplicação ficará disponível em:

```text
http://localhost:8000
```

Documentação interativa:

```text
http://localhost:8000/docs
```

Documentação alternativa:

```text
http://localhost:8000/redoc
```

---

## Endpoints

### `GET /health`

Verifica se a API está em execução.

Exemplo:

```bash
curl http://localhost:8000/health
```

Resposta esperada:

```json
{
  "status": "ok"
}
```

---

### `GET /version`

Retorna metadados básicos da aplicação.

Exemplo:

```bash
curl http://localhost:8000/version
```

Resposta esperada:

```json
{
  "name": "CI/CD Secure API",
  "version": "0.1.0"
}
```

---

## Como rodar os testes

```bash
pytest
```

Ou:

```bash
make test
```

Os testes geram relatório de cobertura no terminal e também podem gerar o arquivo `coverage.xml`.

---

## Como rodar lint

```bash
ruff check src tests
```

Ou:

```bash
make lint
```

---

## Como rodar formatação

```bash
ruff format src tests
```

Ou:

```bash
make format
```

Para apenas verificar se a formatação está correta:

```bash
ruff format --check src tests
```

---

## Como rodar checagem de tipos

```bash
mypy
```

Ou:

```bash
make type-check
```

---

## Como rodar verificações de segurança localmente

### Bandit

```bash
bandit -r src
```

### pip-audit

```bash
pip-audit
```

Ou usando Makefile:

```bash
make security
```

---

## Como rodar todas as verificações locais

```bash
make check
```

Esse comando deve executar:

- lint;
- type check;
- testes;
- verificações de segurança.

---

## Como usar pre-commit

### Instalar hooks

```bash
pre-commit install
```

### Rodar hooks manualmente

```bash
pre-commit run --all-files
```

O uso de pre-commit ajuda a encontrar problemas antes que eles cheguem ao pipeline.

---

## Como rodar com Docker

### Build da imagem

```bash
docker build -t ci-cd-secure-api .
```

Ou:

```bash
make docker-build
```

### Executar container

```bash
docker run --rm -p 8000:8000 ci-cd-secure-api
```

Ou:

```bash
make docker-run
```

### Testar aplicação no container

```bash
curl http://localhost:8000/health
```

Resposta esperada:

```json
{
  "status": "ok"
}
```

---

## Pipeline de CI

O pipeline de CI roda em pull requests para a branch `main`.

Objetivo:

> Garantir que o código tenha qualidade, testes e segurança antes de entrar na branch principal.

Fluxo:

```text
Pull Request
└── CI
    ├── Checkout
    ├── Setup Python
    ├── Install dependencies
    ├── Ruff lint
    ├── Ruff format check
    ├── mypy
    ├── pytest
    ├── coverage
    ├── Bandit
    ├── pip-audit
    ├── Semgrep
    └── Gitleaks
```

---

## Pipeline de CD

O pipeline de CD roda em push para a branch `main`.

Objetivo:

> Gerar uma imagem Docker segura e publicá-la em um registry.

Fluxo:

```text
Push main
└── CD
    ├── Checkout
    ├── Setup Docker Buildx
    ├── Login no registry
    ├── Build Docker image
    ├── Trivy image scan
    ├── Upload SARIF report
    ├── Upload scan artifact
    └── Push Docker image
```

---

## Publicação da imagem Docker

O projeto está preparado para publicar imagens no GitHub Container Registry.

Formato esperado da imagem:

```text
ghcr.io/SEU_USUARIO/ci-cd-secure-api:latest
ghcr.io/SEU_USUARIO/ci-cd-secure-api:<commit-sha>
```

A tag `latest` aponta para a versão mais recente da branch `main`.

A tag com o SHA do commit permite rastreabilidade.

---

## Security Controls

Esta seção explica os controles de segurança utilizados no projeto.

Ela é uma das partes mais importantes do README, porque mostra que o projeto segue uma mentalidade DevSecOps.

---

### Bandit

Bandit analisa código Python em busca de problemas comuns de segurança.

Ele pode encontrar padrões como:

- uso inseguro de funções;
- chamadas perigosas de subprocessos;
- uso de bibliotecas inseguras;
- problemas comuns em código Python.

No projeto:

```bash
bandit -r src
```

---

### Semgrep

Semgrep é uma ferramenta de SAST, ou seja, Static Application Security Testing.

Ela analisa o código-fonte com regras de segurança e qualidade.

No projeto, Semgrep roda no CI para procurar padrões inseguros em código Python.

---

### Gitleaks

Gitleaks procura secrets expostos no repositório.

Exemplos de secrets:

- tokens;
- senhas;
- API keys;
- chaves privadas;
- credenciais de serviços.

O objetivo é impedir que segredos sejam enviados para o histórico do Git.

---

### Trivy

Trivy escaneia a imagem Docker em busca de vulnerabilidades conhecidas.

Ele pode identificar problemas em:

- pacotes do sistema operacional;
- bibliotecas instaladas;
- dependências presentes na imagem;
- configurações inseguras.

No projeto, a imagem é escaneada antes de ser publicada.

---

### pip-audit

pip-audit verifica dependências Python em busca de vulnerabilidades conhecidas.

Ele complementa o Trivy porque olha diretamente para o ecossistema Python.

No projeto:

```bash
pip-audit
```

---

### Dependabot

Dependabot verifica periodicamente se há novas versões para dependências e ferramentas usadas no projeto.

Ele pode abrir pull requests automáticos para atualizar:

- pacotes Python;
- imagens Docker;
- GitHub Actions.

Isso ajuda a manter o projeto saudável e reduz o risco de usar versões antigas com vulnerabilidades conhecidas.

---

## Boas práticas aplicadas

### KISS

O projeto evita complexidade desnecessária.

Não há banco de dados, autenticação, filas, Kubernetes ou Terraform nesta primeira versão.

A ideia é mostrar bem o essencial:

- API;
- testes;
- Docker;
- CI/CD;
- segurança.

---

### DRY

Configurações são centralizadas sempre que possível.

Exemplos:

- `pyproject.toml` concentra configurações de ferramentas Python;
- `Makefile` centraliza comandos locais;
- workflows reutilizam comandos simples e claros.

---

### Código autodocumentado

O código usa:

- nomes claros;
- funções pequenas;
- type hints;
- docstrings objetivas;
- poucos comentários.

Comentários são usados apenas quando ajudam a explicar decisões, não para repetir o que o código já mostra.

---

### Simples é melhor que perfeito

É melhor ter:

- um endpoint funcionando;
- testes passando;
- Docker funcional;
- CI/CD confiável;
- README bem explicado;

do que ter muitas funcionalidades e pouca qualidade.

---

## Branch protection recomendada

Configurações sugeridas no GitHub:

- exigir pull request antes do merge;
- exigir que o CI passe antes do merge;
- bloquear force push;
- bloquear deleção da branch;
- exigir revisão de pelo menos uma pessoa, se o projeto tiver colaboradores.

---

## Comandos principais

```bash
make install
make run
make test
make lint
make format
make type-check
make security
make check
make docker-build
make docker-run
```

