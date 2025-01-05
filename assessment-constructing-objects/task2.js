function Mail(subj, msg) {
    this.subject = subj;
    this.message = msg;
  }

  function task2() {
   const prompt = require("prompt-sync")();
  // Type your code below this line!
  const userSubject = prompt("Ingrese el asunto del correo: ");
  const userMessage = prompt("Ingrese el mensaje del correo: ");
  const newMail = new Mail(userSubject, userMessage);
  
  // Type your code above this line!
  
  console.log(newMail.subject + ": " + newMail.message);

  }

  module.exports = task2;