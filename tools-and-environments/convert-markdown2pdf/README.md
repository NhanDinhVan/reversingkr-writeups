# Markdown → PDF Converter (md2pdf)

This tool provides a simple and consistent way to convert Markdown write-ups in this repository into clean, readable PDF documents using `md2pdf` with custom CSS styling.

## Why this tool?

Raw Markdown often renders inconsistently when converted to PDF, especially for:
- Images (oversized or misaligned)
- Code blocks
- Spacing and layout

This setup solves those issues by applying a custom CSS file (`md2pdf.css`) to control formatting and improve readability.

---

## Installation

Install the required tool with CLI support:

```bash
pip install md2pdf[cli]
```

If you encounter missing dependency errors:

```bash
pip install typer
```

---

## Usage

From inside a write-up folder (or any directory containing a Markdown file):

```bash
md2pdf --input write-up.md --output write-up.pdf --css md2pdf.css
```

### Example

```bash
md2pdf --input README.md --output README.pdf --css ../../tools-and-environments/convert-markdown2pdf/md2pdf.css md2pdf.css
```

---

## CSS Styling

The file `md2pdf.css` controls how the PDF looks.

For example:

```css
img {
  max-width: 70%;
  height: auto;
  display: block;
  margin: auto;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
}
```

This ensures:

* Images are not oversized
* Content is centered and readable
* Layout is consistent across all write-ups

---

## Notes

* Prefer standard Markdown image syntax (`![]()`) instead of raw HTML for better compatibility
* Keep image paths relative to the Markdown file
* If images do not appear, check file paths and ensure they are accessible

---

## Future Improvements

* Add syntax highlighting themes
* Improve typography for long-form write-ups
* Automate batch conversion for all challenges
