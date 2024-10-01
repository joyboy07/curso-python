from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Crear un objeto canvas
pdf = canvas.Canvas('archivo.pdf', pagesize=letter)
width, height = letter

# Añadir texto
pdf.setFont('Helvetica', 16)
pdf.drawString(100, height - 100, 'Hola, este es un PDF creado con Python.')

# Añadir otro texto
pdf.setFont('Helvetica', 12)
pdf.drawString(100, height - 130, 'Este es un segundo renglón de texto.')

# Guardar el PDF
pdf.save()

print('PDF creado con éxito.')