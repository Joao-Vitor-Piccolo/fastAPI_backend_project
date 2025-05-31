const imagens = [
  "src/assets/imgs/carro_eletrico_1.jpg",
  "src/assets/imgs/carro_eletrico_2.jpg",
  "src/assets/imgs/bandeira_baiha.jpg"
];

let indice = 0;

function trocarFundo() {
  document.body.style.backgroundImage = `url('${imagens[indice]}')`;
  indice = (indice + 1) % imagens.length;
}

trocarFundo();
setInterval(trocarFundo, 5000);
