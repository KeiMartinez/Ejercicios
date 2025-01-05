export function costCalculator(amount) {
  const fee = 3;
  const interestRate = 0.01;
  return amount + fee + (amount * interestRate);

}