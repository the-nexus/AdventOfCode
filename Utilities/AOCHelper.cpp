#include "AOCHelper.h"



bool AOCHelper::ReadFile(std::string const& fileName, std::vector<std::string>& outLines)
{
	std::ifstream file(fileName);
	if (file.is_open())
	{
		std::string line;
		while (std::getline(file, line))
		{
			outLines.push_back(line);
		}
		return true;
	}

	return false;
}