class Auto{
    constructor(marca, modelo, año, color, puertas, motor, kilometraje, extras =[]){
        this.marca = marca;
        this.modelo = modelo;
        this.año = año;
        this.color = color;
        this.puertas = puertas;
        this.motor = motor;
        this.kilometraje = kilometraje;
        this.extras = extras;
    }

}

const miAuto = new Auto(
    "Mercedez",
    "Corolla",
    1995,
    "Negro",
    6,
    "Automatico",
    15000,
    ["Aire acondicionado", "Camara trasera", "Y no le duele nada"]

);

console.log(miAuto);