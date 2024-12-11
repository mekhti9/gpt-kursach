"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from reflex_gpt import ui, navigation


def home_page() -> rx.Component:
    # Welcome Page (Index)
    return ui.base_layout(
        rx.vstack(
            rx.heading("Chat Pluto", size="9"),
            rx.text(
                "Ask about anything",
                size="5",
            ),
            rx.link(
                rx.button("Start Chat", on_click=navigation.state.NavState.to_chat),
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )

