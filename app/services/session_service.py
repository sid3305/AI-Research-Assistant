from flask import session


class SessionService:

    @staticmethod
    def set_value(key, value):
        session[key] = value

    @staticmethod
    def get_value(key, default=None):
        return session.get(key, default)

    @staticmethod
    def remove_value(key):
        session.pop(key, None)

    @staticmethod
    def clear_session():
        session.clear()

    @staticmethod
    def get_current_document():
        return session.get("current_document")
    
    @staticmethod
    def get_chat_history():
        return session.get("chat_history", [])


    @staticmethod
    def add_chat_message(question, answer):

        history = session.get(
            "chat_history",
            []
        )

        history.append(
            {
                "question": question,
                "answer": answer
            }
        )

        session["chat_history"] = history

    @staticmethod
    def set_document_chunks(chunks):

        session["document_chunks"] = chunks


    @staticmethod
    def get_document_chunks():

        return session.get(
            "document_chunks",
            []
        )