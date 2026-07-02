import os
from werkzeug.utils import secure_filename


class DocumentService:

    @staticmethod
    def save_document(file, upload_folder):

        os.makedirs(upload_folder, exist_ok=True)

        filename = secure_filename(file.filename)

        filepath = os.path.join(upload_folder, filename)

        file.save(filepath)

        return filename, filepath