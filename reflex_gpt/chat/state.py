from typing import List
import reflex as rx
from . import ai 
from reflex_gpt.models import ChatSession, ChatSessionMessageModel

class ChatMessage(rx.Base):
    message: str
    is_bot: bool = False


class ChatState(rx.State):
    chat_session: ChatSession = None
    did_submit: bool = False
    messages: List[ChatMessage] = []

    @rx.var
    def user_did_submit(self) -> bool:
        return self.did_submit
    
    def on_load(self):
        print("running onload")
        if self.chat_session is None:
            with rx.session() as db_session:
                obj = ChatSession()
                db_session.add(obj)
                db_session.commit()
                db_session.refresh(obj)
                self.chat_session = obj

    def insert_message_to_db(self, content, role='unknown'):
        print("insert data to db")
        if self.chat_session is None:
            return
        if not isinstance(self.chat_session, ChatSession):
            return
        with rx.session() as db_session:
            data = {
                "session_id": self.chat_session.id,
                "content": content,
                "role": role,
            }
            obj = ChatSessionMessageModel(**data)
            db_session.add(obj)
            db_session.commit()

    
    def append_message(self, message, is_bot:bool=False):
        if self.chat_session is not None:
            print(self.chat_session.id)
        self.messages.append(
                ChatMessage(
                    message=message,
                    is_bot=is_bot
                )
            )
        
    def get_gpt_messages(self):
        gpt_messages = [
            {
                "role": "system",
                "content": "expert cheto tam"
            }
        ]
        for chat_message in self.messages:
            role = 'user'
            if chat_message.is_bot:
                role = 'system'
            gpt_messages.append({
                "role": role,
                "content": chat_message.message
            })
        return gpt_messages

    async def handle_submit(self, form_data:dict):
        print(form_data)
        user_message = form_data.get('message')
        if user_message:
            self.did_submit = True
            self.append_message(user_message, is_bot=False)
            self.insert_message_to_db(user_message, role='user')
            yield
            gpt_messages = self.get_gpt_messages()
            print(gpt_messages)
            bot_response = ai.get_llm_response(gpt_messages)
            self.did_submit = False
            self.append_message(bot_response, is_bot=True)
            self.insert_message_to_db(bot_response, role='system')
            yield  