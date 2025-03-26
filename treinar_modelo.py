import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator # é uma ferramneta do tensorflow que ajuda no preprocessamnto automatico de imagnes, ele ajusta tamanho pixels e divide dados
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam

#criar a rede neural da ia#

modelo = models.Sequential()
#dividindo por camadas
#camada de entrada
modelo.add(layers.Input(shape=(224, 224, 3)))
#primrira camada
modelo.add(layers.Conv2D(32, (3,3), activation='relu'))
modelo.add(layers.MaxPooling2D((2,2)))
#segunda camada
modelo.add(layers.Conv2D(64, (3, 3), activation = 'relu'))
modelo.add(layers.MaxPooling2D((2,2)))
#terceira camada
modelo.add(layers.Conv2D(128, (3,3), activation = 'relu'))
modelo.add(layers.MaxPooling2D((2,2)))

#tranforma as imagens 2d em 1d para uma camada densa
modelo.add(layers.Flatten())

#camada densa totalmete conectada
modelo.add(layers.Dense(128, activation='relu')) # camada totalmente conectada
modelo.add(layers.Dense(1, activation= 'sigmoid')) # esse sigmoid é ideal para a clasificaçao binaria; doenca ou nao

#compilar o modelo
modelo.compile(optimizer=Adam(learning_rate=0.0001), 
               loss='binary_crossentropy', 
               metrics=['accuracy'])

# exibir resumo do modelo
modelo.summary()

#cruiar o gerador de imagnes
gerador = ImageDataGenerator(rescale=1./255, validation_split=0.2) # normaliza os valores de pixesl entre 0 e 255,  separa 20% das imagens para validaçao e 80% para treino

#criar o gerador para treinar esses dados em forma de imagems
treino_gera = gerador.flow_from_directory(
    'dataset/', # onde esta  as imagens
    target_size=(224, 224), # tamanho das imagnes em pixel para IA
    batch_size=32, # quantas imagens sao processadas por ves  por lote por vez
    class_mode='binary', # classificados de desses dados em sim ou nao/ com cancer ou nao, em fotam de binario
    subset='training' # define que os 80% dessas imangens sao para trieno
)

#fazer agora que o gerador faça a validaçao desses dados
# sao as mesma linhas de codigo, so vai mudar a ultima linha, subset, que aqui vai ser validados das 20% e os 80% a cima foi para teste
valida_gera = gerador.flow_from_directory(
    'dataset/', # onde esta as imagnes
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='validation', # os outros 20% das imagens para validaçao

)

# fazer o treinamneto do modelo com as imagens
# criado callback para para o treinamento quando a perda nao melhorar
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
 #treinando a IA

historico = modelo.fit(
    treino_gera,# dados de treino
    validation_data = valida_gera, # dados de validaçao
    epochs=10, # numero de vezes o modelo vera todas as imagens
    callbacks=[early_stopping] # para eviat overfitting

)

print('modelo treinado com sucesso')

modelo.save('modelo.h5') # salvar o modelo treinado


