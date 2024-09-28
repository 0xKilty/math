#include <iostream>
#include <unordered_set>

int main() {

    std::unordered_set<unsigned long> seen_numbers;

    int limit = 10000000;

    for (int i = 1; i < limit; i++) {
        unsigned long num = i;
        while (num != 1) {
            if (seen_numbers.find(num) != seen_numbers.end()) {
                break;
            } else {
                seen_numbers.insert(num);
                if (num & 1)
                    num = (3 * num) + 1;
                else
                    num >>= 1;
            }
        }
    }
    
    return 0;
}
