// Refer to Task 7 in your Instructions to complete this task

let buzzWords = [
  "Fizz",
  "Buzz",
  "Woof",
  "Bark",
  "Awoo",
  "Bang"
];

const esPrimo = (num) => {
  if (num <= 2) return false;
  for (let i = 2; i <= Math.sqrt(num); i++){
    if (num % i === 0) return false;
  }
  return true;

};

const resultado = [];
for (let i = 1; i <= 105; i++){
  let output = "";

  if (esPrimo(i) && i % 2 !== 0){
    const palabra = buzzWords[(i - 1) % buzzWords.length];
    output = palabra;
  }else{
    output = i.toString();
  }
  resultado.push(output);
}
  console.log("This is Task Seven!" || resultado);
