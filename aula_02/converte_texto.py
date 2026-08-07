# Manipulando Arquivos

# Bibliotecas
import os
os.environ["TORCH_COMPILE_DISABLE"] = "1"

from docling.document_converter import DocumentConverter
from pathlib import Path

# Converte arquivo pdf em md 
pasta_entrada = Path("arquivos")
pasta_saida = Path("arquivos_md")

# Cria pasta de saída, se não existir
pasta_saida.mkdir(exist_ok=True)

converter = DocumentConverter()

for arquivo in pasta_entrada.glob("*.pdf"):
    print(f"Convertendo: {arquivo.name}")

    doc = converter.convert(str(arquivo)).document

    arquivo_md = pasta_saida / f"{arquivo.stem}.md"

    with open(arquivo_md, "w", encoding="utf-8") as f:
        f.write(doc.export_to_markdown())

print("Conversão finalizada!")

