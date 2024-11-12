import reflex as rx

from . import pages

app = rx.App()
app.add_page(pages.home_page, route='/')
app.add_page(pages.about_us, route='/about')
