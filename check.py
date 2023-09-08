from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation="P", unit="mm", format="A4")




pdf.add_page()
pdf.set_font("Arial", "B",8)
pdf.cell(w=0, h=12, txt="Hi", align="L", ln=1)

pdf.output("output.pdf")