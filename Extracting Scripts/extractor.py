import gzip
import shutil
import sys
import os

def extract_gz(gz_path, out_path=None):
    if out_path is None:
        if gz_path.endswith('.gz'):
            out_path = gz_path[:-3]
        else:
            out_path = gz_path + '.out'
    with gzip.open(gz_path, 'rb') as f_in, open(out_path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    print(f"Extracted: {out_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extractor.py <file.gz> [output_file]")
        sys.exit(1)
    gz_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else None
    extract_gz(gz_file, out_file)