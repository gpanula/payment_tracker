from odf.opendocument import OpenDocumentSpreadsheet
from odf.element import Element
from odf.style import Style, TableColumnProperties, TableCellProperties, TextProperties, Map
from odf.table import Table, TableColumn, TableRow, TableCell
from odf.text import P
from odf.number import DateStyle, Year, Month, Day, Text, Number, CurrencyStyle, CurrencySymbol

CALCEXTNS = "urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0"

def create_payment_tracker_ods():
    doc = OpenDocumentSpreadsheet()

    # --- 1. NUMBER & DATE FORMATS ---
    # Currency Format ($)
    curr_style = CurrencyStyle(name="USD_Currency")
    curr_style.addElement(CurrencySymbol(language="en", country="US", text="$"))
    curr_style.addElement(Number(decimalplaces=2, minintegerdigits=1, grouping=True))
    doc.styles.addElement(curr_style)

    # Date Format (YYYY-MM-DD)
    date_format = DateStyle(name="ISO_Date")
    date_format.addElement(Year(style="long"))
    date_format.addElement(Text(text="-"))
    date_format.addElement(Month(style="long"))
    date_format.addElement(Text(text="-"))
    date_format.addElement(Day(style="long"))
    doc.styles.addElement(date_format)

    # --- 2. BASE CELL & HIGHLIGHT STYLES ---
    # Header Style
    header_style = Style(name="HeaderStyle", family="table-cell")
    header_style.addElement(TableCellProperties(backgroundcolor="#eaeaea", border="1.5pt solid #888888"))
    header_style.addElement(TextProperties(fontweight="bold", color="#222222", fontfamily="Arial"))
    doc.styles.addElement(header_style)

    # Highlight 1: Past Due & Scheduled (Blue)
    style_past_due_paid = Style(name="Style_PastDuePaid", family="table-cell")
    style_past_due_paid.addElement(TableCellProperties(backgroundcolor="#d0e1fd", border="1.5pt solid #888888"))
    style_past_due_paid.addElement(TextProperties(fontfamily="Arial", color="#222222"))
    doc.styles.addElement(style_past_due_paid)

    # Highlight 2: Scheduled Future/Today (Green)
    style_paid = Style(name="Style_Paid", family="table-cell")
    style_paid.addElement(TableCellProperties(backgroundcolor="#e2f0d9", border="1.5pt solid #888888"))
    style_paid.addElement(TextProperties(fontfamily="Arial", color="#222222"))
    doc.styles.addElement(style_paid)

    # Highlight 3: Past Due & Unpaid (Red)
    style_overdue = Style(name="Style_Overdue", family="table-cell")
    style_overdue.addElement(TableCellProperties(backgroundcolor="#ee1b1b", border="1.5pt solid #888888"))
    style_overdue.addElement(TextProperties(fontfamily="Arial", color="#ffffff", fontweight="bold"))
    doc.styles.addElement(style_overdue)

    # Highlight 4: Due Within 7 Days Unscheduled (Orange)
    style_due_soon = Style(name="Style_DueSoon", family="table-cell")
    style_due_soon.addElement(TableCellProperties(backgroundcolor="#f09138", border="1.5pt solid #888888"))
    style_due_soon.addElement(TextProperties(fontfamily="Arial", color="#ffffff", fontweight="bold"))
    doc.styles.addElement(style_due_soon)

    # Base Column Cell Styles
    default_cell_style = Style(name="DefaultCellStyle", family="table-cell")
    default_cell_style.addElement(TableCellProperties(border="1.5pt solid #888888"))
    default_cell_style.addElement(TextProperties(fontfamily="Arial", color="#222222"))

    default_date_cell_style = Style(name="DefaultDateStyle", family="table-cell", datastylename="ISO_Date")
    default_date_cell_style.addElement(TableCellProperties(border="1.5pt solid #888888"))
    default_date_cell_style.addElement(TextProperties(fontfamily="Arial", color="#222222"))

    default_curr_cell_style = Style(name="DefaultCurrencyStyle", family="table-cell", datastylename="USD_Currency")
    default_curr_cell_style.addElement(TableCellProperties(border="1.5pt solid #888888"))
    default_curr_cell_style.addElement(TextProperties(fontfamily="Arial", color="#222222"))

    # Map rules (Standard ODF syntax)
    map_rules = [
        ('is-true-formula(AND(LOWER([.$D2])="x"; [.$B2]<TODAY(); [.$B2]<>""))', 'Style_PastDuePaid'),
        ('is-true-formula(AND(LOWER([.$D2])="x"; [.$B2]>=TODAY(); [.$B2]<>""))', 'Style_Paid'),
        ('is-true-formula(AND(LOWER([.$D2])<>"x"; [.$B2]<TODAY(); [.$B2]<>""))', 'Style_Overdue'),
        ('is-true-formula(AND(LOWER([.$D2])<>"x"; ([.$B2]-TODAY())>=0; ([.$B2]-TODAY())<=7; [.$B2]<>""))', 'Style_DueSoon'),
    ]

    for condition, apply_style in map_rules:
        default_cell_style.addElement(Map(condition=condition, applystylename=apply_style, basecelladdress="'Payment Tracker'.A2"))
        default_date_cell_style.addElement(Map(condition=condition, applystylename=apply_style, basecelladdress="'Payment Tracker'.A2"))
        default_curr_cell_style.addElement(Map(condition=condition, applystylename=apply_style, basecelladdress="'Payment Tracker'.A2"))

    doc.styles.addElement(default_cell_style)
    doc.styles.addElement(default_date_cell_style)
    doc.styles.addElement(default_curr_cell_style)

    # --- 3. COLUMN WIDTH PROPORTIONS ---
    col_widths = ["4.5cm", "4.0cm", "3.5cm", "4.5cm", "6.0cm"]
    for i, w in enumerate(col_widths):
        col_style = Style(name=f"ColWidth_{i}", family="table-column")
        col_style.addElement(TableColumnProperties(columnwidth=w))
        doc.styles.addElement(col_style)

    # --- 4. BUILD TABLE & ROWS ---
    table = Table(name="Payment Tracker")

    for i in range(len(col_widths)):
        table.addElement(TableColumn(stylename=f"ColWidth_{i}"))

    # Add Header Row
    headers = ["Card", "Due Date", "Amount", "Payment Scheduled", "Notes"]
    header_row = TableRow()
    for text in headers:
        cell = TableCell(stylename=header_style)
        cell.addElement(P(text=text))
        header_row.addElement(cell)
    table.addElement(header_row)

    # Sample Data
    sample_data = [
        ("Omega Rewards", "2026-08-22", 45.12, "x", ""),
        ("Atlas Auto Loan", "2026-09-02", 210.00, "x", "bi-weekly payment"),
        ("Zenith Utility", "2026-08-05", 88.50, "", "due soon sample"),
        ("Apex Credit Card", "2026-07-28", 125.00, "", "past due sample"),
    ]

    for row_idx in range(2, 27):
        row = TableRow()
        data = sample_data[row_idx - 2] if row_idx - 2 < len(sample_data) else ("", "", "", "", "")
        card, date_str, amount, scheduled, notes = data

        # Column A: Card
        c1 = TableCell(valuetype="string", stylename=default_cell_style)
        c1.addElement(P(text=card))
        row.addElement(c1)

        # Column B: Due Date
        c2 = TableCell(valuetype="date", datevalue=date_str, stylename=default_date_cell_style) if date_str else TableCell(stylename=default_date_cell_style)
        c2.addElement(P(text=date_str))
        row.addElement(c2)

        # Column C: Amount
        if isinstance(amount, (int, float)):
            c3 = TableCell(valuetype="currency", value=amount, currency="USD", stylename=default_curr_cell_style)
            c3.addElement(P(text=f"${amount:.2f}"))
        else:
            c3 = TableCell(stylename=default_curr_cell_style)
            c3.addElement(P(text=""))
        row.addElement(c3)

        # Column D: Payment Scheduled
        c4 = TableCell(valuetype="string", stylename=default_cell_style)
        c4.addElement(P(text=scheduled))
        row.addElement(c4)

        # Column E: Notes
        c5 = TableCell(valuetype="string", stylename=default_cell_style)
        c5.addElement(P(text=notes))
        row.addElement(c5)

        table.addElement(row)

    # Calcext Conditional Formats (Must be added AFTER all rows!)
    cond_formats = Element(qname=(CALCEXTNS, "conditional-formats"))
    cond_format = Element(qname=(CALCEXTNS, "conditional-format"))
    cond_format.setAttribute((CALCEXTNS, "target-range-address"), "'Payment Tracker'.A2:'Payment Tracker'.E26")

    calcext_rules = [
        ('formula-is(AND(LOWER([.$D2])="x"; [.$B2]<TODAY(); [.$B2]<>""))', 'Style_PastDuePaid'),
        ('formula-is(AND(LOWER([.$D2])="x"; [.$B2]>=TODAY(); [.$B2]<>""))', 'Style_Paid'),
        ('formula-is(AND(LOWER([.$D2])<>"x"; [.$B2]<TODAY(); [.$B2]<>""))', 'Style_Overdue'),
        ('formula-is(AND(LOWER([.$D2])<>"x"; ([.$B2]-TODAY())>=0; ([.$B2]-TODAY())<=7; [.$B2]<>""))', 'Style_DueSoon'),
    ]

    for value, apply_style in calcext_rules:
        cond = Element(qname=(CALCEXTNS, "condition"))
        cond.setAttribute((CALCEXTNS, "apply-style-name"), apply_style)
        cond.setAttribute((CALCEXTNS, "value"), value)
        cond.setAttribute((CALCEXTNS, "base-cell-address"), "'Payment Tracker'.A2")
        cond_format.addElement(cond, check_grammar=False)

    cond_formats.addElement(cond_format, check_grammar=False)
    table.addElement(cond_formats, check_grammar=False)

    doc.spreadsheet.addElement(table)
    doc.save("Payment_Tracker.ods")
    print("Successfully generated Payment_Tracker.ods with built-in conditional rules!")

if __name__ == "__main__":
    create_payment_tracker_ods()
