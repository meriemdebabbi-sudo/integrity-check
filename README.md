# Log File Integrity Checker

A Python-based tool that verifies the integrity of log files using SHA-256 hashing. The tool helps detect unauthorized modifications, missing files, and newly added files by comparing current file hashes with previously stored references.

## Features

- Compute SHA-256 hashes for log files.
- Store hashes in a local JSON database.
- Verify file integrity and detect tampering.
- Detect modified files.
- Detect missing files.
- Detect uninitialized files.
- Support both single files and directories.
- Update stored hashes when changes are legitimate.
- Provide clear status reports for monitored files.


## Project Structure

integrity-check/
│
├── integrity_check.py   # Main Python script
├── hashes.json          # Stores file hashes
└── README.md            # Project documentation



## Requirements

- Python 3.10 or higher
- Linux/Ubuntu environment (recommended)


## Usage

### 1. Initialize Hashes

Store hashes for a file or all files in a directory.

```bash
python3 integrity_check.py init test.log
```

or

```bash
python3 integrity_check.py init logs/
```

Example output:

Hashes stored successfully.


### 2. Check Integrity

Verify whether files have been modified, deleted, or added.
### for files

```bash
python3 integrity_check.py check test.log
```

or
# for directories

```bash
python3 integrity_check.py check logs/
```

Possible outputs:

#### File has not changed

```text
test.log: Unmodified
```

#### File content has been modified

```text
test.log: Modified (Hash mismatch)
```

#### Monitored file has been deleted

```text
logs/a.log: Missing
```

#### New file exists but has never been initialized

```text
logs/c.log: Not initialized
```

---

### 3. Update Hashes

If modifications are legitimate, update the stored hashes.

```bash
python3 integrity_check.py update test.log
```

or

```bash
python3 integrity_check.py update logs/
```

Example output:

```text
Hash updated successfully.
```

---

## How It Works

1. The tool computes a SHA-256 hash for each monitored file.
2. Hashes are stored in `hashes.json`.
3. During a check operation:
   - If the hash matches, the file is reported as **Unmodified**.
   - If the hash differs, the file is reported as **Modified (Hash mismatch)**.
   - If a monitored file no longer exists, it is reported as **Missing**.
   - If a file exists but has never been initialized, it is reported as **Not initialized**.
4. Any mismatch may indicate file tampering or unauthorized modification.


### Initialize Monitoring

```bash
python3 integrity_check.py init logs/
```

### Verify Integrity

```bash
python3 integrity_check.py check logs/
```

Output:

```text
logs/a.log: Unmodified
logs/b.log: Unmodified
```

### Simulate a Modification

```bash
echo "attack" >> logs/a.log
```

### Detect Tampering

```bash
python3 integrity_check.py check logs/
```

Output:

```text
logs/a.log: Modified (Hash mismatch)
logs/b.log: Unmodified
```

### Accept the New Version

```bash
python3 integrity_check.py update logs/
```

### Verify Again

```bash
python3 integrity_check.py check logs/
```

Output:

```text
logs/a.log: Unmodified
logs/b.log: Unmodified
```

---

## Technologies Used

- Python 3
- hashlib (SHA-256)
- JSON
- OS module
- sys module
- File Integrity Monitoring (FIM) concepts

---

## Future Improvements

- Recursive directory scanning.
- Encryption of the hash database.
- Audit logging and reporting.
- Real-time monitoring using Linux inotify.
- Enhanced command-line interface using argparse.
- Support for additional hashing algorithms.

---

## Learning Outcomes

Through this project, I learned:

- How cryptographic hash functions work.
- How SHA-256 is used for integrity verification.
- How to detect file tampering.
- How to work with files and directories in Python.
- How to store and manage data using JSON.
- How to build a command-line security tool.

---

## Author

**Meriem**

This project was developed as a beginner cybersecurity and Python project to learn file integrity monitoring, hashing algorithms, and secure file verification techniques.