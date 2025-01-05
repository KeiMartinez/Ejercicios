//Definir una clase de jugador con nombre y nivel
export class Player {
  constructor(name, level) {
    this.name = name;
    this.level = level;
  }  
  }

const player2  = new Player("Bob", 5);
console.log(player2.name, player2.level);