const holaUno = document.getElementById("rojo");
holaUno.textContent = "Adiós";

const primerHola = document.getElementById("rojo");
primerHola.style.color = "orange";

const pruebaUno = document.getElementById("prueba");
pruebaUno.addEventListener("click", function() {
    pruebaUno.style.color = "brown";
});