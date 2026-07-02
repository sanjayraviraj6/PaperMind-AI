from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField


class UploadForm(FlaskForm):

    pdf_files = FileField(
        "Upload PDF",
        validators=[
            FileAllowed(["pdf"], "Only PDF files are allowed.")
        ]
    )

    submit = SubmitField("Upload")