import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

def gen_password():
    """
    Gera uma senha aleatória com letras, números e símbolos.
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list.extend([random.choice(symbols) for _ in range(random.randint(2, 4))])
    password_list.extend([random.choice(numbers) for _ in range(random.randint(2, 4))])

    random.shuffle(password_list)

    password_entry.delete(0, tk.END)
    password = ''.join(password_list)
    password_entry.insert(1, password)
    pyperclip.copy(password)


def save_data():
    """
    Salva os dados preenchidos pelo usuário em um arquivo de texto.
    """
    if len(website_entry.get()) == 0 or len(user_entry.get()) == 0 or len(password_entry.get()) == 0:
        tk.messagebox.showinfo(title="Oops", message="Por favor, preencha todos os campos.")

    else:
        message = tk.messagebox.askokcancel(title=f"{website_entry.get().title()}",
                                            message=f"Email: {user_entry.get()}\n"
                                                    f"Senha: {password_entry.get()}\n"
                                                    f"Deseja Salvar?")
        if message:
            with open("data.txt", mode="a") as file:
                file.write(f"Site: {website_entry.get().title()}\n"
                           f"Usuário | E-mail: {user_entry.get()}\n"
                           f"Senha: {password_entry.get()}\n\n")

            website_entry.delete(0, tk.END)
            user_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


FONT_COLOR = "#FFFFFF"
ENTRY_COLOR = "#2D2D2D"
BACKGROUND = "#222222"

# Cria a janela principal.
root = tk.Tk()
root.title("Gerenciador de Senhas")
root.geometry("350x400")
root.resizable(width=False, height=False)

# Carrega a imagem.
logo = tk.PhotoImage(file="logo.png")

# Cria um canvas e posiciona a imagem.
canvas = tk.Canvas(width=350, height=450, background=BACKGROUND)
canvas.create_image(175, 68, image=logo)
canvas.pack()

# Cria e posiciona o texto "Website".
website_label = tk.Label(text="Website", font=("Century Gothic", 9, "normal"))
website_label.config(background=BACKGROUND, foreground=FONT_COLOR)
website_label.place(x=47, y=127)
# Cria e posiciona a entry para armazenar os sites.
website_entry = tk.Entry(width=35, font=("Century Gothic", 9, "normal"))
website_entry.config(background=ENTRY_COLOR, foreground=FONT_COLOR, relief="flat", insertbackground="#FFFFFF")
website_entry.focus()
website_entry.place(x=50, y=148)

# Cria e posiciona o texto "email".
user_label = tk.Label(text="Email / Usuário", font=("Century Gothic", 9, "normal"))
user_label.config(background=BACKGROUND, foreground=FONT_COLOR)
user_label.place(x=47, y=183)
# Cria e posiciona a entry para armazenar os emails.
user_entry = tk.Entry(width=35, font=("Century Gothic", 9, "normal"))
user_entry.config(background=ENTRY_COLOR, foreground=FONT_COLOR, relief="flat", insertbackground=FONT_COLOR)
user_entry.place(x=50, y=204)

# Cria e posiciona o texto "Senha".
password_label = tk.Label(text="Senha", font=("Century Gothic", 9, "normal"))
password_label.config(background=BACKGROUND, foreground=FONT_COLOR)
password_label.place(x=47, y=239)
# Cria e posiciona a entry para armazenar as senhas.
password_entry = tk.Entry(width=16, font=("Century Gothic", 9, "normal"))
password_entry.config(background=ENTRY_COLOR, foreground=FONT_COLOR, relief="flat", insertbackground=FONT_COLOR)
password_entry.place(x=50, y=260)
# Cria e posiciona o botão para gerar senhas aleatóriamente.
password_button = tk.Button(text="Gerar Senha", width=16, font=("Century Gothic", 8, "bold"), command=gen_password)
password_button.config(background=ENTRY_COLOR, foreground=FONT_COLOR, relief="flat")
password_button.place(x=177, y=258)

# Cria e posiciona o botão para salvar os dados em arquivo de texto.
add_button = tk.Button(text="Salvar", width=34, font=("Century Gothic", 8, "bold"), command=save_data)
add_button.config(background=ENTRY_COLOR, foreground=FONT_COLOR, relief="flat")
add_button.place(x=51, y=302)

# Inicia o loop de eventos.
root.mainloop()