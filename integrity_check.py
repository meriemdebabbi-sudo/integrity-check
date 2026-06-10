import hashlib
import json
import os
import sys

HASH_DB = "hashes.json"

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

def load_hashes():
    if os.path.exists(HASH_DB):
        try:
            with open(HASH_DB, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_hashes(data):
    with open(HASH_DB, "w") as f:
        json.dump(data, f, indent=4)

def initialize(path):
    hashes = load_hashes()

    files = get_files(path)

    for file in files:
        hashes[file] = calculate_hash(file)

    save_hashes(hashes)

    print("Hashes stored successfully.")

#initialize("test.log")
def get_files(path):
    files = []

    if os.path.isfile(path):
        files.append(path)

    elif os.path.isdir(path):
        for file in os.listdir(path):
            full_path = os.path.join(path, file)

            if os.path.isfile(full_path):
                files.append(full_path)

    return files
def check_file(path):
    hashes = load_hashes()

    for file in hashes:
        if not os.path.exists(file):
            print(f"{file}: Missing")

    files = get_files(path)

    for file in files:

        if file not in hashes:
            print(f"{file}: Not initialized")
            continue

        current_hash = calculate_hash(file)

        if current_hash == hashes[file]:
            print(f"{file}: Unmodified")
        else:
            print(f"{file}: Modified (Hash mismatch)")

def update_hash(path):
    hashes = load_hashes()

    files = get_files(path)

    for file in files:
        hashes[file] = calculate_hash(file)

    save_hashes(hashes)

    print("Hash updated successfully.")

if len(sys.argv) != 3:
    print("Usage:")
    print("python3 integrity_check.py [init|check|update] <path>")
    sys.exit(1)

command = sys.argv[1]
path = sys.argv[2]

if command == "init":
    initialize(path)

elif command == "check":
    check_file(path)

elif command == "update":
    update_hash(path)

else:
    print("Unknown command")

def get_files(path):
    files = []

    if os.path.isfile(path):
        files.append(path)

    elif os.path.isdir(path):
        for file in os.listdir(path):
            full_path = os.path.join(path, file)

            if os.path.isfile(full_path):
                files.append(full_path)

    return files