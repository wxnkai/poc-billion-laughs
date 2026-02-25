# Note: Requires 'pip install defusedxml'
from defusedxml.ElementTree import parse
from defusedxml import EntitiesForbidden
import os

def run_secure_test(file_path):
    print(f"[*] Securely parsing: {file_path}")
    
    try:
        # defusedxml explicitly forbids entity expansion by default
        tree = parse(file_path)
        print("[+] File parsed (This should not happen with a bomb).")
        
    except EntitiesForbidden:
        print("[+] Blocked: defusedxml detected an XML Bomb and blocked it.")
        print("[*] Reason: DTD Entities are forbidden in this secure configuration.")
        
    except Exception as e:
        print(f"[X] An unexpected error occurred: {e}")

if __name__ == "__main__":
    # sample_file = "samples/explosive_sample.xml"
    sample_file = "./samples/safe_sample.xml"
    if os.path.exists(sample_file):
        run_secure_test(sample_file)
    else:
        print(f"[X] Error: {sample_file} not found.")