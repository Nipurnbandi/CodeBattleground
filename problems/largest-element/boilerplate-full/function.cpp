#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> nums(n);
    for (int& number : nums) {
        std::cin >> number;
    }

    int largest = nums[0];
    for (int number : nums) {
        if (number > largest) {
            largest = number;
        }
    }

    std::cout << largest << '\n';
    return 0;
}
