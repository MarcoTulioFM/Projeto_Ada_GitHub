import markdown

# Defina o caminho para o seu arquivo Markdown
caminho_arquivo = './README.md'

# Abra o arquivo e leia seu conteúdo
with open(caminho_arquivo, 'r') as arquivo:
    texto_markdown = arquivo.read()

# Converta o conteúdo Markdown em HTML
html = markdown.markdown(texto_markdown)

# Imprima o HTML resultante
print(html)
