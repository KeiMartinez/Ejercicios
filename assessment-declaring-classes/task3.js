// Definir una clase de jugador con nombre, nivel y metodo info()
export class Player {
  constructor(name, level) {
     this.name = name;
     this.level = level;
  }
  info(){
    console.log(`${this.name} has reached Level ${this.level}!`);
  }
  levelUp(){
    this.level++;
    console.log(`${this.name} has leveled up!`);
  }
}

const player3 = new Player("Tara", 5);
player3.info();
player3.levelUp();
player3.info();


