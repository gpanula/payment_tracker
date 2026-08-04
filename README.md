# Payment Tracker

A lightweight, local-first web application designed to help you track credit card and bill due dates, payment schedules, and notes. Built as a single, zero-dependency HTML file, it runs directly in your web browser with zero setup or server requirements.

---

## Key Features

* **Dynamic Grid & Auto-Save:** Start with a 25-row default grid or expand it as needed. Edits made to card names, due dates, amounts, scheduled markers, or notes save instantly to your browser's local memory (`localStorage`) across sessions.
* **Auto Currency Formatting & Quick Rollover:** The **Amount** column automatically formats typed numbers into two-decimal currency values on blur (e.g., typing `12.84` becomes `$12.84`). Entering `0` for the amount automatically increments the due date by one month and marks the payment as scheduled (`x`).
* **Column Sorting:** Click any table header (**Card**, **Due Date**, **Amount**, **Payment Scheduled**, or **Notes**) to sort the grid in ascending ($\mathbf{\uparrow}$) or descending ($\mathbf{\downarrow}$) order. The **Amount** column sorts numerically, ignoring currency symbols.
* **Interactive Row Management:** 
  * **Add Rows:** Easily add empty rows to the bottom of your tracker using the **+ Add Row** button.
  * **Delete Rows:** Remove individual rows anytime using the **×** button on the right side of each row.
* **Smart Row Highlighting:** Automatic, real-time color-coding based on due dates and payment status:
  * **Teal / Cyan (`#63becb`):** Date updated/changed and pending payment confirmation.
  * **Blue (`#d0e1fd`):** Payment scheduled for a bill whose due date has passed.
  * **Green (`#e2f0d9`):** Payment scheduled for an upcoming or current bill.
  * **Red (`#ee1b1b`):** Past due and unpaid.
  * **Orange (`#f09138`):** Due within 7 days (unscheduled).
* **Customizable Settings Panel:**
  * **Color Customizer:** Adjust highlight colors and grid text color using native color pickers.
  * **Zebra Striping Contrast:** Adjust a slider (from 0% to 50% darker) to tune the contrast of even-numbered rows for maximum readability across adjacent highlighted rows.
  * **Currency Symbol Switcher:** Easily toggle between global currency symbols.
* **CSV Import & Export:**
  * **Export CSV:** Save your grid to a formatted `.csv` file for backups or record-keeping.
  * **Flexible Import:** Imports ISO (`YYYY-MM-DD`) or US (`MM/DD/YY`) date formats seamlessly.
  * **Smart Import Prompt:** When importing into a grid that already contains data, choose to either **Append** the new rows to the bottom or **Replace** the existing grid completely.

---

## How to Use

### 1. Running the Application
No installation or local server is required.
1. Save `payment-tracker.html` on your computer.
2. Double-click `payment-tracker.html` (or right-click and open it with your preferred web browser).

### 2. Entering Data & Sorting
* **Card / Bill Name:** Type the card or bill name in the first column.
* **Due Date:** Select a date using the built-in browser date picker.
  * *Note:* Modifying an existing due date automatically clears the **Payment Scheduled** field and highlights the row in **Teal** to prompt review.
* **Amount:** Enter the payment amount (e.g., `45.12`). Click away or press enter to auto-apply your chosen currency symbol.
  * *Note:* Entering `0` for the amount automatically increments the due date by one month and marks the payment as scheduled (`x`).
* **Payment Scheduled:** Type `x` when a payment is scheduled. This clears the date-updated flag and triggers the green or blue highlight rule.
* **Notes:** Enter additional notes or account info.
* **Sort Columns:** Click any header (e.g., **Due Date** or **Amount**) to toggle ascending or descending order.
* **Delete Row:** Click the red **×** button on the far right of any row to remove it.

### 3. Managing Settings
1. Click **Settings** in the top navigation bar.
2. Select your preferred **Currency Symbol** (`$`, `€`, `¥`, `£`, `₹`).
3. Use the color pickers to customize the **Grid Text Color** or any of the status highlights.
4. Adjust the **Zebra Striping Contrast** slider to make even-numbered rows lighter or up to 50% darker.
5. Click **Reset Defaults** anytime to restore the default palette and settings.

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
* **Storage Keys:** Uses `payment_tracker_grid_data` for row contents and `payment_tracker_color_settings` for custom settings and themes.
* **Privacy:** 100% local-first—no data is sent over the internet.


