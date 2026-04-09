"""
Web Build Packer

A production-ready Python orchestrator for bulk minification and obfuscation 
of HTML, CSS, and JS assets. 

Requirements:
    - Node.js installed
    - Packages: html-minifier-terser, clean-css-cli, javascript-obfuscator

Usage:
    python src/packer.py <project_directory> [--no-js] [--no-css] [--no-html]
"""
import os
import sys
import shutil
from pathlib import Path
import subprocess
import argparse

# Setup CLI arguments
parser = argparse.ArgumentParser(description="Automated Web Asset Minifier & Obfuscator")
parser.add_argument("project_path", help="Target directory to process")
parser.add_argument("--no-js", action="store_true", help="Skip JavaScript obfuscation")
parser.add_argument("--no-css", action="store_true", help="Skip CSS minification")
parser.add_argument("--no-html", action="store_true", help="Skip HTML minification")
args = parser.parse_args()

root_path = Path(args.project_path).resolve()
if not root_path.exists():
    print(f"Error: Path {root_path} not found.")
    sys.exit(1)

# Build Directory Logic
# Creates a unique build folder to prevent overwriting production source
dist_base = root_path / "dist_package"
counter = 0
dist_path = dist_base
while dist_path.exists():
    counter += 1
    dist_path = root_path / f"dist_package_{counter}"

# Copy source files to the new build directory, excluding python scripts and previous builds
shutil.copytree(root_path, dist_path, dirs_exist_ok=True, ignore=shutil.ignore_patterns('dist_package*', '*.py'))
print(f"Build initialized at: {dist_path}")

# Logging System
error_log = dist_path / "build_errors.log"
def log_failure(message):
    print(message)
    with open(error_log, "a", encoding="utf-8") as f:
        f.write(message + "\n")

# Processing Engines
def process_html(file_path):
    try:
        print(f"Compressing HTML: {file_path.name}")
        cmd = f'npx html-minifier-terser --collapse-whitespace --remove-comments --remove-optional-tags --minify-css true --minify-js true -o "{file_path}" "{file_path}"'
        subprocess.run(cmd, shell=True, check=True)
    except Exception as e:
        log_failure(f"HTML processing failed: {file_path} -> {e}")

def process_css(file_path):
    try:
        print(f"Minifying CSS: {file_path.name}")
        cmd = f'cleancss -o "{file_path}" "{file_path}"'
        subprocess.run(cmd, shell=True, check=True)
    except Exception as e:
        log_failure(f"CSS processing failed: {file_path} -> {e}")

def process_js(file_path):
    try:
        print(f"Obfuscating JS: {file_path.name}")
        # Standard production flags for high-level protection
        cmd = f'npx javascript-obfuscator "{file_path}" --output "{file_path}" --compact true --control-flow-flattening true --dead-code-injection true --string-array true --string-array-encoding base64'
        subprocess.run(cmd, shell=True, check=True)
    except Exception as e:
        log_failure(f"JS processing failed: {file_path} -> {e}")

# Execution Loop
for root, dirs, files in os.walk(dist_path):
    for f in files:
        file_path = Path(root) / f
        extension = file_path.suffix.lower()
        
        if extension == ".html" and not args.no_html:
            process_html(file_path)
        elif extension == ".css" and not args.no_css:
            process_css(file_path)
        elif extension == ".js" and not args.no_js:
            process_js(file_path)

print("\nProcess finished. Check build_errors.log for details if needed.")