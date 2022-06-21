from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,  BooleanField, FloatField, IntegerField, SelectField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


##WTForm
class CreateForm(FlaskForm):

    age = IntegerField("Age", validators=[DataRequired()])
    hypertension = BooleanField("History of Hypertension", )
    heart_disease = BooleanField("History of Heart Disease")
    ever_married = BooleanField('Ever Married?',)
    residence_type = SelectField("Residence Type", choices=[(0, "Rural"),(1, "Urban")], validators=[DataRequired()])
    work_type = SelectField("Work Type", choices = [("govt_job","Govertment Job"),("never_worked", "Never Worked"),("private", "Private"),("self_employed", "Self-employed"), ("children", "Children")], validators = [DataRequired(),])
    avg_glucose_level = FloatField("Average Glucose Level (mg/dl)")
    bmi = FloatField("BMI", validators=[DataRequired()])
    gender = SelectField("Gender",choices = [("male", "Male"), ("female", "Female"), ("other", "Other")], validators=[DataRequired()])
    smoking_status = SelectField("Smoking Status", choices= [
        ("unknown", "Unknown"),("formerly_smoked", "Formerly Smoked"),("never_smoked","Never Smoked"),("smokes", "Smokes")],
                                 validators= [DataRequired()])
    submit = SubmitField()