import tkinter as tk
import math

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
timer = ""
reps = 0

def start_timer():
    """
    Inicia um cronômetro baseado no número de repetições.

    A cada 8 repetições, o cronômetro será configurado para um "long break" de 15 minutos.
    A cada 2 repetições, o cronômetro será configurado para um "short break" de 5 minutos.
    Em outros casos será configurado para "work" de 25 minutos.
    """
    global reps
    reps += 1

    if reps % 8 == 0:
        canvas.itemconfig(pomodoro_text, text="Pausa Longa")
        at_timer(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        canvas.itemconfig(pomodoro_text, text="Pausa Curta")
        at_timer(SHORT_BREAK_MIN * 60)
    else:
        canvas.itemconfig(pomodoro_text, text="Foco")
        at_timer(WORK_MIN * 60)

def at_timer(count):
    """
    Atualiza a exibição do cronômetro no canvas com o tempo restante atual.
    :param count: Número de segundos restantes no cronômetro.
    """
    minutes = math.floor(int(count) / 60)
    seconds = int(count) % 60

    canvas.itemconfig(timer_text, text=f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

    if count > 0:
        global timer, reps

        reset_button.config(state="normal")
        start_button.config(state="disabled")

        timer = root.after(1000, at_timer, count - 1)
    else:
        start_timer()

        if reps == 9:
            reps = 0
            check_marks.config(text="")

        check_marks.config(text=CHECK_MARK * math.floor(reps / 2))


def reset_timer():
    """
    Reinicia o cronômetro, definindo o número de repetições (reps) para 0 e habilitando o botão iniciar.
    Ela desabilita o botão "reset" e altera o texto do canvas para o padrão inicial e
    limpa as marcas de verificação.
    Também cancela o cronômetro se estiver em execução.

    """
    global reps

    reps = 0
    start_button.config(state="normal")
    reset_button.config(state="disabled")

    canvas.itemconfig(pomodoro_text, text="Pomodoro")
    canvas.itemconfig(timer_text, text="25:00")
    check_marks.config(text="")

    root.after_cancel(timer)


BACKGROUND = "#B12025"
CIRCLE_OUTLINE = "#961C22"
CIRCLE_FILL = "#A31F25"
FONT_COLOR = "#FFFFFF"
BUTTON_COLOR = "#F5F5F5"
CHECK_MARK = "✔"
CHECK_MARK_COLOR = "#228B22"

# Cria a janela principal.
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("270x420")
root.config(bg=BACKGROUND)
root.resizable(width=False, height=False)

# Carrega a imagem.
lines_img = tk.PhotoImage(file="lines.png")

# Cria um canvas.
canvas = tk.Canvas(width=270, height=420, background=BACKGROUND)
# Cria o texto "Pomodoro", um círculo, o texto inicial "25:00" e adiciona imagem "lines.img"
pomodoro_text = canvas.create_text(135, 35, text="Pomodoro", font=("Century Gothic", 17, "normal"), fill=FONT_COLOR)
circle = canvas.create_oval(35, 70, 235, 270, outline=CIRCLE_OUTLINE, fill=CIRCLE_FILL, width=5)
timer_text = canvas.create_text(135, 168, text="25:00", font=("Century Gothic", 35, "normal"), fill=FONT_COLOR)
canvas.create_image(135, 309, image=lines_img)
canvas.pack()

# Cria o botão para iniciar o cronômetro.
start_button = tk.Button(text="Iniciar", font=("Century Gothic", 8, "bold"), relief="raised", command=start_timer)
start_button.config(width=8, background="#961C22", relief="flat", foreground="#FFFFFF")
start_button.place(x=52, y=350)

# Cria o botão para reiniciar o cronômetro.
reset_button = tk.Button(text="Reiniciar", font=("Century Gothic", 8, "bold"), relief="raised", state="disabled",
                         command=reset_timer)
reset_button.config(width=8, background="#961C22", relief="flat", foreground="#FFFFFF")
reset_button.place(x=153, y=350)

# Cria a label com as check marks.
check_marks = tk.Label(background=CIRCLE_FILL, foreground=CHECK_MARK_COLOR)
check_marks.place(x=109, y=193)

# Inicia o loop de eventos.
root.mainloop()