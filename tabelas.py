import csv
from fpdf import FPDF


class PDF(FPDF):
    def basic_table(self, headings, rows):
        for heading in headings:
            self.cell(w=4, h=0.7, txt=heading, border=1)
        self.ln()
        for row in rows:
            for col in row:
                self.cell(w=4, h=0.6, text=col, border=1)
            self.ln()

    def improved_table(self, headings, rows, col_widths=(4.2, 3.9, 3.5, 4.0)):
        for col_width, heading in zip(col_widths, headings):
            self.cell(w=col_width, h=0.7, text=heading, border=1, align="C")
        self.ln()
        for row in rows:
            self.cell(w=col_widths[0], h=0.6, txt=row[0], border="LR")
            self.cell(w=col_widths[1], h=0.6, txt=row[1], border="LR")
            self.cell(w=col_widths[2], h=0.6, txt=row[2], border="LR", align="R")
            self.cell(w=col_widths[3], h=0.6, txt=row[3], border="LR", align="R")
            self.ln()
        # Closure line:
        self.cell(w=sum(col_widths), h=0, txt="", border="T")

    def colored_table(self, headings, rows, col_widths=(4.2, 3.9, 3.5, 4.2)):
        # Colors, line width and bold font:
        self.set_fill_color(255, 100, 0)
        self.set_text_color(255)
        self.set_draw_color(255, 0, 0)
        self.set_line_width(0.03)
        self.set_font(style="B")
        for col_width, heading in zip(col_widths, headings):
            self.cell(col_width, 0.7, heading, border=1, align="C", fill=True)
        self.ln()
        # Color and font restoration:
        self.set_fill_color(224, 235, 255)
        self.set_text_color(0)
        self.set_font()
        fill = False
        for row in rows:
            self.cell(col_widths[0], 0.6, row[0],border="LR", align="L", fill=fill)
            self.cell(col_widths[1], 0.6, row[1],border="LR", align="L", fill=fill)
            self.cell(col_widths[2], 0.6, row[2],border="LR", align="R", fill=fill)
            self.cell(col_widths[3], 0.6, row[3],border="LR", align="R", fill=fill)
            self.ln()
            fill = not fill
        self.cell(sum(col_widths), 0, "", "T")


def load_data_from_csv(csv_filepath):
    headings, rows = [], []
    with open(csv_filepath, encoding="utf8") as csv_file:
        for row in csv.reader(csv_file, delimiter=","):
            if not headings:  # extracting column names from first row:
                headings = row
            else:
                rows.append(row)
    return headings, rows


col_names, data = load_data_from_csv("countries.txt")
pdf = PDF(unit='cm')
pdf.set_font("helvetica", size=14)
pdf.add_page()
pdf.basic_table(col_names, data)
pdf.add_page()
pdf.improved_table(col_names, data)
pdf.add_page()
pdf.colored_table(col_names, data)
pdf.output("demo.pdf")