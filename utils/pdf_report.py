from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


def generate_pdf(df):

    pdf_name = "Candidate_Ranking_Report.pdf"

    doc = SimpleDocTemplate(pdf_name)

    data = [list(df.columns)]

    for row in df.values.tolist():
        data.append(row)

    table = Table(data)

    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.grey),
            ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
            ("GRID", (0,0), (-1,-1), 1, colors.black),
            ("BACKGROUND", (0,1), (-1,-1), colors.beige)
        ])
    )

    doc.build([table])

    return pdf_name