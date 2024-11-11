# TODO: use flet*
#       checkboxes for charsets*
#       slidebar for security level
#       
import pyperclip
import random
import flet as ft
import string

letters = string.ascii_letters
numbers = string.digits
punctuations = string.punctuation


def main(page: ft.Page):
    page.title = "Password Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def getKey(e):
        keys = []
        if c1.value == True:
            keys.extend(letters)
        if c2.value == True:
            keys.extend(numbers)
        if c3.value == True:
            keys.extend(punctuations)
        passkey = ""
        for x in range(10):
            passkey += random.choice(keys)
        pyperclip.copy(passkey)
        page.show_dialog(dlg)

    dlg = ft.AlertDialog(
        title=ft.Text("Password copied to clipboard"),
        on_dismiss=lambda e: page.add(ft.Text("copied to clipboard")),
    )
    c1 = ft.Checkbox(label="Numbers", value=True)
    c2 = ft.Checkbox(label="Letters", value=True)
    c3 = ft.Checkbox(label="Punctuations", value=False)
    col0 =  ft.Column(controls = [
        c1, c2, c3
    ])
    col1 = ft.Column(controls = [
        ft.ElevatedButton(text="Get Password",icon=ft.icons.KEY_ROUNDED, on_click=getKey)
    ])

    

    page.add(

        ft.Row(
                controls=[col0,col1],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)