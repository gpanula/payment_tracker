# Payment Tracker (ODF / LibreOffice Spreadsheet)

A lightweight, local-first bill and credit card payment tracker formatted as an OpenDocument Spreadsheet (`.ods`). This directory contains `generate_tracker_ods.py`, a standalone Python script that programmatically generates `Payment_Tracker.ods` with built-in conditional formatting, automated currency and date formatting, custom table column widths, and sample data.

---

## Features

* **Native ODF / OpenDocument Format (`.ods`):** Fully compatible with LibreOffice Calc, OpenOffice, and Microsoft Excel without requiring macro security permissions.
* **Dual-Engine Conditional Formatting:** Highlighting rules are compiled directly into the spreadsheet's XML structure using both standard ODF `<style:map>` and modern LibreOffice Calc `<calcext:conditional-formats>` XML elements for maximum cross-application compatibility. Rows update dynamically based on the current system date (`TODAY()`) and payment schedule markers:
  * **Blue (`#D0E1FD`):** Payment scheduled for a bill whose due date has passed.
  * **Green (`#E2F0D9`):** Payment scheduled for an upcoming or current bill.
  * **Red (`#EE1B1B`):** Past due and unscheduled (unpaid).
  * **Orange (`#F09138`):** Due within the next 7 days and unscheduled (unpaid).
* **Automatic Currency & Date Formatting:** 
  * Column B (**Due Date**) uses an ISO Date style (`YYYY-MM-DD`) for clean date parsing and calculations.
  * Column C (**Amount**) is mapped to an internal ODF USD currency style (`$#,##0.00`) for clean numerical alignment and calculations.
* **Proportional Layout:** Pre-configured column widths and high-contrast header borders (`1.5pt solid #888888`) matching the web version layout.

---

## Quick Start

### 1. Prerequisites
The generator script requires Python 3 and the `odfpy` library:

```bash
pip install odfpy
```

### 2. Generate the Spreadsheet

Run the script to output a fresh `Payment_Tracker.ods` file in your current working directory:

```bash
python generate_tracker_ods.py
```

### 3. Open in LibreOffice Calc or Excel

Double-click `Payment_Tracker.ods` or open it from within LibreOffice Calc or Microsoft Excel.

---

## How to Use the Spreadsheet

1. **Card / Bill Name (Column A):** Enter the credit card or service provider name.
2. **Due Date (Column B):** Enter the due date in standard date format (`YYYY-MM-DD` or `MM/DD/YYYY`).
3. **Amount (Column C):** Enter the numeric payment amount (e.g., `45.12`). The cell automatically formats as `$45.12`.
4. **Payment Scheduled (Column D):** Type **`x`** when a payment is scheduled or posted.
   * Typing `x` clears the **Red** or **Orange** unscheduled warnings and converts the row to **Green** or **Blue**.
   * Clearing `x` reverts the row back to unscheduled evaluation rules.
5. **Notes (Column E):** Add additional information such as account details or auto-pay status.

---

## Spreadsheet Conditional Logic Details

The generated spreadsheet uses OpenFormula bracket syntax and semicolon (`;`) argument separators with relative anchors (`base-cell-address="'Payment Tracker'.A2"`) evaluated per row:

| Priority | Status Target | ODF Standard Formula (`style:map`) | LibreOffice Calc Extension (`calcext`) | Cell Style Applied |
| --- | --- | --- | --- | --- |
| **1** | Past Due & Scheduled | `is-true-formula(AND(LOWER([.$D2])="x"; [.$B2]<TODAY(); [.$B2]<>""))` | `formula-is(AND(LOWER([.$D2])="x"; [.$B2]<TODAY(); [.$B2]<>""))` | `Style_PastDuePaid` (Blue) |
| **2** | Scheduled (Current/Future) | `is-true-formula(AND(LOWER([.$D2])="x"; [.$B2]>=TODAY(); [.$B2]<>""))` | `formula-is(AND(LOWER([.$D2])="x"; [.$B2]>=TODAY(); [.$B2]<>""))` | `Style_Paid` (Green) |
| **3** | Past Due & Unpaid | `is-true-formula(AND(LOWER([.$D2])<>"x"; [.$B2]<TODAY(); [.$B2]<>""))` | `formula-is(AND(LOWER([.$D2])<>"x"; [.$B2]<TODAY(); [.$B2]<>""))` | `Style_Overdue` (Red) |
| **4** | Due Within 7 Days (Unscheduled) | `is-true-formula(AND(LOWER([.$D2])<>"x"; ([.$B2]-TODAY())>=0; ([.$B2]-TODAY())<=7; [.$B2]<>""))` | `formula-is(AND(LOWER([.$D2])<>"x"; ([.$B2]-TODAY())>=0; ([.$B2]-TODAY())<=7; [.$B2]<>""))` | `Style_DueSoon` (Orange) |

---

## File Structure

```text
.
├── generate_tracker_ods.py         # Python script that builds the ODF file
├── generate_tracker_ods.readme.md  # Documentation for the ODS generator
└── Payment_Tracker.ods             # Output OpenDocument Spreadsheet file
```
