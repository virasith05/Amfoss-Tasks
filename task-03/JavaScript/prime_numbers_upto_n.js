const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter a number: ', (n) => {
  const number = parseInt(n);

  if (!isNaN(number)) {
    let primes = [];

    for (let i = 2; i <= number; i++) {
      let isPrime = true;
      for (let j = 2; j * j <= i; j++) {
        if (i % j === 0) {
          isPrime = false;
          break;
        }
      }
      if (isPrime) {
        primes.push(i);
      }
    }

    console.log("Prime numbers up to " + number + " are: " + primes.join(", "));
  } else {
    console.log("Invalid input. Please enter a valid number.");
  }

  rl.close();
});
