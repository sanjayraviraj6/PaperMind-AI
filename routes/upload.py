import os

from flask import Blueprint
from flask import current_app
from flask import flash
from flask import render_template
from flask import request

from services.document_service import DocumentService
from services.rag_service import RAGService

upload_bp = Blueprint("upload", __name__)


@upload_bp.route("/upload", methods=["GET", "POST"])
def upload():

    extracted_text = ""
    chunks = []

    if request.method == "POST":

        files = request.files.getlist("pdf_files")

        for file in files:

            if file and file.filename:

                filename, filepath = DocumentService.save_document(
                    file,
                    current_app.config["UPLOAD_FOLDER"]
                )

                result = RAGService.process_document(
                    filepath,
                    filename
                )

                extracted_text = result["text"]
                chunks = result["chunks"]

                # Check if the document already exists
                if result["already_exists"]:

                    flash(
                        f"{filename} has already been uploaded.",
                        "warning"
                    )

                else:

                    flash(
                        "Document uploaded successfully!",
                        "success"
                    )

    upload_folder = current_app.config["UPLOAD_FOLDER"]

    uploaded_files = []

    if os.path.exists(upload_folder):

        uploaded_files = sorted(
            [
                file
                for file in os.listdir(upload_folder)
                if file.lower().endswith(".pdf")
            ]
        )

    return render_template(
        "upload.html",
        uploaded_files=uploaded_files,
        extracted_text=extracted_text,
        chunks=chunks
    )