use std::io;

fn main() {
    println!("Please enter a number: ");

    let mut input = String::new();

    io::stdin().read_line(&mut input)
        .expect("Failed to read line");

    let n: u32 = input.trim().parse()
        .expect("Please type a number!");

    let mut primes = Vec::new();

    'outer: for i in 2..=n {
        if i == 2 {
            primes.push(i);
            continue;
        }
        if i % 2 == 0 {
            continue;
        }
        let sqrt_i = (i as f64).sqrt() as u32;
        for &prime in &primes {
            if prime > sqrt_i {
                break;
            }
            if i % prime == 0 {
                continue 'outer;
            }
        }
        primes.push(i);
    }

    println!("Prime numbers up to {}: ", n);
    for prime in primes {
        println!("{}", prime);
    }
}
