import csv
import random

with open("en_ewt-ud-train.conllu", "r") as f, open("Cleaned EWT.txt", "w") as out:
    csv_file = open("EWT.csv", "w", newline='')
    csv_out = csv.writer(csv_file)
    
    current_doc = ""
    
    for line in f:
        if line.startswith('# newdoc'):
            out.write("\n")
            csv_out.writerow([current_doc])  # Write to CSV
            current_doc = ""
        elif line.startswith('# text '):
            current_line = line.replace("\n", " ")
            out.write(current_line[9:])  # Write the text after '# text '
            current_doc += current_line[9:] + " "
        
    csv_file.close()

    with open("EWT.csv", "r", newline='') as f:
        rows = list(csv.reader(f))

    random.shuffle(rows)

    with open("EWT.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
