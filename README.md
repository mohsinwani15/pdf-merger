
# PDF Merger and Watermark Adder

This Python script allows you to merge multiple PDF files into a single PDF and then add a watermark to the merged file.

## Requirements

- Python 3.x
- PyPDF2 library

You can install the required library using pip:

```bash
pip install PyPDF2
```

## Usage

### 1. Merging PDFs

To merge multiple PDF files into one, use the following command:

```bash
python script_name.py file1.pdf file2.pdf file3.pdf ...
```

This will merge the specified PDF files into a single file named `merged_file.pdf`.

### 2. Adding a Watermark

After merging, the script will automatically add a watermark to the merged PDF. Ensure you have a watermark file named `wtr.pdf` in the same directory as the script. The watermarked PDF will be saved as `watermarked.pdf`.

### Example

```bash
python script_name.py document1.pdf document2.pdf
```

This command will merge `document1.pdf` and `document2.pdf` into `merged_file.pdf` and then add the watermark from `wtr.pdf` to create `watermarked.pdf`.

## Notes

- The watermark file (`wtr.pdf`) should be a single-page PDF file.
- Ensure the PDF files and the script are in the same directory, or provide the full path to the files.

