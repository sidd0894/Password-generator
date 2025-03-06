# Strong Password Generator

This password generator creates strong, secure, and random passwords. You can specify both the length of the password and the number of passwords you want to generate.

## Features
1. **Customizable Password Length**: Specify the length of the password (minimum 8 characters).
2. **Multiple Password Generation**: Generate multiple passwords at once.
3. **Copy to Clipboard**: Easily copy generated passwords for convenient use.

## Requirements

You can install the required dependencies listed in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Running the Program

The program generates random passwords based on user-defined parameters through command-line arguments. Below are the details for using these arguments:

### Arguments

- `--length` / (`-len`): **Optional**  
  Specifies the length of the generated password. The default length is `16`.  
  Example: `--length 12` (Generates a 12-character password).

- `--pass-count` / (`-count`): **Optional**  
  Specifies how many passwords to generate. The default is `1`.  
  Example: `--pass-count 5` (Generates 5 passwords).

- `--show-pass` / (`-show`): **Optional**  
  This flag, when provided, will display the generated password(s).  
  Example: `--show-pass` (Displays the generated password(s)).

### Examples

1. **Generate a single password of length 16:**
   ```bash
   python password-generator.py --length 16
   ```
   This will generate a single password of length 16 and copy it to the clipboard.

2. **Generate 5 passwords of length 12:**
   ```bash
   python password-generator.py --length 12 --pass-count 5
   ```
   This will generate 5 passwords, each 12 characters long, and copy them to the clipboard.

3. **Generate and display a single password of length 16:**
   ```bash
   python password-generator.py --length 16 --show-pass
   ```
   This will generate and display a single password, and copy it to the clipboard.

4. **Generate and display 3 passwords of length 8:**
   ```bash
   python password-generator.py --length 8 --pass-count 3 --show-pass
   ```
   This will generate 3 passwords, each 8 characters long, display them, and copy them to the clipboard.

## Note

- If the `--show-pass` / `-show` flag is not provided, the program will directly copy the password(s) to the clipboard without displaying them.