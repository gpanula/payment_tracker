# Payment Tracker

A lightweight, local-first web application designed to help you track credit card and bill due dates, payment schedules, and notes. Built as a single, zero-dependency HTML file, it runs directly in your web browser with zero setup or server requirements.

---

## Key Features

* **Dynamic Grid & Auto-Save:** Start with a 25-row default grid or expand it as needed. Edits made to card names, due dates, amounts, scheduled markers, or notes save instantly to your browser's local memory (`localStorage`) across sessions.


* **Column Sorting:** Click any table header (**Card**, **Due Date**, **Amount**, **Payment Scheduled**, or **Notes**) to sort the grid in ascending ($\mathbf{\uparrow}$) or descending ($\mathbf{\downarrow}$) order. The **Amount** column sorts numerically, ignoring currency symbols (e.g., `$100.00` vs `$12.84`).


* **Interactive Row Management:**
* **Add Rows:** Easily add empty rows to the bottom of your tracker using the **+ Add Row** button.


* **Delete Rows:** Remove individual rows anytime using the **×** button on the right side of each row.




* **Smart Row Highlighting:** Automatic, real-time color-coding based on due dates and payment status:


* **Pink:** Date updated/changed and pending payment confirmation.


* **Blue:** Payment scheduled for a bill whose due date has passed.


* **Green:** Payment scheduled for an upcoming or current bill.


* **Red:** Past due and unpaid.


* **Yellow:** Due within the next 7 days and unpaid.




* **Customizable Appearance:**
* **Color Customizer:** Adjust highlight colors and text colors using native color pickers.


* **Zebra Striping Contrast:** Adjust a slider (from 0% to 50% darker) to tune the contrast of even-numbered rows for maximum readability when adjacent rows are highlighted.


* **Bold Grid Lines:** 1.5px high-contrast borders for visual clarity.




* **CSV Import & Export:**
* **Export CSV:** Save your grid to a formatted `.csv` file for backups or record-keeping.


* **Flexible Import:** Imports ISO (`YYYY-MM-DD`) or US (`MM/DD/YY`) date formats seamlessly.


* **Smart Import Prompt:** When importing into a grid that already contains data, choose to either **Append** the new rows to the bottom or **Replace** the existing grid completely.





---

## How to Use

### 1. Running the Application

No installation or local server is required.

1. Save `index.html` on your computer.


2. Double-click `index.html` (or right-click and open it with your preferred web browser).



### 2. Entering Data & Sorting

* **Card / Bill Name:** Type the card or bill name in the first column.


* **Due Date:** Select a date using the built-in browser date picker.


* *Note:* Modifying an existing due date automatically clears the **Payment Scheduled** field and highlights the row in **Pink** to prompt review.




* **Amount:** Enter the payment amount (e.g., `$12.84`).


* **Payment Scheduled:** Type `x` when a payment is scheduled. This clears the date-updated flag and triggers the green or blue highlight rule.


* **Notes:** Enter additional notes or account info.


* **Sort Columns:** Click any header (e.g., **Due Date** or **Amount**) to toggle ascending or descending order.


* **Delete Row:** Click the red **×** button on the far right of any row to remove it.



### 3. Managing Color & Theme Settings

1. Click **Color Settings** in the top navigation bar.


2. Use the color pickers to customize the **Grid Text Color** or any of the 5 status highlights.


3. Adjust the **Zebra Striping Contrast** slider to make even-numbered rows lighter or up to 50% darker.


4. Click **Reset Defaults** anytime to restore the original color palette.



### 4. Importing & Exporting Data

* **Export CSV:** Downloads a file named `payment_tracker_YYYY-MM-DD.csv` containing your current grid contents.


* **Import CSV:** Choose a `.csv` file to load. If existing data is detected, a pop-up prompt will ask whether to **Append** the rows or **Replace** the current grid.


* **Clear All:** Clears all data and wipes the grid from `localStorage` after confirmation.



---

## CSV File Format

CSV files can be imported with or without header rows. The tracker maps the first 5 columns as follows:

```csv
card,due date,amount,payment scheduled,notes
omega rewards,08/22/26,$45.12,x,
atlas auto loan,09/02/26,$210.00,x,bi-weekly payment
zenith utility,09/15/26,$88.50,,autopay on file

```

---

## Technical Overview

* **Format:** Single `.html` file containing HTML, CSS, and plain JavaScript.


* **Dependencies:** None (No external libraries, frameworks, or CDNs required).


* **Storage Keys:** Uses `payment_tracker_grid_data` for row contents and `payment_tracker_color_settings` for custom themes.


* **Privacy:** 100% local-first—no data is sent over the internet.
