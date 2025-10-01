import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def exportar_para_pdf():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id , nome, idade FROM usuarios')
    dados = cursor.fetchall()

    nome_arquivo = 'relatorio_usuario.pdf'

    pdf = SimpleDocTemplate(
        nome_arquivo,
        pagesize=letter
    )

    cabecalho = [('Id', 'Nome', 'Idade')]
    dados_tabela = cabecalho + dados

    tabela = Table(dados_tabela)

    estilo = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (2,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 12),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,0), (-1,-1), colors.beige),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
    ])
    tabela.setStyle(estilo)
    elementos = [tabela]
    pdf.build(elementos)

    print(f"Dados exportados com sucesso para o arquivo {nome_arquivo}")

if __name__ == '__main__':
    exportar_para_pdf()