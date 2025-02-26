# GETCA - ReportLab: Create PDFs Like a List of Elements

# from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, HRFlowable, Spacer, Table, TableStyle
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib import colors
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.units import inch

# Imports
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak, Image, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

# Create a Simple Doc Template and Sample Stylesheet
pdf = SimpleDocTemplate("platypus-test.pdf", 
                        pagesize=letter, 
                        rightMargin=inch, 
                        leftMargin=inch, 
                        topMargin=0.5*inch, 
                        bottomMargin=0.5*inch)
styles = getSampleStyleSheet()

# Create a list to add page elements to
flow = []


# Add Paragraphs and Headings to the flow - Paragraph(text, style)
text = "Heading 1"
flow.append(Paragraph(text, styles["Heading1"]))

flow.append(HRFlowable(width="100%", thickness=3, color="#00FF00", spaceAfter=20))

text = "Hello Platypus! I wonder why this is called Platypus?!?"
flow.append(Paragraph(text, styles["Normal"]))

flow.append(Spacer(1,12)) # Spacer(width, height)

text = "This is another paragraph added to the flow. Eventually all things added to this flow will be built into a pdf document."
flow.append(Paragraph(text, styles["Normal"]))

# Add Image
flow.append(Image("Python-logo.png", width=75, height=75, hAlign="CENTER"))

# Add inline Image
text = 'Before <img src="Python-logo.png" width="20" height="20" /> After'
flow.append(Paragraph(text, styles["Normal"]))

text = "Heading 2"
flow.append(Paragraph(text, styles["Heading2"]))
text = "Do Paragraphs Wrap Text by Default? Do Paragraphs Wrap Text by Default? Do Paragraphs Wrap Text by Default? Do Paragraphs Wrap Text by Default? Do Paragraphs Wrap Text by Default? Do Paragraphs Wrap Text by Default?"
flow.append(Paragraph(text, styles["Normal"]))
text = "This is some random text. I should get some lorem ipsum text to use as a filler for here."
flow.append(Paragraph(text, styles["Normal"]))

# Lists
test_list = ListFlowable(
    [
        ListItem(Paragraph("List item 1", styles["Normal"])),
        ListItem(Paragraph("List item 2", styles["Normal"])),
        # ListItem(Paragraph("List item 2", styles["Normal"]), leftIndent=35, bulletColor="red"),
        ListItem(Paragraph("List item 3", styles["Normal"]))
    ],
    # bulletType='bullet', # 1|a|A|i|I|bullet
    # start="circle"
    bulletType="bullet",
    # start="9",
    bulletFontSize=12,
    bulletColor="purple",
    bulletIndent=50
)
flow.append(test_list)


flow.append(Spacer(1,12)) # Spacer(width, height)

# Bullets (Paragraph argument)
para = Paragraph("List Item 1", styles["Normal"], bulletText="1.")
flow.append(para)
para = Paragraph("List Item 2", styles["Normal"], bulletText="2.")
flow.append(para)
para = Paragraph("List Item 3", styles["Normal"], bulletText="30.")
flow.append(para)

# Start a New Page
flow.append(PageBreak())

# Second Page Content
text = "Second Page"
flow.append(Paragraph(text, styles["Heading1"]))

flow.append(HRFlowable(width="100", thickness=3, color="#00FF00", spaceAfter=20))

text = "Welcome to the second page!"
flow.append(Paragraph(text, styles["Normal"]))


# flow.append(Spacer(1, inch))

# para = Paragraph("Hello Again", styles["Normal"])
# flow.append(para)

# para = Paragraph("Do Paragraphs Wrap Text by Default? Do Paragraphs Wrap Text by Default? Do Paragraphs Wrap Text by Default? Do Paragraphs Wrap Text by Default? Do Paragraphs Wrap Text by Default? Do Paragraphs Wrap Text by Default?", styles["Normal"])
# flow.append(para)

# flow.append(Spacer(1, 20))

# para = Paragraph("Goodbye", styles["Normal"])
# flow.append(para)


# XML
text = '''
    Hello from <u>Colin</u>.<br />
    I don't <strong>remember</strong> about <em>Doc Strings</em>.<br />
    What do I do? <strike>Carry on</strike><br />
    Make a <u><a href="www.nba.com" color="blue">link</a></u><br />
    Try to use span to change color of <span color="red">text</span>.<br />
'''
para = Paragraph(text, styles["Normal"])
flow.append(para)

text = '''
    <para fontName="Courier" spaceBefore="50" textTransform="Uppercase" alignment="right">
        Para element testing.
    </para>
'''
para = Paragraph(text, styles["Normal"])
flow.append(para)

# # Custom Fonts
# text = '''
#     <font name="Times-Italic" size=24 color="red">text with custom font</font><br />
# '''
# para = Paragraph(text, styles["Normal"])
# flow.append(para)


# flow.append(Spacer(1, 40))


# # Inline Images
# text = '''
#     This is our logo: <img src="Python-logo.png" width="25" height="25" />, hope you like it.
# '''
# para = Paragraph(text, styles["Normal"])
# flow.append(para)

# # New Page
# flow.append(PageBreak())

# # HRFlowable() like <hr />
# para = Paragraph("Hello Again", styles["Normal"])
# flow.append(para)

# flow.append(HRFlowable())
# flow.append(HRFlowable(width="100%", thickness= 3, color = colors.darkorange, spaceBefore=5))
# flow.append(HRFlowable(width="60%", thickness= 2, color = colors.green, spaceAfter=10, hAlign="LEFT"))

# # Bullets (Paragraph argument)
# para = Paragraph("List Item 1", styles["Normal"], bulletText="**")
# flow.append(para)
# para = Paragraph("List Item 2", styles["Normal"], bulletText="**")
# flow.append(para)
# para = Paragraph("List Item 3", styles["Normal"], bulletText="**")
# flow.append(para)

# # Bullets (<bullet>)
# para = Paragraph("<bullet>&bull</bullet>List Item 1<br />", styles["Normal"])
# flow.append(para)
# para = Paragraph("<bullet>&bull</bullet>List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2 List Item 2<br />", styles["Normal"])
# flow.append(para)
# para = Paragraph("<bullet>&bull</bullet>List Item 3<br />", styles["Normal"])
# flow.append(para)

# for i in range(4,7):
#     para = Paragraph(f"<bullet>&bull</bullet>List Item {i}<br />", styles["Normal"])
#     flow.append(para)

# # Tables
# data = [
#     ["name", "email", "age"],
#     ["Colin", "colin.veldkamp@gmail.com", 44],
#     ["Andrea","andrea.veldkamp@gmail.com", 40],
#     ["Andrew", "veldkamp.andrew@gmail.com", 18]
#         ]

# # TableStyle takes a list of tuples: each tuple declaring a style property
# # Cells can be accessed by coordinates (col, row) like A1 and can be accessed using python indexing
# # [(0,0), (1, 0), (2, 0)]
# # [(0,1), (1, 1), (2, 2)]
# # Top left cell is (0, 0) and bottom right cell is (-1, -1)
# # Line Options
# # - GRID, BOX or OUTLINE, INNERGRID, LINEBELOW, LINEABOVE, LINEBEFORE, LINEAFTER
# t_style = TableStyle([
#     ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
#     ("ALIGN", (0, 0), (-1, 0), "CENTRE"),
#     ("BACKGROUND", (0, 0), (-1, 0), colors.blue),
#     ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
#     ("FONT", (0, 0), (-1, 0), "Courier"),
#     ("BACKGROUND", (1, 1), (1, 1), ("HORIZONTAL", colors.red, colors.white))
    


#     ])
# t = Table(data, hAlign="LEFT", cornerRadii=(5,5,5,5), spaceBefore=15)
# t.setStyle(t_style)
# flow.append(t)


# Create a pdf file out of the page elements added to the flow
pdf.build(flow)



