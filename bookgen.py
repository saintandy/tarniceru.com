import os
import re

def main():
  # Directory containing books
  books_dir = "public/books"
  
  # Output file
  output_file = os.path.join(books_dir, "index.html")
  
  # Get list of book files, excluding index.html
  books = []
  try:
    for filename in os.listdir(books_dir):
      if filename.lower() != "index.html" and filename.lower() != "index2.html" and os.path.isfile(os.path.join(books_dir, filename)):
        books.append(filename)
  except FileNotFoundError:
    print(f"Error: Directory {books_dir} not found")
    return
  
  # Sort books alphabetically
  books.sort()
  
  # Generate HTML content
  html_content = """<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Books</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 20px;
    }
    h1 {
      color: #333;
    }
    p {
      color: #666;
    }
    a {
      color: #007BFF;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <h1>Collection</h1>
  <ul>
"""
  
  # Process each book and add to HTML
  for book in books:
    if '_' in book:
      # Split filename into author and title parts
      author_part, title_part = book.split('_', 1)
      
      # Format author name (replace hyphens with spaces)
      author = author_part.replace('-', ' ')
      
      # Format title (remove file extension and replace hyphens with spaces)
      title = os.path.splitext(title_part)[0].replace('-', ' ')
      
      # Add entry to HTML
      html_content += f'    <li><a href="{book}">{author}: {title}</a></li>\n'
  
  # Complete HTML content
  html_content += """  </ul>
</body>
</html>
"""
  
  # Write to output file
  try:
    with open(output_file, 'w') as f:
      f.write(html_content)
    print(f"Successfully generated {output_file}")
  except Exception as e:
    print(f"Error writing to {output_file}: {e}")

if __name__ == "__main__":
  main()
