from fpdf import FPDF

pdf = FPDF(orientation='p', unit='cm', format='a4')
pdf.add_page()

pdf.set_font("Arial", "B", 16,)
pdf.cell(w=0, h=0.8, txt="Relatório de Vendas",
         align='c', new_x='LMARGIN', new_y='NEXT')

pdf.set_font(size=12)
desc1 = f'''Para o mês de dezembro, foram registradaos um total de 190 vendas para o setor de veículos importados'''
pdf.ln(0.5)
pdf.multi_cell(w=0, h=0.5, txt=desc1, align='l',
               new_x='LMARGIN', new_y='NEXT')

pdf.ln(0.5)
pdf.set_font("Arial", "B", 16,)
pdf.cell(w=0, h=0.8, txt="Vendas de carros americanos",
         align='l', new_x='LMARGIN', new_y='NEXT')

pdf.set_font(size=12)
desc2 = f'''Foram vendidos 100 carros americanos'''
pdf.multi_cell(w=0, h=0.5, txt=desc2, align='l',
               new_x='LMARGIN', new_y='NEXT')

pdf.ln(0.3)

pdf.set_font("Arial", "B", 16,)
pdf.cell(w=0, h=0.8, txt="Vendas de carros italianos",
         align='l', new_x='LMARGIN', new_y='NEXT')


pdf.set_font(size=12)
desc2 = f'''Foram vendidos 90 carros italianos'''
pdf.multi_cell(w=0, h=0.5, txt=desc2, align='l',
               new_x='LMARGIN', new_y='NEXT')



pdf.output("tuto1.pdf")
