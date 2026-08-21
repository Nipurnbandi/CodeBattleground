#include <unordered_map>
#include <vector>

std::vector<int> two_sum(const std::vector<int>& nums, int target) {
	std::unordered_map<int, int> seen;
	for (int index = 0; index < static_cast<int>(nums.size()); ++index) {
		int complement = target - nums[index];
		auto match = seen.find(complement);
		if (match != seen.end()) {
			return {match->second, index};
		}
		seen[nums[index]] = index;
	}
	return {};
}
