#include <vector>

int largest_element(const std::vector<int>& nums) {
    int largest = nums[0];
    for (int number : nums) {
        if (number > largest) {
            largest = number;
        }
    }
    return largest;
}
