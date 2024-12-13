import reflex as rx

from . import pages, chat, navigation

app = rx.App()
app.add_page(pages.home_page, route=navigation.routes.HOME_ROUTE)
app.add_page(chat.chat_page, route=navigation.routes.CHAT_ROUTE, on_load=chat.state.ChatState.on_load)