from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph


class PDFReportService:

    @staticmethod
    def generate(summary):

        buffer = BytesIO()

        doc = SimpleDocTemplate(buffer)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "<b>PaperMind AI Research Report</b>",
                styles["Title"]
            )
        )

        story.append(
            Paragraph("<br/>", styles["Normal"])
        )

        for line in summary.split("\n"):

            if line.strip():

                story.append(
                    Paragraph(line, styles["BodyText"])
                )

        doc.build(story)

        pdf = buffer.getvalue()

        buffer.close()

        return pdf