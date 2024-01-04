# Siamkatze

Siamkatze is a Python script designed to find and manage broken symbolic links within a specified directory.

## Features

- **Find Broken Symbolic Links**: The main feature of Siamkatze is to identify and report broken symbolic links under the given directory.

- **Recursive Search**: Siamkatze provides an option to perform a recursive search, allowing you to scan subdirectories for broken symbolic links.

- **Delete Broken Links**: For added convenience, Siamkatze includes an option to delete the identified broken symbolic links.

## Usage

```bash
python siamkatze.py [-h] [-r] [-d] directory_path
```

### Arguments

- `directory_path`: The path to the directory where Siamkatze will start searching for broken symbolic links.

### Options

- `-h, --help`: Show the help message and exit.

- `-r, --recursive`: Enable recursive search to find broken symbolic links in subdirectories.

- `-d, --delete`: Enable this option to delete the broken symbolic links found.

## Example

To find and list broken symbolic links in the current directory, run:

```bash
python siamkatze.py .
```

To perform a recursive search and delete the broken symbolic links:

```bash
python siamkatze.py -r -d /path/to/directory
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributions

Contributions are welcome! Please check the [contribution guidelines](CONTRIBUTING.md) before making any contributions.

## Issues

If you encounter any issues or have suggestions, please [open an issue](https://github.com/yourusername/siamkatze/issues).

```