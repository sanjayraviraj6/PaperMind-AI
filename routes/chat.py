from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for

from services.chat_service import ChatService

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/chat", methods=["GET", "POST"])
def chat():

    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":

        question = request.form["question"]

        answer = ChatService.ask(question)

        history = session["chat_history"]

        history.append(
            {
                "question": question,
                "answer": answer
            }
        )

        session["chat_history"] = history

    return render_template(
        "chat.html",
        history=session["chat_history"]
    )


@chat_bp.route("/clear_chat")
def clear_chat():

    session.pop("chat_history", None)

    return redirect(url_for("chat.chat"))