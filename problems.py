#progeto 2- To do
import time
from datetime import date
print("==========To-Do list===============")
print("\nTasks:")

def data():
    hoje = date.today()
    print(f"\nData {hoje}")
data()

print("----------------------------------------- ")

print("1.Adicionar")
print("2.Remover")
print("3.Ver")

opcao = int(input("Escolha uma opcao: "))

def tasks():
    task = ["ola"]
    if opcao == 1:
        minhas_tarefas = input(">") 
        task.append(minhas_tarefas)
        print(minhas_tarefas)
        print("Tarefa adicionada")
    
    elif opcao == 2:
        remover_tarefa = input("ordem da tarefa")
        task.remove(remover_tarefa)
        print(task)
tasks()
