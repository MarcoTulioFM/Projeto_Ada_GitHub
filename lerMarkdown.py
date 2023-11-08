import markdown

# Defina o caminho para o seu arquivo Markdown
caminho_arquivo = './README.md'

# Abra o arquivo e leia seu conteúdo
with open(caminho_arquivo, 'r') as arquivo:
    texto_markdown = arquivo.read()

# Converta o conteúdo Markdown em HTML
html = markdown.markdown(texto_markdown)

# Escreva o HTML resultante em um novo arquivo chamado index.html
with open("index.html", 'w') as html_file:
    html_file.write(html)

# Imprima uma confirmação de que o arquivo foi criado com sucesso
print("Arquivo HTML gerado com sucesso.")
