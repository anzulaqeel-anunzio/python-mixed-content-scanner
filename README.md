# Mixed Content Scanner

A security tool that scans HTML-like files for "Mixed Content" warnings. It identifies insecure resources (`http://`) specifically being loaded into what are presumed to be secure pages (scripts, images, iframes, styles).

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Targeted Scanning**: Focuses on active resources (`src` and `href` tags in `script`, `img`, `link`, `iframe`).
*   **File Support**: Scans `.html`, `.php`, `.jsp`, `.asp` and other web templates.
*   **Zero Dependencies**: Pure Python.

## Usage

```bash
python run_scanner.py [path]
```

### Examples

**1. Scan Project**
```bash
python run_scanner.py dist/
```

**2. Check Index**
```bash
python run_scanner.py index.html
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
