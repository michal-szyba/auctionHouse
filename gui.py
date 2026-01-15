import tkinter as tk
from tkinter import ttk, messagebox



def search_items(query: str):
    # TODO: GET /search?q=query
    return [
        {"id": "1", "name": "Iron sword", "price": 2500},
        {"id": "2", "name": "Steel boots", "price": 2200},
    ]


def buy_item(item_id: str):
    # TODO: POST /buy
    messagebox.showinfo("Zakup", f"Kupiono przedmiot {item_id}")


def create_auction(name, price, increment):
    # TODO: POST /create-auction
    messagebox.showinfo(
        "Aukcja",
        f"Wystawiono: {name}, cena {price}, przebitka {increment}"
    )


# ---------------- UI ----------------

class AuctionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aukcje")
        self.geometry("700x500")

        self.create_search_bar()
        self.create_results_list()
        self.create_sell_panel()

    # ---------- SEARCH ----------
    def create_search_bar(self):
        frame = ttk.Frame(self)
        frame.pack(fill="x", padx=10, pady=10)

        self.search_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.search_var, width=40).pack(side="left", padx=5)
        ttk.Button(frame, text="Szukaj", command=self.search).pack(side="left")

    def search(self):
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        items = search_items(self.search_var.get())
        for item in items:
            self.add_result_row(item)

    # ---------- RESULTS ----------
    def create_results_list(self):
        container = ttk.LabelFrame(self, text="Wyniki wyszukiwania")
        container.pack(fill="both", expand=True, padx=10, pady=10)

        self.results_frame = ttk.Frame(container)
        self.results_frame.pack(fill="both", expand=True)

    def add_result_row(self, item):
        row = ttk.Frame(self.results_frame)
        row.pack(fill="x", pady=2)

        ttk.Label(row, text=item["name"], width=30).pack(side="left")
        ttk.Label(row, text=f"{item['price']} gold", width=15).pack(side="left")
        ttk.Button(
            row,
            text="Kup",
            command=lambda: buy_item(item["id"])
        ).pack(side="right")

    # ---------- SELL ----------
    def create_sell_panel(self):
        frame = ttk.LabelFrame(self, text="Wystaw nową aukcję")
        frame.pack(fill="x", padx=10, pady=10)

        self.sell_name = tk.StringVar()
        self.sell_price = tk.StringVar()
        self.sell_increment = tk.StringVar()

        ttk.Label(frame, text="Nazwa").grid(row=0, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.sell_name).grid(row=0, column=1)

        ttk.Label(frame, text="Cena startowa").grid(row=1, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.sell_price).grid(row=1, column=1)

        ttk.Label(frame, text="Min. przebitka").grid(row=2, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.sell_increment).grid(row=2, column=1)

        ttk.Button(
            frame,
            text="Wystaw",
            command=self.submit_auction
        ).grid(row=3, column=0, columnspan=2, pady=5)

    def submit_auction(self):
        create_auction(
            self.sell_name.get(),
            self.sell_price.get(),
            self.sell_increment.get()
        )

if __name__ == "__main__":
    app = AuctionApp()
    app.mainloop()
