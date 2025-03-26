import pandas as pd
import os

# Carregar o CSV
df = pd.read_csv("dataset/HAM10000_metadata.csv")

# Caminhos das pastas
pasta_cancer = "dataset/imagens_cancer"
pasta_normais = "dataset/imagens_normais"

# Listar arquivos movidos
arquivos_cancer = set(os.listdir(pasta_cancer))
arquivos_normais = set(os.listdir(pasta_normais))

# Criar listas para verificar erros
erros_cancer = []
erros_normais = []

# Verificar se todas as imagens foram para as pastas corretas
for index, row in df.iterrows():
    nome_imagem = row["image_id"] + ".jpg"
    diagnostico = row["dx"]  # Diagnóstico da lesão

    if diagnostico == "mel" and nome_imagem not in arquivos_cancer:
        erros_cancer.append(nome_imagem)
    
    if diagnostico != "mel" and nome_imagem not in arquivos_normais:
        erros_normais.append(nome_imagem)

# Exibir os erros, se houver
if erros_cancer:
    print(f"⚠️ {len(erros_cancer)} imagens com 'mel' foram para o lugar errado!")
    print(erros_cancer[:10])  # Exibir apenas os 10 primeiros erros

if erros_normais:
    print(f"⚠️ {len(erros_normais)} imagens normais foram para o lugar errado!")
    print(erros_normais[:10])  # Exibir apenas os 10 primeiros erros

if not erros_cancer and not erros_normais:
    print("✅ A separação das imagens está 100% correta!")
