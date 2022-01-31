import tkinter as tk
from tkinter import ttk
from turtle import bgcolor, width

from click import style


# FUNCTIONS
def filtrar_produto(txt):
    # colocar aqui o codigo pra pesquisar na base de dados
    print(f'{txt} foi pesquisado na base de dados.')


# WINDOW
class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        # WINDOW
        self.title('Gerenciador de Estoque - Marcos e Pablo')
        self.iconbitmap("ERP/resources/carrinho2.ico")
        
        user_width = self.winfo_screenwidth()
        user_height = self.winfo_screenheight()

        self.width = 800
        self.height = 600
        
        self.geometry(
            f'{self.width}x{self.height}+{int(user_width/2-self.width/2)}+{int(user_height/2-self.height/2)}'
        )

        # FRAMES
        self.bg_color = '#8AE3EC'
        frame_bg = tk.Frame(self, background=self.bg_color)
        frame_bg.place(relheight=1, relwidth=1)
        
        frame_produto = tk.Frame(self, background=self.bg_color)
        # frame_produto.grid(padx=100, pady=100)
        frame_produto.place(x=self.width/2, y=self.height/2, anchor=tk.CENTER, ) #, relx=.1, rely=.1)

        
        # STYLE
        self.style = ttk.Style()
        # self.style.configure(style="TNotebook.Tab", font=("Consolas", 10))
        # self.style.configure(style="TButton", font=('Consolas', 16))


        # NOTEBOOKS
        self.tabs = ttk.Notebook(self)
        self.tabs.pack(pady=20, side='top') # pady: desloca, ipady: espessura

        
        tab_dashboard = tk.Frame(self.tabs)
        tab_in_and_out = tk.Frame(self.tabs)
        tab_produtos = tk.Frame(self.tabs, background=self.bg_color)
        tab_fornecedores = tk.Frame(self.tabs)

        self.tabs.add(tab_dashboard, text='Dashboard')
        self.tabs.add(tab_in_and_out, text='Entradas e Saídas')
        self.tabs.add(tab_produtos, text='Produtos')
        self.tabs.add(tab_fornecedores, text='Fornecedores')


        # LABELS
        lbl_produto = ttk.Label(tab_produtos, text='NOME PRODUTO')
        lbl_produto.grid(row=2, column=1)

        lbl_qtd_produto = ttk.Label(tab_produtos, text='QTD')
        # lbl_qtd_produto.grid(row=2, column=2)

        lbl_fornecedor = ttk.Label(frame_produto, text='NOME FORNECEDOR')
        lbl_fornecedor.grid(row=3, column=1)


        # ENTRIES
        filter_produto_input = ttk.Entry(frame_produto, justify='center')
        filter_produto_input.insert(0, 'Pesquise o produto aqui')
        filter_produto_input.grid(row=1, column=1, ipadx=20, )


        # POPUPS
        ## showinfo, showwarning, showerror, askquestion | askyesno, askokcancel

        # BUTTONS
        btn_filtrar = ttk.Button(frame_produto, text='Filtrar', command=lambda:filtrar_produto(filter_produto_input.get()))
        btn_filtrar.grid(row=1, column=2)

        btn_editar_produto = ttk.Button(frame_produto, text='EDITAR')
        btn_editar_produto.grid(row=2, column=3)

        btn_exluir_produto = ttk.Button(frame_produto, text='EXCLUIR')
        btn_exluir_produto.grid(row=3, column=3)
    


if __name__ == '__main__':
    App().mainloop()