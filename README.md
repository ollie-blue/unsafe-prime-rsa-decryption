# Project: Advanced Cryptographic Forensics & RSA Decryption - S7_Custom2 (Brutal Challenge)

## 📋 Executive Summary

Completed an advanced cryptography and digital forensics challenge involving intercepted RSA-encrypted data (`RSA_Smooth.txt`) and a secondary data file (`75706C6F6164732F323032332F3030302F666C61672E747874.txt`). Leveraged unsafe prime factor analysis (Pollard's p-1 algorithm concepts) via Python (`rsa.py`) to derive private keys (`d`), decrypted target user credentials for `mohammadlotfi.com`, performed automated FTP credential brute-forcing via Hydra, and successfully extracted the hidden flag (`cyberMo{BR4V0_!_533M5_U_907_17}`).

---

## 🛠️ Architecture & Tech Stack

- **Operating System:** Ubuntu Linux / WSL / VS Code Environment
- **Core Language:** Python 3 (Math, Cryptography parsing)
- **Forensics & Attack Tools:** Nmap, THC-Hydra, FTP Client
- **Cryptographic Principles:** RSA Cryptosystem, Unsafe Primes / Sophie Germain Primes, Hexadecimal-to-Decimal conversions

---

## ⚙️ Step-by-Step Implementation

### Step 1: Cryptographic Analysis & Unsafe Prime Evaluation

- Analyzed the intercepted RSA parameters (`n`, `c`, and `e`) provided in hexadecimal format within `RSA_Smooth.txt`.
- Recognized that standard factorization fails due to the use of _unsafe primes_ (where $(p-1)/2$ is not prime), prompting the application of specialized factorization logic to determine large prime factors `p` and `q`.

### Step 2: Python Scripting & RSA Decryption (`rsa.py`)

- Developed `rsa.py` to convert hexadecimal parameters into large decimal values (`dec_n`, `dec_c`, `dec_e`).
- Computed Euler's totient $\phi(n) = (p-1)(q-1)$ and calculated the private decryption exponent `d` using modular inverse (`pow(dec_e, -1, phiN)`).
- Decrypted the ciphertext `c` to reveal the plaintext message containing target access parameters: `user: u385686636.cybermo` and `target: mohammadlotfi.com`.
- Converted the secondary hex-encoded file name (`75706C6F6164732F323032332F3030302F666C61672E747874.txt`) to ASCII to locate the file path: `uploads/2023/000/flag.txt`.

```python
# Core RSA Decryption logic implemented in rsa.py
phiN = (p - 1) * (q - 1)
d = pow(dec_e, -1, phiN)
M = pow(dec_c, d, dec_n)
```

### Step 3: Reconnaissance & Credential Brute-Forcing (Hydra)

- Performed network reconnaissance using nmap mohammadlotfi.com to map active service ports, confirming open FTP (21/tcp), HTTP (80/tcp), and MySQL (3306/tcp) endpoints.
- Generated a password list (passlist.txt) from the extracted file strings and deployed THC-Hydra to execute a targeted brute-force attack against the FTP service for user u385686636.cybermo.
- Successfully retrieved valid FTP credentials (password: Soso123aljg)

```
# Command used for FTP credential recovery via Hydra
hydra -l u385686636.cybermo -P passlist.txt ftp://mohammadlotfi.com -f
```

### Step 4: FTP Access & Flag Extraction

- Connected to the target FTP server (mohammadlotfi.com) using the discovered credentials.
- Navigated remote directories, located flag.txt, and downloaded the file to the local environment.
- Successfully retrieved and verified the final challenge flag: cyberMo{BR4V0_!_533M5_U_907_17}.


## 🧪 Testing & Validation
* Validated that manual hexadecimal-to-decimal parsing correctly yielded the exact prime factors needed to bypass RSA encryption.
* Confirmed that automated FTP credential testing successfully authenticated against the target server without locking out accounts.

## 💡 Key Learnings & Challenges
* Challenge: Handling extremely large hexadecimal numbers in RSA parameters and dealing with weak/unsafe primes that expose keys to specific mathematical factorization vectors
* Solution: Used precise Python mathematical conversions (pow with modular inverse) and combined cryptographic analysis with network utility tools (Hydra).
* Key Takeaway: Gained hands-on proficiency in RSA cryptanalysis, handling composite key structures, file string decoding, and protocol-level credential testing.

## 🚀 Future Improvements
* Build an automated wrapper script to parse raw challenge text files, automatically compute prime factors, and output decrypted credentials in a single execution pipeline.
* Integrate automated FTP/SSH check routines into the decryption script to streamline post-decryption reconnaissance.