# BackuPy

BackuPy is a command-line tool for seamless filesystem backups and directory synchronization. It focuses on incremental updates, transferring only changed files, and helping you maintain mirrored directories with minimal hassle.

## Features

- **Incremental Backups:** Quickly detect and sync only modified files.
- **Flexible Commands:** Easily run `backup`, `restore`, and `sync` operations.
- **Cross-Platform:** Works on Windows, macOS, and Linux.
- **Clear Logging:** View progress and diagnostics, with logs saved for troubleshooting.

## Installation

```bash
pip install backupy
```

This will install the `backupy` command globally, ready to run from your terminal.

## Usage

```bash
# Backup a directory to a specified location
backupy backup /path/to/source /path/to/destination

# Sync changes from source to destination
backupy sync /path/to/source /path/to/destination

# Restore a backup from destination to source
backupy restore /path/to/destination /path/to/source
```

### Common Options

- `--dry-run`: Show which files would be transferred without making changes.
- `--verbose`: Enable detailed logging and progress messages.
- `--config`: Specify a configuration file for custom settings.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements, bug fixes, or new features.

## License

BackuPy is released under the [MIT License](LICENSE).
