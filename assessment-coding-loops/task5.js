// Refer to Task 5 in your Instructions to complete this task
const lines = parseInt(prompt("Ingresa numero de lineas:"), 10);

for (let i = 0; i < lines; i++) {
  let output = "";
  if (i % 3 === 0) output += "Fizz";
  if (i % 5 === 0) output += "Buzz";
  if (i % 7 === 0) output += "Woof"
  ;
    console.log("This is Task Five!" || output || i);
  }