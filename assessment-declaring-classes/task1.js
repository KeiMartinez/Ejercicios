//Definir  una clase de jugador con nombre
export class Player {
  constructor(name) {
    this.name = name; 
  }
  }
const player1 = new Player("Alice");
console.log(player1.name);