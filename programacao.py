def ler_notas():
    notas = []

    for i in range(6):
       nota = float(input("Digite a nota de (0 a 10): "))

       while nota < 0.0 or nota > 10.0:
        print("Nota invalida. Digite uma nota de 0 a 10")
        nota = float(input("Digite a nota de (0 a 10): "))

       notas.append(nota)
    print("\nNotas armazenadas no vetor:",notas)
    return notas

def calculo_de_media(notas):
   media = sum(notas) / len(notas)
   print(f"\n1. O valor da média geral da turma é {media:.2f}")

   acima_ou_igual = 0 
   notas_abaixo = []

   for nota in notas: 
      if nota >= media: 
         acima_ou_igual += 1 

      else: 
         notas_abaixo.append(nota)

   print("A quantidade de alunso acima da média é:", acima_ou_igual)
   print("A quantidade de alunos abaixo da média é:", notas_abaixo)

   return media

def processo_recuperacao(notas, media): 
   print("\n--- INICIO DA RECUPERAÇÃO ---")

   for i in range(len(notas)):
      if notas[i] < media:
         print(f"\nO aluno com a nota {notas[i]} ficou abaixo da média ({media:.2f}).")

         nota_rec = float(input("Digite a nota da sua recuperação (0 a 10): "))
         while nota_rec < 0.0 or nota_rec > 10: 
            print("Nota invalida. Digite uma nota entre (0 e 10)")
            nota_rec = float(input("Digite a nota da sua recuperação (0 a 10): "))

         if nota_rec > notas[i]:
            print(f"Parabéns! A nota {nota_rec} substitui a nota antiga {notas[i]}.")

         else: 
          print("A nota da recuperação não foi maior. A nota original foi mantida.")

   print("\nVetor de notas atualizados:", notas)

   nova_media = sum(notas) / len(notas)
   print(f"Nova média geral da turma após recuperação é: {nova_media:.2f}")

   return notas 

turma_notas = ler_notas()

media_turma = calculo_de_media(turma_notas)

processo_recuperacao(turma_notas, media_turma)