import os
import shutil
import pandas as pd

# 📌 Passo 1: Carregar o arquivo CSV com os diagnósticos das imagens
df = pd.read_csv("dataset/HAM10000_metadata.csv")  # Certifique-se de que o caminho está correto

# 📌 Passo 2: Criar pastas para separar as imagens
os.makedirs("dataset/imagens_cancer", exist_ok=True)
os.makedirs("dataset/imagens_normais", exist_ok=True)

# 📌 Passo 3: Definir quais diagnósticos são câncer (SIGLAS IMPORTANTES)
cancer_labels = ["mel"]  # "mel" significa melanoma, que é câncer de pele

# 📌 Passo 4: Caminho onde as imagens estão armazenadas
pasta_origem_1 = "dataset/HAM10000_images_part_1/"
pasta_origem_2 = "dataset/HAM10000_images_part_2/"

# 📌 Passo 5: Mover as imagens para as pastas corretas
for index, row in df.iterrows():
    nome_imagem = row["image_id"] + ".jpg"  # Adicionar extensão .jpg
    diagnostico = row["dx"]  # Diagnóstico da lesão

    # Verifica em qual das duas pastas a imagem está
    origem = None
    if os.path.exists(os.path.join(pasta_origem_1, nome_imagem)):
        origem = os.path.join(pasta_origem_1, nome_imagem)
    elif os.path.exists(os.path.join(pasta_origem_2, nome_imagem)):
        origem = os.path.join(pasta_origem_2, nome_imagem)

    # Se a imagem foi encontrada, move para a pasta correta
    if origem:
        if diagnostico in cancer_labels:
            destino = os.path.join("dataset/imagens_cancer", nome_imagem)
        else:
            destino = os.path.join("dataset/imagens_normais", nome_imagem)

        shutil.move(origem, destino)

# 📌 Passo 6: Verificar quantas imagens foram organizadas
num_cancer = len(os.listdir("dataset/imagens_cancer"))
num_normais = len(os.listdir("dataset/imagens_normais"))

print(f"✅ Total de imagens com câncer movidas: {num_cancer}")
print(f"✅ Total de imagens normais movidas: {num_normais}")
print("🚀 Organização finalizada com sucesso!")
