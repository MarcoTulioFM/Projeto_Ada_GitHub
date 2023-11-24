import markdown

# Defina o caminho para o seu arquivo Markdown
caminho_arquivo_markdown = './README.md'

# Abra o arquivo e leia seu conteúdo
with open(caminho_arquivo_markdown, 'r') as arquivo_markdown:
    texto_markdown = arquivo_markdown.read()

# Converta o conteúdo Markdown em HTML com a extensão 'extra' e 'nl2br'
html = markdown.markdown(texto_markdown, extensions=['extra', 'nl2br'])

# Inclua o HTML gerado em um template
template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seu Título</title>
    
    <!-- Incluindo estilo gerado pelo Python -->
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}

        h1 {{
            text-align: center;
        }}

        ul {{
            list-style: none;
            padding: 0;
        }}

        li {{
            border: 1px solid #ccc;
            margin: 10px 0;
            padding: 10px;
            box-shadow: 2px 2px 5px #aaa;
        }}

        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 10px 0;
        }}
    </style>
</head>
<body>
{html}
</body>
</html>
"""

# Escreva o HTML resultante em um novo arquivo chamado index.html
with open("index.html", 'w') as html_file:
    html_file.write(template)

print("Arquivo HTML gerado com sucesso.")
