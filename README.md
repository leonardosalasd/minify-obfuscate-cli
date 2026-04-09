# minify-obfuscate-cli

**A high-performance Python orchestrator for automated web asset optimization and source code protection.**

`minify-obfuscate-cli` provides a zero-config build pipeline to minify HTML/CSS and obfuscate JavaScript in bulk. Designed for developers who need to protect their intellectual property and optimize production delivery without manual overhead.

---

## 🚀 Prerequisite Setup

This tool leverages industry-standard engines. You must have **Node.js** installed on your system.

Before running the packer, install the required global dependencies:

```bash
npm install -g javascript-obfuscator clean-css-cli html-minifier-terser
```

---

## 🛠 Usage

The script creates an isolated `/dist_package` directory to prevent overwriting your source code. Each execution generates a unique build folder to maintain version integrity.

### Basic Command
Navigate to the root of the repository and run:

```bash
python src/packer.py "path/to/your/project"
```

### Advanced Flags
You can skip specific processing stages using the following flags:

* `--no-js`: Skips JavaScript obfuscation (useful for debugging).
* `--no-css`: Skips CSS minification.
* `--no-html`: Skips HTML minification.

**Example:**
```bash
python src/packer.py "C:/Projects/MyApp" --no-html
```

---

## 📦 Technical Features

* **Isolated Builds:** Automatic cloning of source files into a distribution-ready folder.
* **JS Protection:** Implements string array encoding (Base64), control-flow flattening, and dead code injection.
* **CSS/HTML Optimization:** Strips comments, whitespace, and redundant tags for minimal payload size.
* **Traceability:** Generates a `build_errors.log` inside the distribution folder if any asset fails to process.

---

## ⭐ Support & Contribution

If this tool streamlines your workflow, consider giving it a **Star**. It supports the development of future security-first utilities.

**License:** MIT  
**Engineering Focused. Security Driven.**