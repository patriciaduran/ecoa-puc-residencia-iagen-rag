<p align="center">
  <img src="./assets/banner_iagen_rag.png" alt="Banner IA Generativa e RAG" width="100%">
</p>

# Ecoa | PUC Rio — Residência em Tecnologia
### Trilha: IA Generativa & RAG

A Residência envolve o desenvolvimento de soluções de Inteligência Artificial com foco em RAG (*Retrieval-Augmented Generation*), técnica voltada à criação de sistemas capazes de buscar informações em bases de conhecimento e gerar respostas inteligentes, fundamentadas e com fonte rastreável. 

Durante o programa, os residentes irão estruturar documentos e bases de conhecimento, gerar embeddings e configurar bases vetoriais, desenvolver fluxos de recuperação de informação e construir aplicações que utilizam IA generativa para apoiar consultas, atendimento, automação de processos e tomada de decisão [[1]](#referencia-1).


## 🎯 Objetivo do Repositório
Registrar os estudos, exercícios e projetos desenvolvidos durante a trilha IA Generativa & RAG da Residência em Tecnologias do Ecoa | PUC Rio.


### 📂 Estrutura do Repositório

```text
ecoa-puc-residencia-iagen-rag
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── assets
│   └── banner_iagen_rag.png
│
├── aula_01
│   ├── README.md
│   └── hello_llm.py
│
└── ...
```

Cada aula e projeto possui seu próprio arquivo README com as instruções técnicas e informações detalhadas daquela etapa específica.


## 📆 Cronograma de Aulas

### Aula 01 — Introdução à IA Generativa
Aplicação Python integrada à API da OpenAI para interação e testes iniciais com modelos de linguagem (LLMs).


## 🛠️ Tecnologias e Ferramentas

* **Linguagem:** Python
* **IA:** OpenAI API
* **Ambiente:** VS Code & Python `venv`
* **Controle de Versão:** Git & GitHub


## ⚙️ Configuração do Ambiente Local

Para executar os códigos das aulas na sua máquina local, siga o fluxo de comandos abaixo em seu terminal:

```bash
# Clonar o repositório
git clone https://github.com/patriciaduran/ecoa-puc-residencia-iagen-rag.git
cd ecoa-puc-residencia-iagen-rag

# Criar ambiente virtual
python -m venv venv

# Ativar o ambiente virtual (Windows)
venv\Scripts\activate

# Instalar todas as dependências necessárias
pip install -r requirements.txt
```

> **Nota:** Após a ativação do ambiente virtual, o seu terminal exibirá o prefixo `(venv)` indicando que o isolamento está ativo e pronto para uso.


## 🔗 Referências

<a id="referencia-1"></a>
[[1]](#referencia-1) [Residência em Tecnologia - Ecoa PUC-Rio](https://puc-rio.br)