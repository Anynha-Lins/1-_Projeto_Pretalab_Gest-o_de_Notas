
def calculo_media(nota1, nota2, nota3):
    media = (float(nota1) + float(nota2) + float(nota3)) / 3
    return media

def status_aprovacao(media):
    return "Parabéns, você foi aprovado" if media >= 6 else "Você foi reprovado"

def analisar_notas(alunos):
  for aluno in alunos:
      media = calcular_media(aluno["nota1"], aluno["nota2"], aluno["nota3"])
      aluno["media_final"] = media
      aluno["status"] = status_aprovacao(media)
      return alunos