// Type your code below this line!


// Type your code above this line!
function task4() {
const prompt = require('prompt-sync')();
class Journey{
    constructor(start, end){
        this.from = start;
        this.to = end;
    }
}
// Type your code below this line!
const startLocation = prompt("Ingrese el lugar de partida: ");
const endLocation = prompt("Ingrese el destino: ");

const travel = new Journey(startLocation, endLocation);
// Type your code above this line!
console.log(`Booking a taxi from ${travel.from} to ${travel.to}.`);

}

module.exports = task4;