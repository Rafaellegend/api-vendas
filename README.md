
# Api-Vendas

[![Python Version](https://img.shields.io/badge/3.13-Python-brightgreen?logo=python&logoColor=white&color=%233776AB)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/5.2-Django-brightgreen?logo=django&logoColor=white&color=%23092E20)](https://www.djangoproject.com/download/)

Esse projeto é um desáfio para ver meus conhecimentos sobre Django Rest Api.

O objetivo era criar uma api para uma loja de roupas.

## 💻Pré-Requisitos
Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou:
    - [Python 3.13](https://www.python.org/downloads/)
    - [Django 5.2](https://www.djangoproject.com/download/)
    - [Django REST framework](https://www.django-rest-framework.org/#installation)

## Rodando localmente

Entre no diretório do projeto
```bash
  cd api-vendas
```
Crie o ambiente Virtual
```bash
  python -m venv ./venv
```
Inicie o ambiente virtual

- Windows
    ```bash
    venv/Scripts/activate
    ```
- Linux
    ```bash
    source venv/Scripts/activate.fish
    ```
- Mac
    ```bash
    source venv/Scripts/activate.fish
    ```
Inicie o servidor

```bash
   pip install -r requirements.txt
```

Realize as Migrações

```bash
  python manage.py makemigrations
```

```bash
  python manage.py migrate
```

(Opicional) Popule os Bancos de dados
```bash
  python popular_banco_categorias.py
```
```bash
  python popular_banco_produtos.py
```

Inicie o servidor
```bash
  python manage.py runserver 
```
Acessando Documentação
```bash
  http://localhost:[port]/swagger
```

## 👨‍💻Autores
<table>
    <tr>
        <td align='center'>
            <a href='https://github.com/Rafaellegend'>
                <img src="https://avatars.githubusercontent.com/u/39443512?s=400&u=f816ce76f9d3f3a90aaab97ea80b27f283402ff3&v=4" alt="Rafaellegend Profile Picture"width="100">
                <p>Rafaellegend</p>
            </a>
        </td>
    </tr>
</table>
