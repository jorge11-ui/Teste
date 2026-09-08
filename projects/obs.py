from datetime import datetime
import os
import subprocess

disciplina = str(input("Qual é a disciplina: "))
tema_aula = str(input("Qual o tema da aula: "))

hoje = datetime.now()
data_formatada = hoje.strftime("%d-%m-%Y")
print("A data de hoje é: ", data_formatada)

print(f"A disciplina é {disciplina} e o tema é {tema_aula}.")


caminho_base = "/home/jorge/Documents/sStuff"

nome_ficheiro = f"{data_formatada}.md"

caminho_completo = f"{caminho_base}/{nome_ficheiro}"
print(f"o ficheiro vai ser cirado em: {caminho_completo}")

os.makedirs(caminho_base, exist_ok=True)

with open(caminho_completo, "w") as ficheiro_nota:
    ficheiro_nota.write(f"# {disciplina}\n")
print("nota criada com sucesso")

##subprocess
sStuff = "sStuff"

uri_obsidian = f"obsidian://open?vault={sStuff}&file={caminho_completo}"
subprocess.run(["xdg-open", uri_obsidian])
