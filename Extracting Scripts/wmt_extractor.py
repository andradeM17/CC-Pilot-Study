import xml.etree.ElementTree as ET
import csv
import sys
import random

def xml_to_csv(xml_file_path, csv_file_path):
    """
    Convert XML file to CSV with ID and Text columns.
    
    Args:
        xml_file_path (str): Path to the input XML file
        csv_file_path (str): Path to the output CSV file
    """
    try:
        # Parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        
        # Open CSV file for writing
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header
            writer.writerow(['ID', 'Text'])
            
            # Find all doc elements and extract document id and concatenated text
            for doc in root.findall('.//doc'):
                doc_id = doc.get('id')
                
                # Find all seg elements within this document and concatenate their text
                seg_texts = []
                for seg in doc.findall('.//seg'):
                    seg_text = seg.text.strip() if seg.text else ''
                    if seg_text:
                        seg_texts.append(seg_text)
                
                # Join all segment texts with a space
                combined_text = ' '.join(seg_texts)
                
                # Write row to CSV
                writer.writerow([doc_id, combined_text])
        
        print(f"Successfully converted XML to CSV: {csv_file_path}")
        
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: XML file '{xml_file_path}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    # Get file paths from command line arguments or use defaults
    if len(sys.argv) == 3:
        xml_file = sys.argv[1]
        csv_file = sys.argv[2]
    else:
        xml_file = input("Enter XML file path: ")
        csv_file = input("Enter CSV output file path: ")
    
    # Convert XML file to CSV

if __name__ == "__main__":
    # ...existing code...
    xml_to_csv(xml_file, csv_file)

    # Randomize CSV rows (excluding header)
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = list(csv.reader(f))
        header, rows = reader[0], reader[1:]
        random.shuffle(rows)
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
