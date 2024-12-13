# Vipyr

Vipyr is a Python-powered CLI toolkit for network operations and monitoring. It combines common diagnostics like ping checks, DNS lookups, and port scans into one versatile tool. Vipyr’s goal is to help you quickly identify network issues, gather data, and streamline troubleshooting.

## Features

- **Ping & DNS Checks:** Test host reachability and resolve DNS records.
- **Port Scanning:** Quickly see which ports are open on a target host.
- **Concurrent Operations:** Run multiple checks in parallel for faster results.
- **Customizable Output:** Choose between human-readable or JSON-formatted output.

## Installation

```bash
pip install vipyr
```

This command makes `vipyr` available system-wide, ready to assist with network diagnostics.

## Usage

```bash
# Ping a host
vipyr ping example.com

# Perform a DNS lookup
vipyr dns example.com

# Scan common ports on a host
vipyr scan example.com

# Get a system status summary
vipyr status
```

### Common Options

- `--verbose`: Increase output detail.
- `--json`: Return results in JSON format for easy scripting.
- `--concurrency N`: Control the number of concurrent operations.

## Contributing

Interested in improving Vipyr? Open an issue, suggest a feature, or submit a pull request to help make Vipyr even better.

## License

Vipyr is released under the [MIT License](LICENSE).
