from tabula import read_pdf
import tabula
pdf=["22-1808-16A-EN.pdf"]
csv=["22-1808-16A-EN_5_8.csv"]

d1 = read_pdf(pdf[0], pages=[5,8])
tabula.convert_into(pdf[0], csv[0], output_format="csv", pages=[5,8])