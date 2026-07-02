from flask import Blueprint
from flask import render_template
from flask import request

from services.summary_service import SummaryService

summary_bp = Blueprint("summary", __name__)


@summary_bp.route("/summary", methods=["GET", "POST"])
def summary():

    summary = ""

    if request.method == "POST":

        summary = SummaryService.generate()

    return render_template(
        "summary.html",
        summary=summary
    )