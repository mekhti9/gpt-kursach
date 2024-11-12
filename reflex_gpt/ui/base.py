import reflex as rx

from .navbar import base_navbar
from .footer import base_footer

def base_layout(*arg, **kwargs) -> rx.Component:
    return rx.container(
        base_navbar(),
        rx.fragment(*arg, **kwargs,),
        base_footer()
    )