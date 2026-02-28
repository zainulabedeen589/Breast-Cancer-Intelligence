# from flask import Flask, request, render_template
# import pickle
# import numpy as np
# import pandas as pd

# model = pickle.load(open('model.pkl', 'rb'))

# # flask aapplication
# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the form data
#     features = [float(x) for x in request.form.values()]
#     final_features = [np.array(features)]
#     prediction = model.predict(final_features)

#     output = prediction[0]
#     if output == 0:
#         return render_template('index.html', prediction_text='The breast cancer is Malignant')
#     else:
#         return render_template('index.html', prediction_text='The breast cancer is Benign')


# # python main function
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

# loading model
model = pickle.load(open("models/model.pkl", "rb"))

# flask app
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    features = request.form["feature"]
    features = features.split(",")
    np_features = np.asarray(features, dtype=np.float32)

    # prediction
    pred = model.predict(np_features.reshape(1, -1))
    message = ["Cancrouse" if pred[0] == 1 else "Not Cancrouse"]
    # print(message[0])
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
