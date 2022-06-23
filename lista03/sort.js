let vetor = [0, 5, 4, 3, 2, 8];

for (let x = 2; x < vetor.length; x++) {
  let conteudo = vetor[x];
  let y = x - 1

  while(y > 0 && vetor[y] > conteudo) {
    vetor[y + 1] = vetor[y];
    y = y - 1;
  }

  vetor[y + 1] = conteudo;
}

console.log(vetor);
