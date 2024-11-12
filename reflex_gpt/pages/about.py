"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from reflex_gpt import ui


def about_us() -> rx.Component:
    # about us page
    return ui.base_layout(
        rx.vstack(
            rx.heading("Welcome to Reflex about!", 
            size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

