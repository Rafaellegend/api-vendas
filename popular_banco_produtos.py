import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from vendas.models import Produto,Categoria

dados = [
    ("Camiseta Básica Branca", "Camiseta unissex 100% algodão", 39.90, 120, "Camisetas", None),
    ("Calça Jeans Skinny", "Calça jeans azul escuro com elastano", 129.90, 50, "Calças", None),
    ("Vestido Floral", "Vestido estampado leve para verão", 99.90, 30, "Vestidos", None),
    ("Saia Plissada Midi", "Saia rosa clara com tecido fluido", 89.90, 20, "Saias", None),
    ("Bermuda Cargo Masculina", "Bermuda com bolsos laterais e cós elástico", 74.90, 35, "Bermudas", None),
    ("Blusa Canelada Manga Longa", "Blusa justa com gola alta", 59.90, 40, "Blusas", None),
    ("Camisa Social Branca", "Camisa para eventos e trabalho", 119.90, 25, "Camisas", None),
    ("Jaqueta Jeans Oversized", "Jaqueta estilosa em jeans claro", 179.90, 15, "Jaquetas", None),
    ("Moletom Canguru Preto", "Moletom com bolso frontal e capuz", 99.90, 60, "Moletons", None),
    ("Cueca Boxer Kit com 3", "Cuecas em algodão com elástico confortável", 49.90, 80, "Roupas Íntimas", None),
    ("Top Esportivo Feminino", "Top com alta sustentação", 69.90, 28, "Roupas Esportivas", None),
    ("Sunga Estampada", "Sunga masculina para praia", 39.90, 20, "Roupas de Banho", None),
    ("Boné Aba Curva", "Boné com ajuste traseiro e logo frontal", 34.90, 100, "Acessórios", None),
    ("Tênis Casual Branco", "Tênis unissex ideal para o dia a dia", 149.90, 42, "Calçados", None),
    ("Macacão Infantil Azul", "Macacão de algodão para bebês", 59.90, 18, "Infantil", None),
    ("Blusa Juvenil Estampada", "Blusa divertida para adolescentes", 49.90, 22, "Juvenil", None),
    ("Vestido Plus Size Longo", "Vestido confortável com elástico na cintura", 119.90, 14, "Plus Size", None),
    ("Regata Praia Masculina", "Regata leve com estampa tropical", 44.90, 50, "Moda Praia", None),
    ("Camisa Social Slim Fit", "Camisa formal com corte moderno", 139.90, 12, "Moda Festa", None),
    ("Uniforme Escolar Básico", "Conjunto camiseta e bermuda", 89.90, 33, "Uniformes", None),
    ("Camiseta Estampada Manga Curta", "Estampa exclusiva com tinta ecológica", 54.90, 45, "Camisetas", None),
    ("Calça Jogger Moletom", "Calça com punho e cordão na cintura", 89.90, 28, "Calças", None),
    ("Vestido Tubinho Preto", "Clássico e elegante", 139.90, 17, "Vestidos", None),
    ("Saia Jeans Destroyed", "Saia desfiada com lavagem clara", 99.90, 10, "Saias", None),
    ("Bermuda de Moletom", "Conforto para o dia a dia", 64.90, 38, "Bermudas", None),
    ("Blusa Cropped Estampada", "Modelo curto com tecido leve", 49.90, 34, "Blusas", None),
    ("Camisa Polo Masculina", "Polo clássica com detalhe na gola", 79.90, 40, "Camisas", None),
    ("Jaqueta Corta-Vento", "Resistente à água e super leve", 159.90, 25, "Jaquetas", None),
    ("Moletom Oversized Colorido", "Moletom unissex com cores vibrantes", 109.90, 20, "Moletons", None),
    ("Calcinha Renda Kit com 3", "Conforto e beleza para o dia a dia", 44.90, 65, "Roupas Íntimas", None),
    ("Legging Compressão Alta", "Ideal para treinos intensos", 79.90, 26, "Roupas Esportivas", None),
    ("Maiô Recorte Lateral", "Design moderno e elegante", 89.90, 14, "Roupas de Banho", None),
    ("Bolsa Tiracolo Pequena", "Compacta e estilosa", 99.90, 19, "Acessórios", None),
    ("Sandália Rasteira", "Confortável e leve", 69.90, 30, "Calçados", None),
    ("Body Infantil Manga Longa", "Tecido macio com botão entrepernas", 39.90, 24, "Infantil", None),
    ("Jaqueta Juvenil com Capuz", "Ideal para dias frios", 129.90, 13, "Juvenil", None),
    ("Calça Legging Plus Size", "Alta elasticidade e conforto", 89.90, 11, "Plus Size", None),
    ("Camisa de Linho Masculina", "Perfeita para eventos na praia", 149.90, 9, "Moda Praia", None),
    ("Vestido Longo com Fenda", "Sofisticação para eventos", 169.90, 8, "Moda Festa", None),
    ("Uniforme Profissional Cinza", "Modelo unissex resistente", 119.90, 18, "Uniformes", None),
    ("Camiseta Gola V Básica", "Modelo slim com acabamento reforçado", 44.90, 37, "Camisetas", None),
    ("Calça Cargo Feminina", "Estilo urbano com bolsos funcionais", 119.90, 20, "Calças", None),
    ("Vestido Chemise", "Modelo leve com botões frontais", 109.90, 14, "Vestidos", None),
    ("Saia Lápis Social", "Elegância para o ambiente de trabalho", 89.90, 16, "Saias", None),
    ("Bermuda Estampada Masculina", "Conforto com estilo casual", 74.90, 22, "Bermudas", None),
    ("Blusa Ombro a Ombro", "Modelo feminino com babados", 64.90, 18, "Blusas", None),
    ("Camisa Flanela Xadrez", "Ideal para meia estação", 94.90, 21, "Camisas", None),
    ("Tênis Esportivo Corrida", "Alta performance e conforto", 199.90, 10, "Calçados", None)
]

def criar_produtos():
    for nome, descricao, preco, estoque, categoria, imagem  in dados:
        categoria_obj, created = Categoria.objects.get_or_create(nome=categoria)
        Produto.objects.create(nome=nome, descricao=descricao, preco=preco, quantidade_estoque=estoque, categoria=categoria_obj, imagem=imagem)

criar_produtos()