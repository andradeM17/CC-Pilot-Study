import subprocess
import os

# List of dataset names
datasets = [
    "OPUS-news_commentary-v16-eng-zho"
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
# Linux: mtdata echo <dataset_name> | cut -f1 | head -n 50 > <file_to_save_to>.txt
# Windows (PowerShell): mtdata echo <dataset_name> | ForEach-Object { ($_ -split "`t")[0] } | Select-Object -First 50 > <file_to_save_to>.txt