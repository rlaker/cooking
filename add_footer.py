import os


def insert_footer(file_path, footer_content):
    with open(file_path, 'r') as file:
        content = file.read()

    # # Check if the footer is already present
    # if footer_content.strip() in content:
    #     print(f"Footer already present in {file_path}")
    #     return

    # Split the content at '</body>' and insert the footer
    parts = content.split('</body>')
    if len(parts) == 2:
        updated_content = parts[0] + footer_content + '</body></html>'
        # print(updated_content)
        with open(file_path, 'w') as file:
            file.write(updated_content)
            print(f"Footer added to {file_path}")
    else:
        print(f"Could not find '</body>' tag in {file_path}")

def find_and_update_html_files(root_folder, footer_content):
    for subdir, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(subdir, file)
                insert_footer(file_path, footer_content)


# Define the footer content
footer_content = """
<!-- Footer -->
<footer>
    <script async data-id="101072216" src="//static.getclicky.com/js"></script>
</footer>
"""

# Specify the root folder where your HTML files are located
root_folder = '.'

# Run the function
find_and_update_html_files(root_folder, footer_content)
