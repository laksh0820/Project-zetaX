from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField, PasswordField, SubmitField,TextAreaField,RadioField,BooleanField
from wtforms.validators import DataRequired,EqualTo,Email

class SignUpForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(),Email(message="Invalid email address (should be of the form something@example.com)")])
    password = PasswordField("Password",validators=[DataRequired(),EqualTo('confirm_password',message="Password does not match to Confirm Password. Please retype")])
    confirm_password = PasswordField("Confirm-Password",validators=[DataRequired()])
    type = RadioField("Type",validators=[DataRequired()],choices=[('Contestant','Contestant'),('Judge','Judge')])
    submit = SubmitField("Submit")

class SignInForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(),Email(message="Invalid email address (should be of the form something@example.com)")])
    password = PasswordField("Password",validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Submit")

class ProblemForm(FlaskForm):
    title = StringField("Title",validators=[DataRequired()])
    description = TextAreaField("Description",validators=[DataRequired()])
    sample_input = TextAreaField("Sample Input",validators=[DataRequired()])
    sample_output = TextAreaField("Sample Output",validators=[DataRequired()])
    exe_time = IntegerField("Expected Execution Time",validators=[DataRequired()])
    exe_space = IntegerField("Expected Execution Space",validators=[DataRequired()])
    judging_testcases = TextAreaField("Judging Testcases",validators=[DataRequired()])
    exp_testcases_output = TextAreaField("Expected Testcases Output",validators=[DataRequired()])
    submit = SubmitField("Submit")  