isPrime :: Int -> Bool
isPrime n = null [x | x <- [2..(n-1)], n `mod` x == 0]

primes :: Int -> [Int]
primes n = [x | x <- [2..n], isPrime x]

main :: IO ()
main = do
    putStrLn "Please enter a number:"
    n <- readLn
    let primeNumbers = primes n
    putStrLn $ "Prime numbers up to " ++ show n ++ " are: " ++ show primeNumbers