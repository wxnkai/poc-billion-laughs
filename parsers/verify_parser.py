import xml.etree.ElementTree as ET
import os

def verify_safe_xml(file_path):
    if not os.path.exists(file_path):
        print(f"[X] Error: {file_path} not found.")
        return

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        print(f"--- Verification of {file_path} ---")
        # Accessing specific tags to show successful parsing
        project_name = root.find('.//name').text
        author = root.find('.//author').text
        description = root.find('.//description').text

        print(f"Project:     {project_name}")
        print(f"Researcher:  {author}")
        print(f"Description: {description}")
        print("---------------------------------")
        print("[+] Control file verified and readable.")

    except Exception as e:
        print(f"[X] Parsing failed: {e}")

if __name__ == "__main__":
    verify_safe_xml("./samples/safe_sample.xml")