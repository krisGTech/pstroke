from flask import Flask , render_template , request 

import pickle
import numpy as np

model = pickle.load(open('stroke_rf_model.pkl', 'rb'))

app = Flask(__name__)
healthy_status = True


@app.route('/')
def man():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def makePredict():
    int_features=[float(x) for x in request.form.values()]
    final=np.array([int_features])

    
    
    prediction=model.predict_proba(final)
    print(prediction)
    output='{0:.{1}f}'.format(prediction[0][1], 2)
   

    if output > str(0.45):
        healthy_status = True
        return render_template('index.html',predict = 'Your are at high risk of stroke. Please see physician.Probability of stroke is {}'.format(output), messgae_color=True)
    
    else:
        healthy_status=False
        return render_template('index.html',predict=' Congratulation you are in GOOD HEALTH. Probability of stroke is {}'.format(output),messgae_color=False)

if __name__ == "__main__":
    app.run(debug=True) 