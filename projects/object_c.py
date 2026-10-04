from PIL import Image

def converter_para_ascii(caminho_imagem, nova_largura=60):
    # 1. Carrega a imagem e converte para tons de cinzento
    img = Image.open(caminho_imagem).convert("L")
    
    # 2. Ajusta a proporção (caracteres do terminal são mais altos do que largos)
    largura_original, altura_original = img.size
    proporcao = altura_original / largura_original
    nova_altura = int(nova_largura * proporcao * 0.55)
    img = img.resize((nova_largura, nova_altura))
    
    # 3. Mapeia os píxeis para caracteres (do mais escuro ao mais claro)
    caracteres = "@%#*+=-:. "
    pixeis = img.getdata()
    
    art = "".join([caracteres[pixel // 26] for pixel in pixeis])
    
    # 4. Divide o texto em linhas com a largura correta
    for i in range(0, len(art), nova_largura):
        print(art[i:i+nova_largura])

# Exemplo de uso (requer uma imagem guardada no seu PC):
# converter_para_ascii("carro.png")

