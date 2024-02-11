import tkinter as tk

def convertion():
    """
    Converte uma distância em milhas para quilômetros.
    A distância em milhas é lida a partir de uma entrada do usuário e é convertida para quilômetros usando a fórmula
    1 milha = 1.60934 quilômetros.
    O resultado é exibido em um widget de texto específico "km_result".
    """
    km_result.config(text=float(mile_entry.get()) * 1.60934)


# Define a cor do fundo e da fonte.
BACKGROUND = "#1F1F1F"
FONT_COLOR = "#FFFFFF"

# Cria a janela principal.
root = tk.Tk()
root.title("Conversor de Milha para Quilômetro")
root.config(background=BACKGROUND, padx=25, pady=25)
root.geometry("400x141")
root.resizable(width=False, height=False)

# Cria o texto "Milha".
mile_text = tk.Label(text="Milha", font=("Century Gothic", 9, "normal"))
mile_text.config(background=BACKGROUND, foreground=FONT_COLOR)
mile_text.place(x=42, y=6)

# Cria o texto "Quilômetro".
km_text = tk.Label(text="Quilômetro", font=("Century Gothic", 9, "normal"))
km_text.config(background=BACKGROUND, foreground=FONT_COLOR)
km_text.place(x=188, y=6)

# Cria o texto "=".
equal_label = tk.Label(text="=", font=("Century Gothic", 15, "normal"))
equal_label.config(background=BACKGROUND, foreground=FONT_COLOR)
equal_label.place(x=166, y=24)

# Cria um campo de entrada para as milhas.
mile_entry = tk.Entry(justify="center", font=("Century Gothic", 15, "normal"))
mile_entry.config(width=10, background=BACKGROUND, foreground=FONT_COLOR, insertbackground=FONT_COLOR)
mile_entry.focus()
mile_entry.place(x=45, y=25)

# Cria o campo para mostrar o resultado da conversão.
km_result = tk.Label(text="", font=("Century Gothic", 15, "normal"), bd=1)
km_result.config(width=9, background=BACKGROUND, foreground=FONT_COLOR, relief="sunken")
km_result.place(x=191, y=25)

# Cria o botão para calcular a conversão.
calculate_button = tk.Button(text="Calcular", font=("Century Gothic", 8, "bold"), command=convertion)
calculate_button.config(background=BACKGROUND, foreground=FONT_COLOR, relief="ridge")
calculate_button.place(x=147, y=64)

# Inicia o loop de eventos.
root.mainloop()