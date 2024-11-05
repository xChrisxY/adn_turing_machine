import tkinter as tk
from tkinter import ttk
from turing_machine import encontrar_patron

def check_tapes(patterns, dna_sequence, result_frame):
    for pattern in patterns:
        accepted = encontrar_patron(dna_sequence, pattern)

        row = len(result_frame.grid_slaves()) // 2 + 1
        bg_color = "#A7F3D0" if accepted else "#FECACA"

        tk.Label(result_frame, text=pattern, font=('Arial', 10), bg=bg_color, width=25, relief="solid").grid(
            row=row, column=0, padx=5, pady=2)

        result_text = "ACEPTADO" if accepted else "RECHAZADO"
        tk.Label(result_frame, text=result_text, font=('Arial', 10), bg=bg_color, width=25, relief="solid").grid(
            row=row, column=1, padx=5, pady=2)

    patterns.clear()

def create_interface():
    root = tk.Tk()
    root.title("Simulación de Máquina de Turing - Patrón de ADN")
    root.geometry("600x600")
    root.configure(bg="#1E293B")

    patterns = []
    dna_sequence = ""

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font=("Arial", 12), padding=6)
    style.configure("TEntry", font=("Arial", 12), padding=5)

    title_label = tk.Label(root, text="Máquina de Turing", font=("Arial", 20, "bold"), bg="#1E293B", fg="#F1F5F9")
    title_label.pack(pady=10)

    entry_adn = tk.StringVar()
    entry_field = ttk.Entry(root, textvariable=entry_adn, width=40)
    entry_field.pack(pady=10)
    entry_field.insert(0, "Introduce la secuencia de ADN")

    entry_var = tk.StringVar()
    pattern_field = ttk.Entry(root, textvariable=entry_var, width=40)
    pattern_field.pack(pady=10)
    pattern_field.insert(0, "Introduce un patrón de ADN")

    button_frame = tk.Frame(root, bg="#1E293B")
    button_frame.pack(pady=5)

    def save_adn():
        nonlocal dna_sequence
        dna_sequence = entry_adn.get()
        if dna_sequence:
            print(f"Secuencia de ADN guardada: {dna_sequence}")

    def add_entry():
        pattern = entry_var.get()
        if pattern:
            patterns.append(pattern)
            entry_var.set("")
            print(f"Patrón agregado: {pattern}")

    add_button = ttk.Button(button_frame, text="Secuencia de ADN", command=save_adn)
    add_button.grid(row=0, column=0, padx=5)

    add_pattern_button = ttk.Button(button_frame, text="Agregar Patrón", command=add_entry)
    add_pattern_button.grid(row=0, column=1, padx=5)

    check_button = ttk.Button(button_frame, text="Validar Cadenas", command=lambda: check_tapes(patterns, dna_sequence, result_frame))
    check_button.grid(row=0, column=2, padx=5)

    result_frame = tk.Frame(root, bg="#1E293B")
    result_frame.pack(pady=20)

    tk.Label(result_frame, text="Patrón", font=('Arial', 12, 'bold'), width=25, bg="#374151", fg="#F1F5F9", relief="solid").grid(
        row=0, column=0, padx=5, pady=5)
    tk.Label(result_frame, text="Resultado", font=('Arial', 12, 'bold'), width=25, bg="#374151", fg="#F1F5F9", relief="solid").grid(
        row=0, column=1, padx=5, pady=5)

    root.mainloop()
