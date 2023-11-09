import json

# Abrindo e lendo o arquivo JSON
with open('projeto.json', 'r') as json_file:
    data = json.load(json_file)

# Inicializando o conteúdo do README.md
readme_content = "# Conteúdo\n\n"

# Iterando sobre os itens no arquivo JSON
for item in data:
    readme_content += f"## {item['Titulo']}\n\n"
    readme_content += f"- **Autor**: {item['Author']}\n"
    readme_content += f"- **Descrição**: {item['Descrição']}\n\n"

# Escrevendo no arquivo README.md
with open('README.md', 'w') as readme_file:
    readme_file.write(readme_content)
