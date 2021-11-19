from flask import Flask, render_template # importing the flask class
import config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy, model
import joblib 
import pandas as pd
from forms import FormHouseSpecs


app = Flask(__name__) # creating an instance of the Flask class

app.config.from_object(config)
Bootstrap(app)
db = SQLAlchemy(app)


data = {'accommodates'                 : 0,
        'bathrooms'                    : 0,
        'cleaning_fee'                 : 0,
        'review_scores_rating'         : 0,
        'bedrooms'                     : 0,
        'beds'                         : 0,
        'property_type_Condominium'    : 0,
        'property_type_Dorm'           : 0,
        'room_type_Entire home/apt'    : 0,
        'room_type_Private room'       : 0,
        'room_type_Shared room'        : 0,
        'bed_type_Airbed'              : 0,
        'bed_type_Futon'               : 0,
        'bed_type_Real Bed'            : 0,
        'cancellation_policy_flexible' : 0,
        'cancellation_policy_moderate' : 0,
        'cancellation_policy_strict'   : 0,
        'city_Chicago'                 : 0,
        'city_DC'                      : 0,
        'city_LA'                      : 0,
        'city_NYC'                     : 0,
        'city_SF'                      : 0}

@app.route('/') 
def index():
    return render_template("index.html")

@app.route('/predict_price', methods=["get", "post"]) 
def predict_price():
    """ Endpoint to predict price """
    form = FormHouseSpecs()

    if form.validate_on_submit():
        from models import HouseSpecs
        
        #Save values in database
        house = HouseSpecs()
        form.populate_obj(house)
        db.session.add(house)
        db.session.commit()
        
        # Write data values
        data['accommodates'] = form.accommodates.data
        data['bathrooms'] = form.bathrooms.data
        data['cleaning_fee'] = form.cleaning_fee.data
        data['review_scores_rating'] = form.review_scores_rating.data
        data['beds'] = form.beds.data
        if form.property_type.data != "Other":
            data[f"property_type_{form.property_type.data}" ] = 1
        if form.room_type.data != "Other":
            data[f"room_type_{form.room_type.data}" ] = 1
        if form.bed_type.data != "Other":
            data[f"bed_type_{form.bed_type.data}" ] = 1
        if form.cancellation_policy.data != "Other":
            data[f"cancellation_policy_{form.cancellation_policy.data}" ] = 1
        if form.city.data != "Other":
            data[f"city_{form.city.data}" ] = 1

        df = pd.DataFrame(data=data, index=[0])
        print(df)

        log_price_house = model_load.predict(df )

        return render_template("index.html", 
                                log_value_house=round(log_price_house[0], 3))

    return render_template("predict_price.html", form=form)

@app.route('/under_over_price', methods=["get", "post"]) 
def under_over_price(): 
    """ Endpoint to estimate if actual prices is under or over price """
    form = FormHouseSpecs()

    if form.validate_on_submit():
        from models import HouseSpecs
        
        #Save values in database
        house = HouseSpecs()
        form.populate_obj(house)
        db.session.add(house)
        db.session.commit()
        
        # Write data values
        data['accommodates'] = form.accommodates.data
        data['bathrooms'] = form.bathrooms.data
        data['cleaning_fee'] = form.cleaning_fee.data
        data['review_scores_rating'] = form.review_scores_rating.data
        data['beds'] = form.beds.data
        if form.property_type.data != "Other":
            data[f"property_type_{form.property_type.data}" ] = 1
        if form.room_type.data != "Other":
            data[f"room_type_{form.room_type.data}" ] = 1
        if form.bed_type.data != "Other":
            data[f"bed_type_{form.bed_type.data}" ] = 1
        if form.cancellation_policy.data != "Other":
            data[f"cancellation_policy_{form.cancellation_policy.data}" ] = 1
        if form.city.data != "Other":
            data[f"city_{form.city.data}" ] = 1

        df = pd.DataFrame(data=data, index=[0])

        log_price_house = model_load.predict(df)

        status_predict = "Over"
        if log_price_house > form.log_price.data:
            status_predict = "Under"

        return render_template("index.html", 
                                log_value_house=round(log_price_house[0], 3),
                                actual_price=round(form.log_price.data, 3),
                                status_predict = status_predict)

    return render_template("under_over_price.html", form=form)
 

if __name__ == '__main__':
    db.create_all()
    model_load = joblib.load('xgboost_final_model.pkl')
    app.run(debug=False, host='0.0.0.0') # This statement starts the server on your local machine.