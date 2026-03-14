import tkinter as tk
from tkinter import ttk, messagebox
from view import *

import matplotlib.pyplot as plt
import pandas as pd


# =========================
# Janela
# =========================

janela = tk.Tk()
janela.title("Controle Financeiro")
janela.geometry("900x600")
janela.configure(bg="#f5f6fa")


# =========================
# Funções
# =========================

def atualizar_dashboard():

    receitas = ver_receitas()
    gastos = ver_gastos()

    total_receitas = sum([r[3] for r in receitas])
    total_gastos = sum([g[3] for g in gastos])

    saldo = total_receitas - total_gastos

    label_receitas["text"] = f"Receitas: R$ {total_receitas:.2f}"
    label_gastos["text"] = f"Gastos: R$ {total_gastos:.2f}"
    label_saldo["text"] = f"Saldo: R$ {saldo:.2f}"


def atualizar_tabela():

    tabela.delete(*tabela.get_children())

    receitas = ver_receitas()
    gastos = ver_gastos()

    for r in receitas:
        tabela.insert("", "end", values=("Receita", r[0], r[1], r[2], r[3]))

    for g in gastos:
        tabela.insert("", "end", values=("Gasto", g[0], g[1], g[2], g[3]))

    atualizar_dashboard()


def limpar_campos():

    entrada_categoria.set("")
    entrada_data.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)


def adicionar_receita():

    categoria = entrada_categoria.get()
    data = entrada_data.get()
    valor = entrada_valor.get()

    if categoria == "" or valor == "":
        messagebox.showerror("Erro", "Preencha os campos")
        return

    try:
        valor = float(valor)
    except:
        messagebox.showerror("Erro", "Valor inválido")
        return

    inserir_receitas((categoria, data, valor))

    atualizar_tabela()
    limpar_campos()


def adicionar_gasto():

    categoria = entrada_categoria.get()
    data = entrada_data.get()
    valor = entrada_valor.get()

    if categoria == "" or valor == "":
        messagebox.showerror("Erro", "Preencha os campos")
        return

    try:
        valor = float(valor)
    except:
        messagebox.showerror("Erro", "Valor inválido")
        return

    inserir_gastos((categoria, data, valor))

    atualizar_tabela()
    limpar_campos()


# =========================
# Deletar movimentação
# =========================

def deletar():

    item = tabela.selection()

    if not item:
        messagebox.showwarning("Aviso", "Selecione um item")
        return

    valores = tabela.item(item)["values"]

    tipo = valores[0]
    id = valores[1]

    if tipo == "Receita":
        deletar_receitas((id,))
    else:
        deletar_gastos((id,))

    atualizar_tabela()


# =========================
# Gráfico de gastos
# =========================

def grafico_gastos():

    gastos = ver_gastos()

    categorias = []
    valores = []

    for g in gastos:
        categorias.append(g[1])
        valores.append(g[3])

    if len(valores) == 0:
        messagebox.showinfo("Aviso", "Não há gastos registrados")
        return

    plt.pie(valores, labels=categorias, autopct='%1.1f%%')
    plt.title("Distribuição de Gastos")
    plt.show()


# =========================
# Exportar Excel
# =========================

def exportar_excel():

    receitas = ver_receitas()
    gastos = ver_gastos()

    dados = []

    for r in receitas:
        dados.append(["Receita", r[1], r[2], r[3]])

    for g in gastos:
        dados.append(["Gasto", g[1], g[2], g[3]])

    df = pd.DataFrame(dados, columns=["Tipo", "Categoria", "Data", "Valor"])

    df.to_excel("relatorio_financeiro.xlsx", index=False)

    messagebox.showinfo("Sucesso", "Relatório exportado!")


# =========================
# Dashboard
# =========================

frame_dashboard = tk.Frame(janela, bg="#f5f6fa")
frame_dashboard.pack(pady=20)

label_receitas = tk.Label(
    frame_dashboard,
    text="Receitas: R$ 0",
    font=("Arial", 14),
    bg="#2ecc71",
    fg="white",
    width=20
)

label_receitas.grid(row=0, column=0, padx=10)

label_gastos = tk.Label(
    frame_dashboard,
    text="Gastos: R$ 0",
    font=("Arial", 14),
    bg="#e74c3c",
    fg="white",
    width=20
)

label_gastos.grid(row=0, column=1, padx=10)

label_saldo = tk.Label(
    frame_dashboard,
    text="Saldo: R$ 0",
    font=("Arial", 14),
    bg="#3498db",
    fg="white",
    width=20
)

label_saldo.grid(row=0, column=2, padx=10)


# =========================
# Formulário
# =========================

frame_form = tk.Frame(janela, bg="#f5f6fa")
frame_form.pack()


tk.Label(frame_form, text="Categoria", bg="#f5f6fa").grid(row=0, column=0)

categorias = [c[1] for c in ver_categoria()]

entrada_categoria = ttk.Combobox(
    frame_form,
    values=categorias
)

entrada_categoria.grid(row=1, column=0)


tk.Label(frame_form, text="Data", bg="#f5f6fa").grid(row=0, column=1)

entrada_data = tk.Entry(frame_form)
entrada_data.grid(row=1, column=1)


tk.Label(frame_form, text="Valor", bg="#f5f6fa").grid(row=0, column=2)

entrada_valor = tk.Entry(frame_form)
entrada_valor.grid(row=1, column=2)


botao_receita = tk.Button(
    frame_form,
    text="Adicionar Receita",
    bg="#2ecc71",
    fg="white",
    command=adicionar_receita
)

botao_receita.grid(row=2, column=0, pady=10)


botao_gasto = tk.Button(
    frame_form,
    text="Adicionar Gasto",
    bg="#e74c3c",
    fg="white",
    command=adicionar_gasto
)

botao_gasto.grid(row=2, column=1, pady=10)


# =========================
# Tabela
# =========================

colunas = ("Tipo", "ID", "Categoria", "Data", "Valor")

tabela = ttk.Treeview(
    janela,
    columns=colunas,
    show="headings"
)

for col in colunas:
    tabela.heading(col, text=col)

tabela.pack(fill="both", expand=True)


# =========================
# Botões extras
# =========================

frame_botoes = tk.Frame(janela, bg="#f5f6fa")
frame_botoes.pack(pady=10)

tk.Button(
    frame_botoes,
    text="Deletar",
    command=deletar
).grid(row=0, column=0, padx=10)

tk.Button(
    frame_botoes,
    text="Gráfico de Gastos",
    command=grafico_gastos
).grid(row=0, column=1, padx=10)

tk.Button(
    frame_botoes,
    text="Exportar Excel",
    command=exportar_excel
).grid(row=0, column=2, padx=10)


# =========================

atualizar_tabela()

janela.mainloop()