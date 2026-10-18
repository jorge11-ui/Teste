import flet as ft


def main(page: ft.Page):
  page.add(ft.Text("Olá, Flet!", size=30, weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE))



ft.run(main)

