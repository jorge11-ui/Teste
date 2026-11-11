import reflex as rx

class State(rx.State):
    pass

def index():
    return rx.center()

app = rx.App()
app.add_page(index)
