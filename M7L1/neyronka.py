from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np


np.set_printoptions(suppress=True)
model = load_model("keras_model.h5", compile=False)
class_names = open("labels.txt", "r", encoding="utf-8").readlines()

def func(path):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(f"images/{path}").convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    # confidence_score = prediction[0][index]
    # if confidence_score < 0.5:
    #     class_name = '0 Неизвестно\n'

    if class_name[2:-1] == 'Brimstone':
        sposobki = ['ЗАЖИГАТЕЛЬНАЯ ГРАНАТА', 'НЕБЕСНЫЙ ДЫМ', 'МАЯЧОК-СТИМУЛЯТОР', 'ОРБИТАЛЬНЫЙ УДАР']
    elif class_name[2:-1] == 'Sage':
        sposobki = ['СФЕРА ЗАМЕДЛЕНИЯ', 'СФЕРА ЛЕЧЕНИЯ', 'СФЕРА БАРЬЕРА', 'ВОСКРЕШЕНИЕ']
    elif class_name[2:-1] == 'Phoenix':
        sposobki = ['КРУЧЕНАЯ ПОДАЧА', 'ГОРЯЧИЕ РУКИ', 'ПЕКЛО', 'ВОЗВРАТ']
    elif class_name[2:-1] == 'Raze':
        sposobki = ['ВЗРЫВНОЙ РАНЕЦ', 'КАССЕТНАЯ ГРАНАТА', 'БОМБОТРОН', 'ГАСИМ СВЕЧИ']
    elif class_name[2:-1] == 'Skye':
        sposobki = ['СЛЕДОПЫТ', 'ПУТЕВОДНЫЙ СВЕТ', 'НОВАЯ ПОРОСЛЬ', 'ИЩЕЙКИ']
    elif class_name[2:-1] == 'Yoru':
        sposobki = ['ОШЕЛОМЛЕНИЕ', 'НЕЗВАНЫЙ ГОСТЬ', 'ПРИМАНКА', 'ПРОСТРАНСТВЕННЫЙ ДРИФТ']
    elif class_name[2:-1] == 'Astra':
        sposobki = ['ВЗРЫВ СВЕРХНОВОЙ', 'ТУМАННОСТЬ', 'ГРАВИТАЦИОННЫЙ КОЛОДЕЦ', 'ПРОСТРАНСТВЕННЫЙ РАЗЛОМ']
    else:
        sposobki = []
    # print(confidence_score)
    # print(class_name)
    return class_name[2:-1], sposobki

    # print("Confidence Score:", confidence_score)
