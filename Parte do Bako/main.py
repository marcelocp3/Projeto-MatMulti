# main.py
import math
import numpy as np
import streamlit as st
import os
import atexit
from Curva import Curva

st.title('CurvaCalculator')

# Parâmetros para a curva específica
# x(t) = 8 * np.cos(t) - 5 * np.cos(8 * t / 3)
# y(t) = 8 * np.sin(t) - 5 * np.sin(8 * t / 3)

# Definindo parametrização em X
def funcX(t: float) -> float:
    return 8 * np.cos(t) - 5 * np.cos(8 * t / 3)

# Definindo parametrização em Y
def funcY(t: float) -> float:
    return 8 * np.sin(t) - 5 * np.sin(8 * t / 3)

# Parâmetros de intervalo
start = 0
end = 2 * np.pi
interval = 0.01

def main(curva):
    curva.run()

def delete_image():
    if os.path.exists('static\curva_plot.png'):
        os.remove('static\curva_plot.png')

atexit.register(delete_image)

if __name__ == '__main__':
    # Gerando a curva com os parâmetros definidos
    curva = Curva(list_t=np.arange(start, end, interval), funcX=funcX, funcY=funcY)
    main(curva=curva)
    st.image('static\curva_plot.png', caption='Curva')
