
relatorio_csv = '/Projeto_1/gestao_notas/relatorios/relatorio.csv'

def criar_relatorio_csv(alunos, relatorio_csv):
  with open (relatorio_csv, 'w', newline='') as arquivo:
    colunas = ["Matrícula", "Nome do Aluno", "Disciplina", "Média Final", "Status"]
    writer = csv.DictWriter(relatorio_csv, colunas=colunas)
    writer.writeheader()
    writer.writerow({
    "Matrícula": aluno["matricula"],
    "Nome do Aluno": aluno["nome"],
    "Disciplina": aluno["disciplina"],
    "Média Final": aluno["media_final"],
    "Status": aluno["status"]
})
    return alunos 