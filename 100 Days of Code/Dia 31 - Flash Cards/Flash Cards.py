import tkinter as tk
import pandas as pd
import random

# Tenta ler o arquivo "words_To_Learn.csv.
try:
    df = pd.read_csv("Data/Words_To_Learn.csv")
# Caso o arquivo não seja encontrado o programa vai ler o arquivo "French_Words.csv.
except FileNotFoundError:
    df = pd.read_csv("Data/French_Words.csv")
# Finaliza convertendo os dados do dataframe em um dicionário e escolhe uma palavra aleatória para aprender.
finally:
    to_learn = df.to_dict(orient="records")
    word = random.choice(to_learn)

def next_word():
    """
    Seleciona uma palavra aleatória do arquivo "French_Words.csv", exibe a palavra em francês e configura o temporizador
    para exibir a tradução em português após 3 segundos.
    """
    global word, timer
    root.after_cancel(timer)

    if len(to_learn) == 0:
        right_button.config(state="disabled")
        wrong_button.config(state="disabled")

    word = random.choice(to_learn)

    canvas.itemconfig(card_language, text="Francês")
    canvas.itemconfig(card_word, text=word["Francês"].title())

    timer = root.after(3000, show_translate)

def show_translate():
    """
    Exibe a tradução da palavra selecionada aleatóriamente.
    """
    canvas.itemconfig(card_language, text="Português")
    canvas.itemconfig(card_word, text=word["Português"].title())

def right():
    """
    Adiciona a palavra selecionada atual à lista de palavras aprendidas, salva essa lista em um arquivo .CSV. Remove a
    palavra da lista de palavras para aprender e salva essa lista em um arquivo .CSV. Em seguida chama a função
    "new_word" para selecionar e exibir uma nova palavra.
    """
    try:
        learned_data = pd.read_csv("Data/Learned_Words.csv")
    except FileNotFoundError:
        learned_data = pd.DataFrame(columns=["Francês", "Português"])
        learned_data.to_csv("Data/Learned_Words.csv", index=False)

        learned_data = pd.read_csv("Data/Learned_Words.csv")

    new_learned_data = pd.DataFrame(word, index=[len(learned_data)])
    learned_data = pd.concat([learned_data, new_learned_data], ignore_index=True)
    learned_data.to_csv("Data/Learned_Words.csv", index=False)

    to_learn.remove(word)

    to_learn_data = pd.DataFrame(to_learn)
    to_learn_data.to_csv("Data/Words_To_Learn.csv")

    next_word()


BACKGROUND = "#800000"
LANGUAGE_COLOR = "#BFB5A8"
WORD_COLOR = "#505050"

# Cria a janela principal.
root = tk.Tk()
root.title("Flash Cards")
root.geometry("450x450")
root.resizable(width=False, height=False)

# Carrega a imagem da carta e dos botões.
card_img = tk.PhotoImage(file="Images/Card.png")
right_img = tk.PhotoImage(file="Images/Right_Button.png")
wrong_img = tk.PhotoImage(file="Images/Wrong_Button.png")

# Criação de canvas para desenhar a interface.
canvas = tk.Canvas(width=450, height=450)
canvas.config(background=BACKGROUND)
canvas.create_image(224, 188, image=card_img)
canvas.pack()

# Temporizador para exibir a tradução após 3 segundos.
timer = root.after(3000, show_translate)

# Cria os elementos de texto da interface.
card_language = canvas.create_text(224, 121, text="Francês", font=("Century Gothic", 16, "normal"), fill=LANGUAGE_COLOR)
card_word = canvas.create_text(224, 186, text=word["Francês"].title(), font=("Century Gothic", 20, "normal"),
                               fill=WORD_COLOR)

# Cria e posiciona o botão "correto".
right_button = tk.Button(image=right_img, background=BACKGROUND, activebackground=BACKGROUND, relief="flat",
                         command=right)

right_button.place(x=106, y=330)
# Cria e posiciona o botão "errado".
wrong_button = tk.Button(image=wrong_img, background=BACKGROUND, activebackground=BACKGROUND, relief="flat",
                         command=next_word)

wrong_button.place(x=242, y=330)

# Exibindo a primeira palavra
next_word()
# Inicia o loop de eventos.
root.mainloop()