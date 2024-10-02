# Este arquivo de entrada é usado em desenvolvimento. Comece lendo o README.md
import time_series_visualizer
from unittest import main

# Testa as funções chamando-as aqui
time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
time_series_visualizer.draw_box_plot()

# Executa os testes unitários automaticamente
main(module='test_module', exit=False)