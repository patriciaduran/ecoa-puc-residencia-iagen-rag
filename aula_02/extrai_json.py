# Extrai json

# Bibliotecas
import os
import json
from dotenv import load_dotenv
from groq import Groq
from pathlib import Path

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

pasta_md = Path("arquivos_md")
pasta_saida = Path("output_json")
pasta_saida.mkdir(exist_ok=True)

schema = {
    "type": "object",
    "properties": {
        "titulo": {"type": "string"},
        "autores": {"type": "array", "items": {"type": "string"}},
        "ano": {"type": "integer"},
        "palavras_chave": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["titulo", "autores", "ano", "palavras_chave"],
    "additionalProperties": False
}

for arquivo in pasta_md.glob("*.md"):
    print(f"Processando: {arquivo.name}")

    with open(arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()[:3000]

    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL"),
        messages=[
            {"role": "system", "content": "Você é um assistente que extrai metadados de artigos acadêmicos."},
            {"role": "user", "content": f"Extraia os metadados do seguinte texto:\n\n{conteudo}"}
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {"name": "metadados_paper", "strict": True, "schema": schema}
        }
    )

    dados = json.loads(response.choices[0].message.content)

    saida = pasta_saida / f"output_{arquivo.stem}.json"
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

print("Extração finalizada!")