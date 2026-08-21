#include <iostream>
#include <unordered_map>
#include <vector>

int main() {
	int n;
	std::cin >> n;

	std::vector<int> nums(n);
	for (int& number : nums) {
		std::cin >> number;
	}

	int target;
	std::cin >> target;

	std::unordered_map<int, int> seen;
	for (int index = 0; index < n; ++index) {
		int complement = target - nums[index];
		auto match = seen.find(complement);
		if (match != seen.end()) {
			std::cout << match->second << ' ' << index << '\n';
			return 0;
		}
		seen[nums[index]] = index;
	}

	return 0;
}
