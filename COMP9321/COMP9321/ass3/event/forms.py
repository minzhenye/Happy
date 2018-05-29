from flask_wtf import FlaskForm
from wtforms import StringField,validators,DateTimeField,FloatField
from wtforms.widgets import TextArea
from flask_wtf.file import FileField,FileAllowed

class BasicEventForm(FlaskForm):
  name = StringField('Party Name',validators=[validators.DataRequired(),validators.Length(min=2,max=80)])
  gplace = StringField('Places')
  lng = FloatField("Longtitude",validators=[validators.Optional()])
  lat = FloatField("Latitude",validators=[validators.Optional()])
  place = StringField('Place',validators=[validators.DataRequired()],widget=TextArea())
  start_datetime = DateTimeField('Start Time',validators=[validators.DataRequired()],format='%Y-%m-%d %H:%M')
  end_datetime =  DateTimeField('End Time',validators=[ validators.DataRequired() ],format='%Y-%m-%d %H:%M')
  description = StringField('Discription',widget=TextArea(),validators=[ validators.Length(min=20) ])
  

  
class CancelEventForm(FlaskForm):
  confirm = StringField("Are you sure you want to cancel?",validators=[validators.DataRequired()])
  
class EditForm(BasicEventForm):
      photo = FileField("Party Photo",validators=[FileAllowed(['jpg','jpeg','png','gif','bmp'],"Only allow .jpg .png .gif files"),validators.Optional()])
    


