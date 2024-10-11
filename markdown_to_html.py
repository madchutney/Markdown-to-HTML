import markdown
import sys

def convert_markdown_to_html(markdown_file_path, html_file_path):
    """
    Converts a Markdown file to an HTML file with support for tables, fenced code blocks, and adds enhanced CSS for auto-sizing tables based on content.

    Parameters:
    - markdown_file_path: Path to the Markdown file.
    - html_file_path: Path where the HTML file will be saved.
    """
    try:
        # Read Markdown file
        with open(markdown_file_path, 'r', encoding='utf-8') as md_file:
            markdown_text = md_file.read()

        # Convert Markdown to HTML with extensions for tables and code fences
        html_content = markdown.markdown(markdown_text, extensions=['tables', 'fenced_code'])

        # Add CSS for auto-sizing tables
        css = """
        <style>
        table {
            border-collapse: collapse;
            width: auto; /* Adjusted from 100% to auto to allow table to size based on content */
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2; /* Light grey shade for the header row */
        }
        </style>
        """

        # Combine CSS with HTML content
        full_html = css + html_content

        # Write HTML to file
        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(full_html)
        
        print(f"HTML file has been created successfully at: {html_file_path}")
    
    except FileNotFoundError:
        print("The Markdown file was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_markdown_file.md> <output_html_file.html>")
    else:
        markdown_file = sys.argv[1];
        html_file = sys.argv[2];
        convert_markdown_to_html(markdown_file, html_file)
