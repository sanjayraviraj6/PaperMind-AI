from flask import Blueprint
from flask import render_template
from flask import request
from flask import session

from services.chat_service import ChatService

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/chat", methods=["GET", "POST"])
def chat():

    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":

        question = request.form.get("question")

        answer = ChatService.ask(question)

        history = session["chat_history"]

        history.append({
            "role": "user",
            "content": question
        })

        history.append({
            "role": "assistant",
            "content": answer
        })

        session["chat_history"] = history

    return render_template(
        "chat.html",
        chat_history=session["chat_history"]
    )