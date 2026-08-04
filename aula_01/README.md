# Aula 01 - Introdução à IA Generativa

## Objetivo

Desenvolver uma aplicação em Python integrada à API da OpenAI para compreender o uso de variáveis de ambiente e a comunicação com modelos de linguagem (LLMs), por meio do envio de uma pergunta e do recebimento de uma resposta gerada por IA.

## Conteúdos Trabalhados

- Configuração do ambiente Python;
- Criação da chave da API da OpenAI;
- Uso de variáveis de ambiente (`.env`);
- Configuração do arquivo `.gitignore`;
- Integração entre Python e um modelo de linguagem (LLM);
- Envio de uma solicitação à API e processamento da resposta.

## Estrutura da Aula

**Repositório**

```text
aula_01/
├── hello_llm.py
└── README.md
```

**Ambiente Local**

```text
aula_01/
├── hello_llm.py
├── README.md
└── .env
```

## Criação da Chave da API

Para utilizar a API da OpenAI, é necessário possuir uma conta na plataforma da OpenAI.

1. Acesse a [OpenAI Platform](https://platform.openai.com/login).
2. Faça login ou crie uma conta.
3. Gere uma nova chave de API.
4. Copie a chave gerada e utilize-a no arquivo `.env`.

> **Importante:** a chave de API é exibida apenas no momento da criação. Guarde-a em um local seguro e nunca a compartilhe ou a envie para repositórios públicos.

## Configuração da API da OpenAI

Para executar o exemplo desta aula, crie um arquivo `.env` na pasta `aula_01` com as seguintes variáveis:

```env
OPENAI_API_KEY=sua_chave_da_openai
OPENAI_MODEL=gpt-5.4-mini
```

A chave da API é uma informação sensível e não deve ser enviada para o repositório. Caso esteja desenvolvendo o projeto do zero, adicione ao arquivo `.gitignore`:

```text
.env
venv/
```

Dessa forma, o arquivo `.env` e o ambiente virtual permanecerão apenas na máquina local.

Caso tenha clonado este repositório, essa configuração já está presente no arquivo `.gitignore`.

## ▶️ Execução

Com o ambiente local configurado conforme as instruções do [README principal](../README.md) e após configurar a chave da API da OpenAI, execute:

```bash
# Acessar a pasta da Aula 01
cd aula_01

# Executar a aplicação
python hello_llm.py
```

O programa enviará uma solicitação para a API da OpenAI e exibirá a resposta no terminal.
