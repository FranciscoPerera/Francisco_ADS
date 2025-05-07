from dearpygui.core import *
from dearpygui.simple import *

def ao_clicar():
    set_value("label", "Você clicou!")

with window("Exemplo Dear PyGui"):
    add_text("Olá, mundo!", source="label")
    add_button("Clique aqui", callback=ao_clicar)

start_dearpygui()
