# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import flask
import joblib, pickle
from flask import request

### Initialize webapp
app = flask.Flask(__name__, template_folder = 'templates')

### Define web home
@app.route('/home', methods = ['GET'])
def main_home():
    
    return flask.render_template('home-index.html')


### Define prediction route
@app.route('/predict', methods = ['GET'])
def predict():
    try:
        ### Get the input features from the request form
        cap_shape = int(request.args.get('cap-shape'))
        cap_surface = int(request.args.get('cap-surface'))
        cap_color = int((request.args.get('cap-color')))
        bruises = int(request.args.get('bruises'))
        odor = int(request.args.get('odor'))
        
        gill_attachment = int(request.args.get('gill-attachment'))
        gill_spacing = int(request.args.get('gill-spacing'))
        gill_size = int(request.args.get('gill-size'))
        gill_color = int(request.args.get('gill-color'))
        stalk_shape = int(request.args.get('stalk-shape'))
        
        stalk_root = int(request.args.get('stalk-root'))
        stalk_surface_above_ring = int(request.args.get('stalk-surface-above-ring'))
        stalk_surface_below_ring = int(request.args.get('stalk-surface-below-ring'))
        stalk_color_above_ring = int(request.args.get('stalk-color-above-ring'))
        stalk_color_below_ring = int(request.args.get('stalk-color-below-ring'))
        
        veil_color = int(request.args.get('veil-color'))
        ring_number = int(request.args.get('ring-number'))
        ring_type = int(request.args.get('ring-type'))
        spore_print_color = int(request.args.get('spore-print-color'))
        
        population = int(request.args.get('population'))
        habitat = int(request.args.get('habitat'))
        
        ### Combine the input features to form an input array
        input_array = np.array([cap_shape, cap_surface, cap_color,
                               bruises, odor, gill_attachment, gill_spacing,
                               gill_size, gill_color, stalk_shape, stalk_root,
                               stalk_surface_above_ring, stalk_surface_below_ring,
                               stalk_color_above_ring, stalk_color_below_ring,
                               veil_color, ring_number, ring_type, spore_print_color, population, habitat])
        
        input_array = input_array.astype('int64')
        
        input_array = input_array.reshape(1, -1)
        print(input_array.shape)
        print(input_array)
        print(input_array.dtype)
        
        model = pickle.load(open('Decision Tree Classifier.pkl', 'rb'))
        
        predictions = model.predict(input_array)[0]
        
        if predictions == 0:
            predictions = 'Poisonous'
        else:
            predictions = 'Edible'
        print(model)
            
        return flask.render_template('output-index.html', results = predictions)
    
    except:
        raise Exception('Error. Input valid features.')
        
if __name__ == '__main__':
    app.run(debug = False)