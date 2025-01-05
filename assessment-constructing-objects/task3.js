// Type your code below this line!

function Mail(subj, msg) {
    this.subject = subj;
    this.message = msg;
    
    this.printMail = function(){
      console.log(`${this.subject}: ${this.message}`)
    }
    
// Type your code above this line!
}
  function task3() {
    const prompt = require("prompt-sync")();
    const userSubject = prompt("Ingrese el asunto del correo: ");
    const userMessage = prompt("Ingrese el mensaje del correo: ");
// Type your code below this line! 
    const newMail = new Mail(userSubject, userMessage);
// Type your code above this line!  
  newMail.printMail()

  }


  module.exports = task3;