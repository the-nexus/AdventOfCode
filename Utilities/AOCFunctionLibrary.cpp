#include "AOCFunctionLibrary.h"
#include <ctime>
#include <cstdlib>



//////////////////////////////////////////////////////////////////////////////////////////////////
// File I/O
bool AOCFunctionLibrary::ReadFile(std::string const& fileName, std::vector<std::string>& outLines)
{
	std::ifstream file(fileName);
	if (file.is_open())
	{
		std::string line;
		while (std::getline(file, line))
		{
			outLines.push_back(line);
		}
		return !outLines.empty();
	}

	return false;
}



//////////////////////////////////////////////////////////////////////////////////////////////////
// String
void AOCFunctionLibrary::SplitString(std::string const& stringToSplit, std::string const& delimiter, std::vector<std::string>& outStrings)
{
	outStrings.clear();

	int startIndex = 0;
	int endIndex = 0;

	int stringSize = (int)stringToSplit.size();
	while (startIndex < stringSize)
	{
		int delemiterIndex = (int)stringToSplit.find(delimiter, startIndex);
		endIndex = delemiterIndex >= 0 ? delemiterIndex : stringSize;

		outStrings.push_back(stringToSplit.substr(startIndex, endIndex - startIndex));

		startIndex = endIndex + (int)delimiter.size();
	}
}



//////////////////////////////////////////////////////////////////////////////////////////////////
// Random
void AOCFunctionLibrary::ResetRNG()
{
	std::srand((unsigned int)std::time(0));
}
