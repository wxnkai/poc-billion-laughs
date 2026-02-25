# Billion Laughs Attack: XML Entity Expansion Lab

## 📌 Overview
This repository is a security research project focused on the **Billion Laughs Attack** (also known as an **XML Bomb**). This project demonstrates how recursive entity expansion can lead to an exponential increase in resource consumption, resulting in a **Denial of Service (DoS)**.

The lab compares legacy vulnerable parsing methods against modern, hardened parsing libraries to illustrate the evolution of XML security.

## 📂 Project Structure
The project is organized as follows:

* **`parsers/`**: Contains the logic for different parsing scenarios.
    * `vulnerable_parser.py`: Demonstrates the exploit using standard libraries (and the barriers modern versions place in our way).
    * `secure_parser.py`: Implementation of a safe parser using the `defusedxml` library.
    * `verify_parser.py`: A utility script to ensure the environment is correctly parsing legitimate XML data.
* **`samples/`**: XML files used for testing.
    * `explosive_sample.xml`: The recursive payload designed for exponential growth.
    * `safe_sample.xml`: A standard, non-malicious XML file for baseline testing.
* **`requirements.txt`**: Lists necessary dependencies (e.g., `defusedxml`).
* **`.gitignore`**: Configured to ignore virtual environments and cached files.
* **`LICENSE`**: MIT License.

## ⚡ The Science of the "Bomb"
The attack leverages the **Document Type Definition (DTD)** to define entities that refer to one another. 

### Expansion Logic
The growth is exponential rather than linear:
* `&l0;` = "payload" (7 bytes)
* `&l1;` = 10 `&l0;` references
* `&l2;` = 10 `&l1;` references
* ...
* `&l9;` = $10^9$ (1 billion) instances of the base payload.

### 🛑 Modern Mitigations Encountered
During this lab, you may encounter the error:
`Maximum entity amplification factor exceeded`

This is a **Security-by-Default** feature in modern C-libraries (like `libxml2`). It monitors the ratio between the input file size and the resulting expansion. If the ratio (Amplification Factor) is too high, the parser kills the process to prevent a system crash.

## 🧪 How to Run the Lab

### 1. Environment Setup
```bash
# It is recommended to use a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Verification
Ensure the parser is working correctly with safe data:
```bash
python parsers/verify_parser.py
```

### 3. Test the Vulnerability
Observe how modern parsers handle the recursive entity and trigger security limits:
```bash
python parsers/vulnerable_parser.py
```

### 4. Test the Mitigation
Observe how specialized libraries like `defusedxml` provide more granular security by forbidding DTDs entirely:
```bash
python parsers/secure_parser.py
```

## ⚠️ Disclaimer
This project is for educational and portfolio purposes only. I am not responsible for the misuse of the code provided. Do not use these scripts against systems you do not have explicit permission to test.