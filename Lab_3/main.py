import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Goods manager")

# Змінні для введення
var_name = tk.StringVar()
var_price = tk.IntVar()
var_status = tk.StringVar()

# --- Фрейм для таблиці ---
frame_tree = tk.LabelFrame(root, text="List of goods")
frame_tree.pack(padx=10, pady=5, fill="both", expand=True)

# --- Скролбар для таблиці ---
scrollbar = tk.Scrollbar(frame_tree, orient="vertical")
scrollbar.pack(side="right", fill="y")

# --- Таблиця (Treeview) ---
tree = ttk.Treeview(
    frame_tree,
    columns=("name", "price", "status"),
    show="headings",
    selectmode="browse",
    height=10,
    yscrollcommand=scrollbar.set
)

# Заголовки стовпців
tree.heading("name", text="Title", anchor="w")
tree.heading("price", text="Price", anchor="w")
tree.heading("status", text="Status", anchor="w")

# Визначення ширини стовпців
tree.column("name", width=300, anchor="w", stretch=True)
tree.column("price", width=100, anchor="center", stretch=False)
tree.column("status", width=80, anchor="center", stretch=False)

tree.pack(fill="both", expand=True)
scrollbar.config(command=tree.yview)

# --- Додавання початкових товарів ---
items = [
    ("Smartphone", 12000, "Availbable"),
    ("Laptop", 35000, "Not available"),
    ("Планшет", 15000, "Availbable"),
    ("Навушники", 4000, "Availbable"),
    ("Клавіатура", 2000, "Not available"),
    ("Миша", 1500, "Availbable"),
    ("Монітор", 18000, "Availbable"),
    ("Принтер", 9000, "Not available"),
    ("Колонки", 7000, "Availbable"),
    ("Флешка", 800, "Availbable")
]

for item in items:
    tree.insert("", "end", values=item)

tree.selection_set(tree.get_children()[0])  # Виділити перший елемент

# --- Фрейм для введення нових даних ---
labelframe_entry = tk.LabelFrame(root, text="Add / Edit")
labelframe_entry.pack(padx=10, pady=5, fill="x")

# Поле введення назви товару
entry_name = tk.Entry(labelframe_entry, textvariable=var_name, width=40)
entry_name.pack(pady=2)

# Слайдер для вибору ціни
scale_price = tk.Scale(
    labelframe_entry,
    variable=var_price,
    from_=0,
    to=50000,
    tickinterval=10000,
    resolution=500,
    orient="horizontal"
)
scale_price.pack(pady=2, fill="x")

# Комбобокс для вибору статусу
combo_status = ttk.Combobox(
    labelframe_entry,
    textvariable=var_status,
    values=("Availbable", "Not available"),
    state="readonly"
)
combo_status.pack(pady=2)
combo_status.current(0)

# --- Фрейм для кнопок ---
labelframe_button = tk.LabelFrame(root, text="Operations")
labelframe_button.pack(padx=10, pady=5, fill="x")

# Функція додавання товару
def handle_insert():
    name = var_name.get()
    price = var_price.get()
    status = var_status.get()
    if name.strip() == "":
        return
    tree.insert("", "end", values=(name, price, status))
    var_name.set("")
    var_price.set(0)
    var_status.set("Availbable")

button_insert = tk.Button(labelframe_button, text="Add", command=handle_insert)
button_insert.pack(side="left", padx=5, pady=2)

# Функція видалення товару
def handle_delete():
    selection = tree.selection()
    if not selection:
        return
    tree.delete(selection[0])

button_delete = tk.Button(labelframe_button, text="Delete", command=handle_delete)
button_delete.pack(side="left", padx=5, pady=2)

# Функція отримання вибраного товару
def handle_get_item():
    selection = tree.selection()
    if not selection:
        return
    values = tree.item(selection[0]).get("values")
    var_name.set(values[0])
    var_price.set(values[1])
    var_status.set(values[2])

button_get = tk.Button(labelframe_button, text="Get", command=handle_get_item)
button_get.pack(side="left", padx=5, pady=2)

# Функція редагування вибраного товару
def handle_set():
    selection = tree.selection()
    name = var_name.get()
    price = var_price.get()
    status = var_status.get()
    if name.strip() == "" or not selection:
        return
    tree.item(selection[0], values=(name, price, status))
    var_name.set("")
    var_price.set(0)
    var_status.set("Availbable")

button_set = tk.Button(labelframe_button, text="Edit", command=handle_set)
button_set.pack(side="left", padx=5, pady=2)

root.mainloop()
