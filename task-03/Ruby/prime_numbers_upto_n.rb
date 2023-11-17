puts "Enter a number:"
n = gets.chomp.to_i

prime_numbers = []

for i in 2..n
 is_prime = true

 for j in 2..Math.sqrt(i).to_i
    if i % j == 0
      is_prime = false
      break
    end
 end

 prime_numbers.push(i) if is_prime
end

puts "Prime numbers up to #{n} are:"
puts prime_numbers