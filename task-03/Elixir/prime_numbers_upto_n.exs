IO.puts("Enter a number: ")
n = String.trim(IO.gets("") || "") |> String.to_integer()

for num <- 2..n do
  is_prime = num in [2, 3] or not Enum.any?(2..trunc(:math.sqrt(num)), fn x -> rem(num, x) == 0 end)
  if is_prime, do: IO.puts("#{num} is prime")
end
