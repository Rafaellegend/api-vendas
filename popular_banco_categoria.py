import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from vendas.models import Categoria

dados = [ 
    ("Camisetas", "Modelos casuais e estampados para o dia a dia"),
    ("Calças", "Jeans, sarja, moletom e outros modelos"),
    ("Vestidos", "Vestidos casuais, sociais e para festas"),
    ("Saias", "Saias curtas, médias e longas de vários tecidos"),
    ("Bermudas", "Bermudas masculinas e femininas para diversas ocasiões"),
    ("Blusas", "Blusas femininas de diversos estilos"),
    ("Camisas", "Camisas sociais, casuais e polo"),
    ("Jaquetas", "Jaquetas jeans, de couro, corta-vento e mais"),
    ("Moletons", "Moletons lisos e estampados para o frio"),
    ("Roupas Íntimas", "Lingeries, cuecas e peças íntimas"),
    ("Roupas Esportivas", "Roupas para academia, corrida e esportes em geral"),
    ("Roupas de Banho", "Biquínis, maiôs, sungas e shorts de banho"),
    ("Acessórios", "Bolsas, cintos, bonés, chapéus e mais"),
    ("Calçados", "Tênis, sapatos, sandálias e chinelos"),
    ("Infantil", "Roupas para bebês e crianças"),
    ("Juvenil", "Moda jovem para adolescentes"),
    ("Plus Size", "Moda inclusiva com tamanhos maiores"),
    ("Moda Praia", "Roupas leves para praia e verão"),
    ("Moda Festa", "Roupas formais e sofisticadas para eventos"),
    ("Uniformes", "Roupas profissionais e escolares")
]

def criar_categorias():
    for nome, descricao in dados:
        Categoria.objects.create(nome=nome, descricao=descricao)

criar_categorias()