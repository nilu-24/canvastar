from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image, ImageOps
import base64
import io
from io import BytesIO
app = Flask(__name__)
model = keras.models.load_model('model2.h5') #loading the model
input_list = ["Aquarius", "Aries", "Cancer", "Canis Major", "Cassiopeia", "Cygnus", "Leo", "Lyra", "Orion", "Pisces", "Scorpius", "Taurus", "Ursa Minor", "Virgo"]
@app.route("/")
def index():
    return render_template("index.html")
@app.route('/hook', methods=['POST'])
def get_image():
    
    content = request.form.get("imageBase64").split(';')[1]
    img_enc = content.split(',')[1]
    body = base64.decodebytes(img_enc.encode('utf-8'))
    img = Image.open(BytesIO(body)).convert('L') # L means turn gray
    img = img.resize((128,128))
    img= np.asarray(img)
    img = img/255
    img = img.reshape(1,128,128,1)

    prediction = input_list[np.argmax(model.predict(img))]

    sorted_predictions = np.sort(model.predict(img))
    sorted_predictions=sorted_predictions.flatten()
    sorted_predictions=list(sorted_predictions)

    predictions = model.predict(img).flatten()
    predictions = list(predictions)

    second_best = (sorted_predictions[-2])
    third_best = (sorted_predictions[-3])

    second_index = predictions.index(second_best)
    third_index = predictions.index(third_best)
   
    second_val = input_list[second_index]
    third_val=input_list[third_index]
    my_dict = {'pred': prediction, 'score':str(round(np.amax(model.predict(img))*100,2)),'pred_2':second_val,'score_2':str(round(second_best*100,2)),'pred_3':third_val,'score_3':str(round(third_best*100,2))}
    return my_dict