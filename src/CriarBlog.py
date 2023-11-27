from jinja2 import Template
import json

# Carregando os dados do arquivo JSON
with open('projeto.json', 'r') as json_file:
    data = json.load(json_file)

# O template HTML
template_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Versionamento e GitHub</title>
    <!-- Incluindo estilo gerado pelo Python -->
</head>
<body>
    <h1>Conteúdo</h1>
    {% for item in data %}
    <h2>{{ item['Titulo'] }}</h2>
    <ul>
        <li><strong>Autor</strong>: {{ item['Author'] }}</li>
        <li><strong>Descrição</strong>: {{ item['Descrição'] }}</li>
    </ul>
    {% endfor %}
    <img src="./assets/all.png">
</body>
</html>
'''

# Carregando o template
template = Template(template_html)

# Renderizando o template com os dados do JSON
rendered_html = template.render(data=data)

# Escrevendo o HTML renderizado em um arquivo
with open('../index.html', 'w') as file:
    file.write(rendered_html)

print("Arquivo HTML gerado com sucesso!")
