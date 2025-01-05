export class Player {
  constructor(name, level = 1) {
    this.name = name;
    this.level = level;
    this.experience = 0;
    this.experienceToNextLevel = 100;
  }
  
  gainExperience(amount){
    this.experience += amount;
    while (this.experience >= this.experienceToNextLevel){
      this.levelUp();
      this.experience -= this.experienceToNextLevel;
      this.experienceToNextLevel *= 1.5;
    }
  }
  levelUp(){
    this.level++;
    console.log(`${this.name} level ${this.level}`);
  }
  }

  