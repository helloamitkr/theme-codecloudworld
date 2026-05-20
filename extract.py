import re

with open('theme.xml', 'r') as f:
    content = f.read()

css_match = re.search(r'<b:skin><!\[CDATA\[(.*?)\]\]></b:skin>', content, re.DOTALL)
if css_match:
    with open('preview/style.css', 'w') as f:
        f.write(css_match.group(1))

js_match = re.search(r'<script>\s*(document\.addEventListener.*?)\s*</script>', content, re.DOTALL)
if js_match:
    with open('preview/script.js', 'w') as f:
        f.write(js_match.group(1))
