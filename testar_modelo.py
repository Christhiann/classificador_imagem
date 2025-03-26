import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Carregar o modelo treinado
modelo = load_model('modelo.h5')  # Certifique-se de que o modelo treinado existe

# Pasta onde estão as imagens de teste
pasta_teste = 'dataset/teste/'  # Caminho da pasta onde colocou as imagens

# Listar todas as imagens na pasta
imagens_teste = [f for f in os.listdir(pasta_teste) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Definir o limiar para a predição
limiar = 0.6  # Tente aumentar para reduzir falsos positivos

if not imagens_teste:
    print("Nenhuma imagem encontrada na pasta de teste.")
else:
    for img_nome in imagens_teste:
        caminho_imagem = os.path.join(pasta_teste, img_nome)

        # Carregar e pré-processar a imagem
        img = image.load_img(caminho_imagem, target_size=(224, 224))  # Redimensiona
        img_array = image.img_to_array(img)  # Converte para array NumPy
        img_array = np.expand_dims(img_array, axis=0)  # Adiciona dimensão de batch
        img_array = img_array / 255.0  # Normaliza os pixels (0 a 1)

        # Fazer a predição
        previsao = modelo.predict(img_array)
        
        # Alterando o limiar da decisão
        classe_predita = "Com câncer" if previsao[0][0] > limiar else "Sem câncer"
        
        # Exibir o resultado
        print(f"Imagem: {img_nome} -> {classe_predita} (Confiança: {previsao[0][0]:.2f})")
