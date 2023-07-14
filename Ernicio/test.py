from er import criarBoard,printBoard,getinputvalido,verficarMovimento,fazMovimento,verficarGanhador


jogador = 0 # jogador 1
board = criarBoard()
ganhador = verficarGanhador(board)
while (not ganhador):
 printBoard(board)
 i = getinputvalido("Digite a linha: ")
 j = getinputvalido("Digite a coluna: ")
 
 if(verficarMovimento(board,i,j)):
  fazMovimento(board,i,j,jogador)
  jogador = (jogador+1)%2
 else:
  print("A posição informada ja esta ocupada")
 ganhador =  verficarGanhador(board)

print("~"*29)
printBoard(board)
print("Ganhador = ",ganhador)
print("~"*29)
