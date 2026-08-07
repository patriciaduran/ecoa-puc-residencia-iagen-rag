# Aula 02 - Processamento de PDFs com Docling e Extração de Metadados

## Objetivo

Desenvolver uma aplicação em Python para converter documentos PDF em Markdown utilizando o Docling e, em seguida, extrair metadados estruturados (título, autores, ano e palavras-chave) desses documentos por meio de Structured Outputs, utilizando a API da Groq.

## Conteúdos Trabalhados

- Conversão de arquivos PDF para Markdown com Docling;
- Manipulação de arquivos e diretórios com `pathlib`;
- Configuração da API da Groq;
- Uso de variáveis de ambiente (`.env`);
- Extração de metadados estruturados com Structured Outputs (`response_format` / `json_schema`);
- Definição de JSON Schema para validação de saída do modelo;
- Persistência dos resultados em arquivos `.json`.

## Estrutura da Aula

**Repositório**

```text
aula_02/
├── arquivos/
│   ├── bioetica_e_ia.pdf
│   ├── escrita_academica_ia.pdf
│   └── twitter_algoritmo.pdf
├── arquivos_md/
│   ├── bioetica_e_ia.md
│   ├── escrita_academica_ia.md
│   └── twitter_algoritmo.md
├── output_json/
│   ├── output_bioetica_e_ia.json
│   ├── output_escrita_academica_ia.json
│   └── output_twitter_algoritmo.json
├── converte_texto.py
├── extrai_json.py
└── README.md
```

**Ambiente Local**

```text
aula_02/
├── ... (arquivos acima)
└── .env
```

## Criação da Chave da API

Para utilizar a API da Groq, é necessário possuir uma conta na plataforma.

1. Acesse o [Groq Console](https://console.groq.com/).
2. Faça login ou crie uma conta.
3. Gere uma nova chave de API.
4. Copie a chave gerada e utilize-a no arquivo `.env`.

## Configuração da API da Groq

Crie um arquivo `.env` na pasta `aula_02` com a seguinte variável:

```env
GROQ_API_KEY=sua_chave_da_groq
GROQ_MODEL=openai/gpt-oss-20b
```

A chave da API é uma informação sensível e não deve ser enviada para o repositório. Certifique-se de que o `.gitignore` contenha:

```text
.env
venv/
```

## Instalação de Dependências Específicas

Além das dependências do ambiente principal (ver [README raiz](../README.md)), esta aula requer o Docling e o SDK da Groq:

```bash
pip install docling groq python-dotenv
```

Documentação de instalação do Docling: https://docling-project.github.io/docling/getting_started/installation/#development-setup

## ▶️ Execução

### Tarefa 1 - Conversão de PDFs para Markdown

Baixe os PDFs indicados pelo professor e coloque-os na pasta `arquivos/`. Em seguida, execute:

```bash
# Acessar a pasta da Aula 02
cd aula_02

# Executar a conversão
python converte_texto.py
```

O script converte todos os PDFs da pasta `arquivos/` e salva os arquivos `.md` correspondentes na pasta `arquivos_md/`.

### Tarefa 2 - Extração de Metadados com Structured Outputs

Com os arquivos `.md` já gerados, execute:

```bash
python extrai_json.py
```

O script processa cada arquivo `.md` da pasta `arquivos_md/`, envia o conteúdo para o modelo definido no `.env` via API da Groq com Structured Outputs, e salva o resultado estruturado (título, autores, ano e palavras-chave) em um arquivo `.json` na pasta `output_json/`.

## Observação Técnica

- Devido ao limite de tokens por minuto (TPM) do tier gratuito da Groq, o conteúdo de cada `.md` é truncado para os primeiros 3000 caracteres antes do envio, suficiente para capturar título, autores, ano e palavras-chave, que normalmente aparecem no início dos artigos.