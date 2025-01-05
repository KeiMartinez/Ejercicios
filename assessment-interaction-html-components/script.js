const burgerBtn = document.getElementById('burger-btn');
const alertBtn = document.getElementById('alert-btn');
const elementosLista = document.querySelectorAll('td ul li');
const titulo = document.getElementById('titulo');
burgerBtn.addEventListener('click', () => {
  console.log("¡Alguien hizo clic en BURGER TOWN!");
});

alertBtn.addEventListener('click', () => {
  alert("ES HORA DE HAMBURGUESA");
});

elementosLista.forEach(function (elemento) {
    if (elemento.textContent.includes('ARROZ')) {
        elemento.addEventListener('click', function () {
            titulo.style.color = 'red';
        });
    }
});