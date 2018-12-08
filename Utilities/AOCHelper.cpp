#include "AOCHelper.h"
#include <ctime>
#include <cstdlib>



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

void AOCHelper::ResetRNG()
{
	std::srand((unsigned int)std::time(0));
}
