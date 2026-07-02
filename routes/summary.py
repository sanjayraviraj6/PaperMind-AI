from flask import Blueprint
from flask import render_template
from flask import request
from flask import send_file

import io
import markdown

from services.summary_service import SummaryService
from services.pdf_report_service import PDFReportService

summary_bp = Blueprint("summary", __name__)

latest_summary = ""


@summary_bp.route("/summary", methods=["GET", "POST"])
def summary():

    global latest_summary

    report = None

    if request.method == "POST":

        latest_summary = SummaryService.generate()

        report = markdown.markdown(
            latest_summary,
            extensions=["extra"]
        )

    return render_template(
        "summary.html",
        report=report
    )


@summary_bp.route("/download-report")
def download_report():

    global latest_summary

    pdf = PDFReportService.generate(
        latest_summary
    )

    return send_file(

        io.BytesIO(pdf),

        as_attachment=True,

        download_name="PaperMind_AI_Report.pdf",

        mimetype="application/pdf"
    )