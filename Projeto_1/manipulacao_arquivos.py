
import pandas as pd
import csv
notas_csv = 'Projeto_1/gestao_notas/arquivos_csv/notas.csv'

def notas(notas_csv):
    alunos = []
    with open(notas_csv, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            alunos.append({
                "matricula": row["Matrícula"],
                "nome": row["Nome do Aluno"],
                  "disciplina": row["Disciplina"],
                "nota1": row["Nota 1"],
                "nota2": row["Nota 2"],
                "nota3": row["Nota 3"],
                "nota_final": row["Nota Final"],
    })
            return alunos