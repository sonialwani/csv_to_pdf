from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv", sep=",")

for index, row in df.iterrows():
    for number in range(row['Pages']):
        pdf.add_page()
        pdf.set_font("Arial", "B", 8)
        pdf.cell(w=0, h=20, txt=row["Topic"], align="L", ln=1)




pdf.output("output.pdf")



