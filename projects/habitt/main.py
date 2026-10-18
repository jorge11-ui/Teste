#como executar o file "Textual"- textual run main.py
from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.color import Color

class Myapp(App):
    def compose(self) -> ComposeResult:
        self.widget1 = Static("ola mundo")
        yield self.widget1
        self.widget2 = Static("ola mundo")
        yield self.widget2
        self.widget3 = Static("ola mundo")
        yield self.widget3 


    def on_mount(self) -> None:
        self.widget1.styles.background = "black"
        self.widget2.styles.background = "lightblue"
        self.widget3.styles.background = "red"
        self.screen.styles.background = "blue"
        self.screen.styles.border = ("heavy", "white")


if __name__ == "__main__":
    app = Myapp()
    app.run()

