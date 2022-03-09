from typing import Any
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField,SelectField
from wtforms.validators import InputRequired,Optional,AnyOf,URL,NumberRange

class AddPetForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Pet Name",validators=[InputRequired()])
    species = StringField("Species",validators=[InputRequired(), AnyOf(['cat','dog','porcupine'], message="Please enter correct species.")])
    photo_url = StringField("Photo URL",validators=[InputRequired(),URL(require_tld=True, message="Please enter a valid URL")])
    age = IntegerField("Age",validators=[Optional(),NumberRange(min=1, max=30, message="Age cannot be greater than 30yrs.")])
    notes = StringField("Notes",validators=[Optional()])
    available = SelectField("Available", choices=[(True, True),  (False, False)],validators=[InputRequired()],coerce=bool)


class EditPetForm(FlaskForm):
    """Form for adding snacks."""
    photo_url = StringField("Photo URL",validators=[Optional(),URL(require_tld=True, message="Please enter a valid URL")])
    notes = StringField("Notes",validators=[Optional()])
    available = SelectField("Available", choices=[(True, True),  (False, False)],validators=[Optional()],coerce=bool)