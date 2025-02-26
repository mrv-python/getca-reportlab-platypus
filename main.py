from reportlab.platypus import Paragraph, PageBreak, HRFlowable, Spacer, SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

pdf = SimpleDocTemplate("platypus.pdf", 
                        pagesize = letter, 
                        rightMargin = inch, 
                        leftMargin = inch, 
                        topMargin = 0.5 * inch, bottomMargin = 0.5 * inch)
styles = getSampleStyleSheet()
flow = []

para = Paragraph("Hello Platypus", styles["Normal"])
flow.append(para)
para = Paragraph("Hello Platypus", styles["Normal"])
flow.append(para)

flow.append(Spacer(1, inch))

para = Paragraph("Hello Again", styles["Normal"])
flow.append(para)

para = Paragraph("Do Paragraphs Wrap Text by Default? Do Paragraphs Wrap Text by Default? Do Paragraphs Wrap Text by Default? Do Paragraphs Wrap Text by Default? Do Paragraphs Wrap Text by Default? Do Paragraphs Wrap Text by Default?", styles["Normal"])
flow.append(para)

flow.append(Spacer(1, 20))

para = Paragraph("Goodbye", styles["Normal"])
flow.append(para)


# XML
text = '''
    Hello from <u>Colin</u>.<br />
    I don't <strong>remember</strong> about <em>Doc Strings</em>.<br />
    What do I do? <strike>Carry on</strike><br />
    Make a <u><a href="www.nba.com" color="BLUE">link</a></u><br />
    Try to use span to change color of <span color="RED">text</span>.
'''
para = Paragraph(text, styles["Normal"])
flow.append(para)

# Custom Fonts
text = '''
    <font name="Times-Italic" size=24 color="red">text with custom font</font><br />
'''
para = Paragraph(text, styles["Normal"])
flow.append(para)


flow.append(Spacer(1, 40))


# Inline Images
text = '''
    This is our logo: <img src="Python-logo.png" width="25" height="25" />, hope you like it.
'''
para = Paragraph(text, styles["Normal"])
flow.append(para)

# New Page
flow.append(PageBreak())

# HRFlowable() like <hr />
para = Paragraph("Hello Again", styles["Normal"])
flow.append(para)

flow.append(HRFlowable())
flow.append(HRFlowable(width="100%", thickness= 3, color = colors.darkorange, spaceBefore=5))
flow.append(HRFlowable(width="60%", thickness= 2, color = colors.green, spaceAfter=10, hAlign="LEFT"))

# Bullets (Paragraph argument)
para = Paragraph("List Item 1", styles["Normal"], bulletText="**")
flow.append(para)
para = Paragraph("List Item 2", styles["Normal"], bulletText="**")
flow.append(para)
para = Paragraph("List Item 3", styles["Normal"], bulletText="**")
flow.append(para)

# Bullets (<bullet>)
para = Paragraph("<bullet>&bull</bullet>List Item 1<br />", styles["Normal"])
flow.append(para)
para = Paragraph("<bullet>&bull</bullet>List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2<br />", styles["Normal"])
flow.append(para)
para = Paragraph("<bullet>&bull</bullet>List Item 3<br />", styles["Normal"])
flow.append(para)

for i in range(4,7):
    para = Paragraph(f"<bullet>&bull</bullet>List Item {i}<br />", styles["Normal"])
    flow.append(para)

# Tables
data = [
    ["name", "email", "age"],
    ["Colin", "colin.veldkamp@gmail.com", 44],
    ["Andrea","andrea.veldkamp@gmail.com", 40],
    ["Andrew", "veldkamp.andrew@gmail.com", 18]
        ]

# TableStyle takes a list of tuples: each tuple declaring a style property
# Cells can be accessed by coordinates (col, row) like A1 and can be accessed using python indexing
# [(0,0), (1, 0), (2, 0)]
# [(0,1), (1, 1), (2, 2)]
# Top left cell is (0, 0) and bottom right cell is (-1, -1)
# Line Options
# - GRID, BOX or OUTLINE, INNERGRID, LINEBELOW, LINEABOVE, LINEBEFORE, LINEAFTER
t_style = TableStyle([
    ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
    ("ALIGN", (0, 0), (-1, 0), "CENTRE"),
    ("BACKGROUND", (0, 0), (-1, 0), colors.blue),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Courier"),
    ("BACKGROUND", (1, 1), (1, 1), ("HORIZONTAL", colors.red, colors.white))
    


    ])
t = Table(data, hAlign="LEFT", cornerRadii=(5,5,5,5), spaceBefore=15)
t.setStyle(t_style)
flow.append(t)

pdf.build(flow)



