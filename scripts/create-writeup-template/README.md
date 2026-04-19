# Create Write-up Template

This script creates a new reversing challenge folder with this structure:

```text
<output-directory>/
└── <challenge-name>/
	├── image-evidences/
	└── write-up.md
```

## Requirements

- Python 3.8 or newer
- No third-party packages required

## Usage

Run the script with a challenge name and an output directory:

```bash
python3 create-template.py <challenge-name> <output-directory>
```

If you want to overwrite an existing `write-up.md`, add `--force`:

```bash
python3 create-template.py <challenge-name> <output-directory> --force
```

## Examples

### Linux

```bash
python3 create-template.py easy_crack ../../challenge-writeups/
```

If the script is executable, you can also run:

```bash
./create-template.py easy_crack ./writeups
```

### macOS

```bash
python3 create-template.py easy_crack ../../challenge-writeups/
```

Optional executable mode:

```bash
chmod +x create-template.py
./create-template.py easy_crack ../../challenge-writeups/
```

### Windows

```powershell
python create-template.py easy_crack ../../challenge-writeups/
```

If `python` is not available, try the Python Launcher:

```powershell
py create-template.py easy_crack ../../challenge-writeups/
```

## Notes

- The challenge folder name is normalized to a slug format.
- The script creates `image-evidences/` automatically.
- The script does not overwrite `write-up.md` unless `--force` is used.
- Use a short challenge name if you want a clean folder name.
