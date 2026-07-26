# PDF Merger GUI in Python

from pypdf import PdfWriter

merger = PdfWriter()

# OR we can use this syntax to import pypdf as well.

# import pypdf
# merger = pypdf.PdfWriter()

pdfs = ["Module II Lecture 13 Iron C Phase diagram.pdf", "Module II Lecture 14 Metal Forming.pdf", "Module II Lecture 15 Metal processing.pdf"]
for pdf in pdfs:
    merger.append(pdf)

merger.write("lecture_merged.pdf")

# flow of code 
#                 PdfWriter()

#                     │
#                     ▼

#           Empty PdfWriter Object
#                 Pages = []

#                     │
#         append("Lecture13.pdf")
#                     ▼

#         Pages = [All pages of Lecture13]

#                     │
#         append("Lecture14.pdf")
#                     ▼

#  Pages = [Lecture13 pages + Lecture14 pages]

#                     │
#         append("Lecture15.pdf")
#                     ▼

#  Pages = [Lecture13 + Lecture14 + Lecture15]

#                     │
#      write("lecture_merged.pdf")
#                     ▼

#       Creates a brand new merged PDF

 