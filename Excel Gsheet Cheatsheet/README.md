# Excel ↔ Google Sheets — Master Data Analysis Cheat Sheet

A side-by-side reference for 44 of the most useful Excel and Google Sheets functions and features, delivered as a filterable, sortable spreadsheet. Built so the formulas live where you'd actually use them.

## What's inside

`Excel_GoogleSheets_Cheatsheet.xlsx` — three tabs:

### 1. Master Cheat Sheet
All 44 functions and features, grouped into 9 categories:

- **Basic Aggregation** — SUM, AVERAGE, COUNT, MAX, MIN
- **Logic & Lookup** — IF, VLOOKUP, XLOOKUP, INDEX/MATCH
- **Conditional Aggregation** — COUNTIF(S), SUMIF(S), AVERAGEIFS
- **Statistics** — RANK, QUARTILE, PERCENTILE, RANDBETWEEN, FORECAST.ETS
- **Text** — CONCATENATE, LEFT/RIGHT/MID, case functions, Text-to-Columns
- **Arrays & Matrices** — array formulas, TRANSPOSE, MMULT, MINVERSE, MUNIT
- **Database functions** — DSUM, DAVERAGE, DCOUNT
- **Data tools & features** — PivotTables, slicers, named ranges, validation, charts
- **Power tools / analysis** — Power Query, Analysis ToolPak, Solver, Goal Seek, 3D formulas, macros

Each row shows the **Excel** formula and the **Google Sheets** formula side by side, plus a Notes column. Use the header dropdowns (row 4) to filter or sort.

### 2. Live Examples
A small sales dataset with 12 real, working formulas. Edit any number and every result recalculates. These formulas work identically in both apps.

### 3. Read Me
In-workbook guide to the tabs, the Notes column, and the key differences.

## How to use

1. Open `Excel_GoogleSheets_Cheatsheet.xlsx` in Excel or upload it to Google Sheets.
2. Browse by category, or use the filter dropdowns on the Master Cheat Sheet to find a function.
3. Copy the formula from the column for your app.
4. Try the Live Examples tab to see formulas compute on real data.

## Key differences at a glance

Rows marked with a ★ (amber highlight) flag a real difference. The biggest **Excel-only** items with no direct Google Sheets equivalent:

- Power Query (Get & Transform)
- Data Analysis ToolPak (regression, ANOVA, correlation)
- Built-in Solver and Goal Seek
- 3D cross-sheet references — `=SUM(Sheet1:Sheet3!B2)`
- FORECAST.ETS, MUNIT
- VBA macros

**Google Sheets advantages:**

- `ARRAYFORMULA` for easy whole-column formulas
- `IMPORTRANGE` for live data across files
- Filter Views (per-user filters)
- Apps Script (JavaScript) for cloud automation

Most other formulas are **identical** in both apps. In Excel 365, many older array formulas now "spill" automatically like Google Sheets — so the two are converging.

## Notes

- All 84 live formulas verified with zero errors.
- The formula columns on the Master sheet are stored as text so they display literally (as a reference), not computed.

## Source

Reshaped and expanded from a 44-item Excel data-analysis reference, with Google Sheets equivalents and a few modern functions (XLOOKUP, INDEX/MATCH) added.
