import tkinter as tk
from tkinter import ttk

# WINDOW
root = tk.Tk()
root.title('Gerenciador de Estoque - Marcos e Pablo')
root.iconbitmap("ERP/resources/carrinho2.ico")
root.geometry('450x300')


# FUNCTIONS
def filtrar_produto(txt):
    # colocar aqui o codigo pra pesquisar na base de dados
    print(f'{txt} foi pesquisado na base de dados.')


# NOTEBOOKS


# LABELS
lbl_produto = ttk.Label(root, text='NOME PRODUTO')
lbl_produto.grid(row=2, column=1)

lbl_qtd_produto = ttk.Label(root, text='QTD')
lbl_qtd_produto.grid(row=2, column=2)

lbl_fornecedor = ttk.Label(root, text='NOME FORNECEDOR')
lbl_fornecedor.grid(row=3, column=1)


# ENTRIES
filter_produto_input = ttk.Entry(root, justify='center')
filter_produto_input.insert(0, 'Pesquise o produto aqui')
filter_produto_input.grid(row=1, column=1, ipadx=20, )


# POPUPS
## showinfo, showwarning, showerror, askquestion | askyesno, askokcancel

# BUTTONS
btn_filtrar = ttk.Button(root, text='Filtrar', command=lambda:filtrar_produto(filter_produto_input.get()))
btn_filtrar.grid(row=1, column=2)

btn_editar_produto = ttk.Button(root, text='EDITAR')
btn_editar_produto.grid(row=2, column=3)

btn_exluir_produto = ttk.Button(root, text='EXCLUIR')
btn_exluir_produto.grid(row=3, column=3)


# END (LOOP)
tk.mainloop()