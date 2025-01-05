//Define una clase de jugador con nombre, nivel, metodo info() y metodo levelUp()
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
  }
}

const player4 = new Player("Keila", 2);
player4.levelUp();
player4.info();