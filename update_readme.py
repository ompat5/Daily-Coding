import re

def update_readme():
    with open('daily_progress_table.html', 'r', encoding="utf-8") as html_file:
        table_html = html_file.read()

    with open('README.md', 'r', encoding="utf-8") as readme_file:
        readme_content = readme_file.read()

    new_readme = re.sub(
        r'<!-- START PROGRESS TABLE -->.*<!-- END PROGRESS TABLE -->',
        f'<!-- START PROGRESS TABLE -->\n{table_html}\n<!-- END PROGRESS TABLE -->',
        readme_content,
        flags=re.DOTALL
    )

    with open('README.md', 'w', encoding="utf-8") as readme_file:
        readme_file.write(new_readme)

if __name__ == '__main__':
    update_readme()