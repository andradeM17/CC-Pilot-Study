import subprocess
import os

# List of dataset names
datasets = [
    "Statmt-news_commentary-18.1-eng"
]

# Output directory
outdir = "wmt-data"
os.makedirs(outdir, exist_ok=True)

# Run mtdata echo for each dataset and save to numbered files
for i, dataset in enumerate(datasets, start=1):
    result = subprocess.run(
        ["mtdata", "echo", dataset],
        capture_output=True,
        text=True,
        check=True
    )
    outfile = os.path.join(outdir, f"{i}.txt")
    with open(outfile, "w") as f:
        f.write(result.stdout)
    print(f"Created {outfile} for {dataset}")

# To extract data through the command line, you can use:
#mtdata echo <dataset_name> | cut -f1 | head -n 50 > <file_to_save_to>.txt