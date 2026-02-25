import xml.etree.ElementTree as ET
import os
import time

def run_vulnerable_test(file_path):

    print(f"[*] Attempting to parse: {file_path}")
    print("[!] WARNING: This may cause a temporary spike in RAM usage.")
    
    start_time = time.time()
    try:
        # Standard ElementTree is often vulnerable to entity expansion
        tree = ET.parse(file_path)
        
        # Accessing the text forces the parser to expand the entities
        content_preview = ET.tostring(tree.getroot(), encoding='utf-8')[:50] if tree.getroot() is not None else "No text content"
        print(f"[+] Successfully parsed. Preview: {content_preview}...")
        print(f"[+] Size: {len(ET.tostring(tree.getroot(), encoding='utf-8'))} bytes")
    
    except Exception as e:
        print(f"[X] Execution failed: {e}")
    
    end_time = time.time()
    print(f"[*] Process took {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    # sample_file = "samples/explosive_sample.xml"
    sample_file = "./samples/safe_sample.xml"
    if os.path.exists(sample_file):
        run_vulnerable_test(sample_file)
    else:
        print(f"[X] Error: {sample_file} not found.")