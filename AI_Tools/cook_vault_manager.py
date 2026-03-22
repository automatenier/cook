import os
import argparse
from cryptography.fernet import Fernet
from pathlib import Path

# Configuration
KEY_FILE = Path(".pass/.master.key")
PASS_DIR = Path(".pass")

def generate_key():
    """Generates a new Fernet key and saves it to the key file."""
    if KEY_FILE.exists():
        print(f"Key file {KEY_FILE} already exists. Skipping generation.")
        return
    
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    print(f"Generated new master key at {KEY_FILE}. KEEP THIS FILE SAFE AND DO NOT COMMIT.")

def load_key():
    """Loads the Fernet key from the key file."""
    if not KEY_FILE.exists():
        raise FileNotFoundError(f"Master key file {KEY_FILE} not found. Generate it first.")
    
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_file(file_path, key):
    """Encrypts a single file using the provided key."""
    f = Fernet(key)
    file_path = Path(file_path)
    
    if file_path.suffix == ".encrypted":
        print(f"Skipping {file_path}, already encrypted.")
        return

    with open(file_path, "rb") as file:
        file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)
    
    output_path = file_path.with_suffix(file_path.suffix + ".encrypted")
    with open(output_path, "wb") as file:
        file.write(encrypted_data)
    
    print(f"Encrypted: {file_path} -> {output_path}")

def decrypt_file(file_path, key):
    """Decrypts a single encrypted file."""
    f = Fernet(key)
    file_path = Path(file_path)
    
    if file_path.suffix != ".encrypted":
        print(f"Skipping {file_path}, not an .encrypted file.")
        return

    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = f.decrypt(encrypted_data)
    
    # Remove .encrypted suffix
    output_path = file_path.with_name(file_path.stem)
    with open(output_path, "wb") as file:
        file.write(decrypted_data)
    
    print(f"Decrypted: {file_path} -> {output_path}")

def process_directory(action, key):
    """Applies encryption/decryption to all relevant files in the .pass directory."""
    files = [f for f in PASS_DIR.iterdir() if f.is_file() and f.name != ".master.key"]
    
    for file_path in files:
        if action == "encrypt":
            encrypt_file(file_path, key)
        elif action == "decrypt":
            decrypt_file(file_path, key)

def decrypt_all():
    """Importable helper to decrypt all files in the .pass directory."""
    try:
        master_key = load_key()
        process_directory("decrypt", master_key)
        return True
    except Exception as e:
        print(f"Failed to auto-unlock vault: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cook Vault Manager - Encryption Tool for .pass")
    parser.add_argument("action", choices=["gen-key", "encrypt", "decrypt"], help="Action to perform")
    parser.add_argument("--file", help="Specific file to process (optional)")
    
    args = parser.parse_args()
    
    if args.action == "gen-key":
        generate_key()
    else:
        try:
            master_key = load_key()
            if args.file:
                if args.action == "encrypt":
                    encrypt_file(args.file, master_key)
                else:
                    decrypt_file(args.file, master_key)
            else:
                process_directory(args.action, master_key)
        except Exception as e:
            print(f"Error: {e}")
