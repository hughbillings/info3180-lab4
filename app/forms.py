from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_wtf import FlaskForm






class UploadForm(FlaskForm):
    file = FileField('Form',validators=[FileRequired(),FileAllowed(['jpg','png'])])
    
