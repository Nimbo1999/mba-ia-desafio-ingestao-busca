# Desafio MBA Engenharia de Software com IA - Full Cycle

## Visão geral

Esse repositório contém o código-fonte referente ao desafio proposto no MBA em Engenharia de Software com IA pela faculdade FullCycle.

O objetivo do desafio consiste em criar um software capaz de executar duas funcionalidades principais.

A primeira funcionalidade consiste em ler as informações de um arquivo PDF que contém um relatório de faturamento de empresas fictícias, e fazer a ingestão dessa informação em um banco de dados.

Já a segunda funcionalidade deve permitir que usuários realizem perguntas relacionadas aos dados do arquivo de faturamento das empresas aos modelos de inteligência artificial (No caso desse projeto o modelo `gpt-5-nano` da OpenAI) que estão integrados ao projeto com a ajuda do framework [LangChain](https://www.langchain.com/).

> Caso a pergunta não tenha relação com o arquivo de faturamento das empresas, o modelo deve responder `Não tenho informações necessárias para responder sua pergunta.`.

## Passo a passo para executar esse projeto

1. Inicie um ambiente virtual com o comando 

    ```bash
    # Crie um ambiente virtual com o gerenciador de pacotes uv
    uv venv
    ```
    ou
    ```bash
    # Crie um ambiente virtual com o python3
    python3 -m venv .venv
    ```

2. Ative seu ambiente virtual com o comando:

    ```bash
    source .venv/bin/activate
    ```
    ```bash
    # Para desativar o ambiente virtual, você pode executar o seguinte comando assim que estiver finalizado de interagir com o projeto
    deactivate
    ```

3. Instale as dependências que estão especificadas no arquivo [requirements.txt](./requirements.txt)

    ```bash
    # Instale as dependências com o gerenciador de pacotes uv
    uv pip install --requirements requirements.txt
    ```
    ou
    ```bash
    # Instale as dependências com o gerenciador de pacotes pip
    pip install --requirements requirements.txt
    ```

4. Inicie a ingestão do arquivo PDF na base de dados com a execução do script `src/ingest.py` com o seguinte comando

    ```bash
    # Utilize o comando make para executar o script
    make ingest
    ```
    ou
    ```bash
    # Rode o script com o python
    python src/ingest.py
    ```

4. Inicie o chat com as perguntas pré-definidas com o seguinte comando

    ```bash
    # Utilize o comando make para executar o script
    make chat
    ```
    ou
    ```bash
    # Rode o script com o python
    python src/chat.py
    ```

## Tecnologias utilizadas

- **Docker** para a criação do container responsável por rodar a base de dados.
- **PostgreSQL** e a extensão **PgVector** para armazenar os dados vetoriais.
- **LangChain** framework que oferece APIs para criar agentes e integrações com modelos de inteligência artificial.
- **Python** como sendo a linguagem de programação.

## Dependências

Esse projeto utiliza Python como sua linguagem de programação. Caso não tenha o Python instalado na sua máquina, sugiro instalar o gerenciador de pacotes [uv](https://docs.astral.sh/uv/) para gerenciar e instalar a versão que desejar.

### Como instalar o uv em seu MacOS ou Linux

Utilize o `curl` para instalar o gerenciador de pacotes com o seguinte comando em seu terminal:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Caso seu sistema não possua `curl`, você pode utilizar o `wget` com o seguinte comando em seu terminal:

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```
