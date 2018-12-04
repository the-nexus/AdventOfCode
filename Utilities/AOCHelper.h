#pragma once

#include <fstream>
#include <iostream>
#include <string>
#include <vector>

class AOCHelper
{
public:
	static bool ReadFile(std::string const& fileName, std::vector<std::string>& outLines);
};
