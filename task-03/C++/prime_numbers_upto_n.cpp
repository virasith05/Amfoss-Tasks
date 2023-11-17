#include <iostream>

int main() {
    int n;

    std::cout << "Enter a number: ";
    std::cin >> n;

    std::cout << "Prime numbers up to " << n << " are: ";

    for (int i = 2; i <= n; i++) {
        bool isPrime = true;
        
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            std::cout << i << " ";
        }
    }

    std::cout << std::endl;

    return 0;
}

