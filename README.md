# Markdown to HTML Converter

This Python script converts Markdown files into HTML, adding enhanced CSS styles for better visualization. It supports rendering tables with borders, shaded table headers, and auto-sizing based on content. The script is ideal for generating HTML documents from Markdown files, especially useful for documentation and reporting where consistency in styling and format is crucial.

## Features

- **Table Rendering**: Converts Markdown tables to HTML with borders for clarity.
- **Shaded Table Headers**: Adds a subtle grey background to table headers for visual distinction.
- **Auto-sizing Tables**: Adjusts table width automatically based on the content, enhancing layout responsiveness.
- **Fenced Code Blocks**: Supports fenced code blocks, preserving the format of code snippets within your Markdown.

## Requirements

- Python 3.x
- Markdown library: Ensure the `markdown` library is installed via pip:
  ```bash
  pip install markdown
  ```

## Installation

Clone the repository or download the script directly to your local machine.

```bash
git clone https://github.com/madchutney/markdown-to-html-converter.git
cd markdown-to-html-converter
```

## Usage

Run the script from the command line by specifying the input Markdown file and the output HTML file path:

```bash
python markdown_to_html.py input.md output.html
```

The script reads the specified Markdown file, converts it into HTML with the added styles, and saves the result to the specified output HTML file. If there are any issues with the file paths or reading the content, the script will provide a descriptive error message.

## Contributing

Contributions to enhance the script, add more features, or improve documentation are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for more details. This license ensures both flexibility for the user and protection against patent claims for contributors.
