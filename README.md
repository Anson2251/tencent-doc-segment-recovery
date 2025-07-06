# Tencent Doc PDF Segment Recovery Tool

A toolkit to reconstruct complete PDFs from segmented Tencent Doc downloads

## Overview

This toolkit enables recovery of PDF documents from Tencent Doc by:

1. Extracting PDF segments from HAR files
2. Analyzing PDF object IDs
3. Reordering segments correctly
4. Merging into a final PDF

*Note: This tool is designed for downloading documents you have access to view but lack download permissions for.*

## Disclaimer

> [!CAUTION]
> This tool is provided for educational and research purposes only. Users are responsible for ensuring they have proper authorisation to access and download any documents.
>
> - The tool should only be used on documents you have legitimate access to view
> - Respect all copyright laws and terms of service
> - The authors assume no liability for misuse of this tool
> - No warranty is provided, use at your own risk

## Prerequisites

- Python 3
- Chrome/Firefox developer tools

## Toolkit Components

### `harextract.html`

- Converts HAR files to ordered PDF segments (file0.pdf, file1.pdf, etc.)
- Preserves original network request order
- **Usage**: Open in browser and upload HAR file

### `pdf_obj_num_range.py`

- Extracts PDF object ID ranges from segments
- Outputs CSV with `filename, first_obj_num, last_obj_num`
- **Usage**: `python pdf_obj_num_range.py > ranges.csv`

### `batch_rename.py`

- Renames files according to CSV mapping
- CSV format: `original_name,new_name`
- **Usage**: `python batch_rename.py rename_table.csv`

### `merge.sh`

- Concatenates sorted PDF segments
- Outputs to `merged.pdf`
- **Usage**: `./merge.sh`

## Workflow Steps

> [!NOTE]
> If the file is relatively small (likely < 1 MiB), Tencent Doc will not split the document into multiple segments. In this case, you can download that PDF file directly in developer tools and skip all steps in the workflow below.

### 0. Collect All the Segments

1. Open Tencent Doc in browser
2. Refresh the page
3. Scroll the document down to the end slowly to ensure all segments are loaded

> [!IMPORTANT]
> Ensure all segments are loaded before saving the HAR file. If not, repeat the steps.

### 1. Extract PDF Segments

1. Filter network requests for PDF segments by developer tools (in network panel)

2. Save as HAR file

> [!TIP]
> Sometimes by using the url to filter `https://docs.qq.com/api/pdf-loader/load`

### 2. Convert HAR to PDF Segments

Use `harextract.html` to convert HAR to ordered PDF segments (file0.pdf, file1.pdf, etc.)

### 3. Extract Object ID Ranges

Since the PDF format states that object IDs are unique and sorted, we can use this property to sort the segments.

Run in the folder containing the PDF segments:

```bash
python pdf_obj_num_range.py > ranges.csv
```

Expected output format:

```csv
filename, first_obj_num, last_obj_num
```

### 4. Sort Segments in Excel

1. Open ranges.csv
2. Sort by first_obj_num (ascending)
3. Create another table for rename mapping:
   - Column A: Original filename (`fileX.pdf`, e.g. `file0.pdf`)
   - Column B: New filename (`sortedX`, e.g. `sorted1`)

Example:

||A|B|
|:--|:--|:--|
|1|file0.pdf|sorted1|
|2|file1.pdf|sorted2|

### 5. Batch Rename Files

Run:

```bash
python batch_rename.py rename_table.csv
```

### 6. Merge Final PDF

Run:

```bash
./merge.sh
```

Outputs: merged.pdf

## Troubleshooting

- **N/A object IDs**: Some segments may show N/A when extracting the object ID ranges.

    May need manual placement in the rename table.

    However, these chunks do not affect the final output, as they are 'resource chunks'. The only issue is the validity of the resources (e.g. some images may be broken).

- **Missing files**: Ensure all segments are present before merging

## Credits

HAR Extractor is modified from [HAR Extractor](https://github.com/JC3/harextract), licenced under GPL-3.0.

---

Last update: 2025-07-06
