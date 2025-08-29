import zipfile
import os
import random
import xml.etree.ElementTree as ET
import csv

# === CONFIG ===
zip_path = '/home/intern/Downloads/ga.zip'  # Path to your .zip file
output_txt_dir = 'extracted_texts'          # Directory to save .txt files
output_csv_path = '/home/intern/Downloads/first_40_lines.csv'      # Path to save .csv summary
base_path = 'EUbookshop/xml/ga/'            # Base folder inside the zip
num_files = 2                               # Number of files to extract
lines_to_csv = 40                           # Number of lines per file for CSV

def extract_lines_from_xml(xml_content):
    """Extracts lines of words from each <s> block."""
    try:
        root = ET.fromstring(xml_content)
    except ET.ParseError as e:
        print(f"Parse error: {e}")
        return []
    lines = []
    for s in root.iter('s'):
        words = [w.text for w in s.iter('w') if w.text]
        if words:
            lines.append(' '.join(words))
    return lines

def extract_and_save(zip_path, output_txt_dir, output_csv_path, base_path, num_files, lines_to_csv):
    csv_rows = []
    os.makedirs(output_txt_dir, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zipf:
        file_list = [f for f in zipf.namelist() if f.startswith(base_path) and f.endswith('.xml')]
        print(f"Total XML files found: {len(file_list)}")

        if len(file_list) < num_files:
            raise ValueError("Not enough XML files to sample.")

        selected_files = random.sample(file_list, num_files)

        for file in selected_files:
            with zipf.open(file) as xml_file:
                xml_content = xml_file.read().decode('utf-8')

            lines = extract_lines_from_xml(xml_content)

            # Save full text to .txt file
            base_filename = os.path.splitext(os.path.basename(file))[0]
            txt_path = os.path.join(output_txt_dir, base_filename + '.txt')
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write('\n'.join(lines))

            # Join first 20 lines into one multi-line string
            first_20_text_block = '\n'.join(lines[:lines_to_csv])
            csv_rows.append([base_filename, first_20_text_block])

            print(f"Processed: {file} -> {txt_path}")

    # Write to CSV with newline-containing cells
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Filename', 'First40Lines'])  # Header
        writer.writerows(csv_rows)

    print(f"CSV saved to: {output_csv_path}")

# === Run it ===
extract_and_save(zip_path, output_txt_dir, output_csv_path, base_path, num_files, lines_to_csv)
