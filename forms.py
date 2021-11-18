from flask_wtf import FlaskForm
from wtforms.validators import NumberRange, DataRequired
from wtforms import SelectField, IntegerField, BooleanField, SubmitField
    
choise_property_type = ['Condominium', 'Dorm', 'Other']
choise_room_type = ['Entire home/apt', 'Private room', 'Shared room', 'Other']
choise_bed_type = ['Real Bed', 'Airbed', 'Futon',  'Other']
choise_cancellation_policy = ['flexible', 'moderate', 'strict', 'Other']
choise_city = ['Chicago', 'DC', 'LA', 'NYC', 'SF', 'Other']

class FormHouseSpecs(FlaskForm):
    log_price = IntegerField("Actual price:", default=0)
    accommodates = IntegerField("Number of accommodates:", default=0)
    bathrooms = IntegerField("Number of bathrooms:", default=0)
    cleaning_fee = BooleanField("Include commission for cleaning?:", default=0)
    review_scores_rating = IntegerField("Review scores rating:", default=0, validators=[NumberRange(min=0, max=100, message='Between 0 and 100')])
    bedrooms = IntegerField("Number of bedrooms:", default=0)
    beds = IntegerField("Number of beds:", default=0)
    property_type = SelectField("Property type:",
                                choices=choise_property_type,
                                validators=[DataRequired()])
    room_type = SelectField("Room type:",
                            choices=choise_room_type,
                            validators=[DataRequired()])
    bed_type = SelectField("Bed type:",
                            choices=choise_bed_type,
                            validators=[DataRequired()])
    cancellation_policy = SelectField("Cancellation policy:",
                                       choices=choise_cancellation_policy,
                                       validators=[DataRequired()])
    city = SelectField("City:",
                        choices=choise_city,
                        validators=[DataRequired()])

    submit = SubmitField('Send')
