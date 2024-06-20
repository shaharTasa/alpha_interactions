from draws.header import draw_header
from draws.input_receiver import draw_input_receiver
from draws.output_protein_data import draw_output_data

def draw_app():
    draw_header()
    input_file = draw_input_receiver()
    if input_file != None:
        draw_output_data(input_file)
