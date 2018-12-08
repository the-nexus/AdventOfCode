#pragma once

#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <map>

class AOCHelper
{
public:
	static bool ReadFile(std::string const& fileName, std::vector<std::string>& outLines);

	static void ResetRNG();

	template<typename T>
	static void ShuffleVector(std::vector<T>& target)
	{
		std::random_shuffle(target.begin(), target.end());
	}
};
