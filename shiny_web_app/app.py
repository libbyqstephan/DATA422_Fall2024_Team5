from shiny import render, ui
from shiny.express import input

ui.panel_title("Hello Shiny!")
ui.input_slider("n", "N", 0, 100, 20)

ui.input_slider("p", "Please Enter Phone Number", 1111111111, 9999999999, 0)

@render.text
def hi():
    return f"I have no idea what I am doing"
@render.code
def txt():
    s = str(input.p())
    return f"phone number is ({s[0:3]}){s[3:6]}-{s[6:10]}"
