# 📄 PDF Table & Image Extraction with Python  

## 📌 Summary
This script extracts both **tables** and **images** from a PDF document using `pdf2image` and `unstructured.partition.pdf`, with visualization support via Matplotlib.  

- **PDF Conversion**  
  - Converts each page of `arso.pdf` into high-resolution images with `pdf2image.convert_from_path`.  

- **PDF Partitioning**  
  - Uses `unstructured.partition.pdf` to parse the PDF into structured elements.  
  - Extracts elements categorized as `"Table"` or `"Image"`.  

- **Table Handling**  
  - Prints the **first extracted table** as HTML (if available) using `metadata.text_as_html`.  

- **Image Cropping & Visualization**  
  - Identifies image bounding coordinates (`metadata.coordinates.points`).  
  - Crops regions with padding from page images.  
  - Displays cropped images with Matplotlib.  

---

## 🔧 Suggested Improvements

1. **Add Error Handling**  
   - Validate for missing PDF, empty tables, or invalid coordinates before processing.  

2. **Export Results**  
   - Save extracted tables as `.csv` / `.xlsx` and images as `.png` for reuse.  

3. **Batch Image Handling**  
   - Instead of showing images one by one, generate a grid view or save all cropped regions automatically.  

4. **Configurable Parameters**  
   - Allow CLI or config file input for PDF name, DPI, and padding instead of hardcoding.  

5. **Integrate OCR**  
   - Use `pytesseract` or similar OCR to extract text from cropped image regions when no table text is available.  

---

## 🚀 Alternative Approaches & Models

- **Approach 1: Camelot / Tabula**  
  *Use specialized table extraction libraries like Camelot or Tabula for more reliable PDF table parsing.*  

- **Approach 2: LayoutLMv3**  
  *Apply transformer-based document AI models for better detection of structured regions (tables, figures, text).*  

- **Approach 3: Hybrid Workflow with LLMs**  
  *Combine PDF parsing with an LLM (e.g., Llama-3 or Claude) to summarize or describe extracted tables and images automatically.*  
