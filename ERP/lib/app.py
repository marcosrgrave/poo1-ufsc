import tkinter as tk
from tkinter import ttk, messagebox

# FUNCTIONS
def filtrar_produto(txt):
    # colocar aqui o codigo pra pesquisar na base de dados
    print(f'O produto "{txt}" foi pesquisado na base de dados.')

def filtrar_fornecedor(txt):
    # colocar aqui o codigo pra pesquisar na base de dados
    print(f'O fornecedor "{txt}" foi pesquisado na base de dados.')

def editar_produto():
    # colocar aqui o codigo pra pesquisar na base de dados
    print(f'O produto foi editado.')

def editar_fornecedor():
    # colocar aqui o codigo pra pesquisar na base de dados
    print(f'O fornecedor foi editado.')

def excluir_produto():
    # colocar aqui o codigo pra pesquisar na base de dados
    print(f'O produto foi excluido.')

def excluir_fornecedor():
    # colocar aqui o codigo pra pesquisar na base de dados
    print(f'O fornecedor foi excluido.')


    ## Popups
        ### showinfo, showwarning, showerror, askquestion or askyesno, askokcancel
def show_popup(master, title, message, popup_type=int):
    '''
    popup_type options: showinfo(1), showwarning(2), showerror(3), askquestion or askyesno(4), askokcancel(5)
    '''
    
    if popup_type   == 1:
        msg_pop = messagebox.showinfo(title=title, message=message)
    elif popup_type == 2:
        msg_pop = messagebox.showwarning(title=title, message=message)
    elif popup_type == 3:
        msg_pop = messagebox.showerror(title=title, message=message)
    elif popup_type == 4:
        msg_pop = messagebox.askquestion(title=title, message=message)
    else:
        msg_pop = messagebox.askokcancel(title=title, message=message)
    
    tk.Label(master, text=msg_pop)


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
        
        # self.style = ttk.Style(self)
        # self.style.theme_use('aqua')
        
        self.geometry(
            f'{self.width}x{self.height}+{int(user_width/2-self.width/2)}+{int(user_height/2-self.height/2)}'
        )

        # FRAMES
        self.bg_color = '#8AE3EC'
        # frame_bg = tk.Frame(self, background=self.bg_color)
        # frame_bg.place(relheight=1, relwidth=1)
        
        window_frame = tk.Frame(self, background=self.bg_color)
        window_frame.place(relheight=1, relwidth=1) # pintando a janela inteira (n afeta as tabs)

        
        # STYLE
        self.style = ttk.Style()
        # self.style.configure(style="TNotebook.Tab", font=("Consolas", 10))
        # self.style.configure(style="TButton", font=('Consolas', 16))


        # NOTEBOOKS (TABS)
        self.tabs = ttk.Notebook(self)
        self.tabs.pack(pady=20, side='top') # pady: desloca, ipady: espessura

        
        tab_dashboard = ttk.Frame(self.tabs)  # tk frame allows 'place' and 'pack'
        tab_entradas = ttk.Frame(self.tabs)
        tab_produtos = ttk.Frame(self.tabs)  # background=self.bg_color (n serve no ttk, apenas no tk)
        tab_fornecedores = ttk.Frame(self.tabs)

        self.tabs.add(tab_dashboard, text='Dashboard')
        self.tabs.add(tab_entradas, text='Entradas e Saídas')
        self.tabs.add(tab_produtos, text='Produtos')
        self.tabs.add(tab_fornecedores, text='Fornecedores')


        # LABELS
        lbl_produto = ttk.Label(tab_produtos, text='NOME PRODUTO')
        lbl_produto.grid(row=2, column=1)

        lbl_qtd_produto = ttk.Label(tab_produtos, text='QTD')
        lbl_qtd_produto.grid(row=2, column=2, rowspan=2)

        lbl_fornecedor_prod = ttk.Label(tab_produtos, text='NOME FORNECEDOR')
        lbl_fornecedor_prod.grid(row=3, column=1)

        lbl_fornecedor_forn = ttk.Label(tab_fornecedores, text='NOME FORNECEDOR')
        lbl_fornecedor_forn.grid(row=2, column=1, rowspan=2, columnspan=3, sticky='w')


        # ENTRIES
        filter_produto = ttk.Entry(tab_produtos, justify='center')  # show='*' -> for password
        filter_produto.insert(0, 'Pesquise o produto aqui')
        filter_produto.grid(row=1, column=1, ipadx=20)

        filter_forn = ttk.Entry(tab_fornecedores, justify='center')  # show='*' -> for password
        filter_forn.insert(0, 'Pesquise o fornecedor aqui')
        filter_forn.grid(row=1, column=1, ipadx=20)


        # BUTTONS
        btn_filtrar_prod = ttk.Button(tab_produtos, text='Filtrar', command=lambda:filtrar_produto(filter_produto.get()))
        btn_filtrar_prod.grid(row=1, column=2)

        btn_filtrar_forn = ttk.Button(tab_fornecedores, text='Filtrar', command=lambda:filtrar_fornecedor(filter_forn.get()))
        btn_filtrar_forn.grid(row=1, column=2)

        btn_editar_produto = ttk.Button(tab_produtos, text='Editar', command=lambda:editar_produto())
        btn_editar_produto.grid(row=2, column=3)

        btn_editar_forn = ttk.Button(tab_fornecedores, text='Editar', command=lambda:editar_fornecedor())
        btn_editar_forn.grid(row=2, column=3)

        btn_exluir_produto = ttk.Button(tab_produtos, text='Excluir', command=lambda:excluir_produto())
        btn_exluir_produto.grid(row=3, column=3)

        btn_exluir_forn = ttk.Button(tab_fornecedores, text='Excluir', command=lambda:excluir_fornecedor())
        btn_exluir_forn.grid(row=3, column=3)

        btn_popup1 = ttk.Button(tab_dashboard, text='show popup', command=lambda:show_popup(self, 'title', 'eat shit', 1))
        btn_popup1.grid()
    


if __name__ == '__main__':
    App().mainloop()