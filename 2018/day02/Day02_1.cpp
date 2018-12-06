#include "Day02_1.h"
#include <map>


Day02_1::Day02_1()
{

}

Day02_1::~Day02_1()
{

}

bool Day02_1::SetUp(std::string const& inputFileName)
{
	return AOCHelper::ReadFile(inputFileName, m_inputLines);
}

void Day02_1::Run()
{
	int doubleTotal = 0;
	int tripleTotal = 0;

	for (std::string const& line : m_inputLines)
	{
		std::map<char, int> symbolCountMap;

		for (char symbol : line)
		{
			symbolCountMap[symbol] += 1;
		}

		bool hasDouble = false;
		bool hasTriple = false;

		for (std::pair<char, int> symbolCountPair : symbolCountMap)
		{
			hasDouble |= (symbolCountPair.second == 2);
			hasTriple |= (symbolCountPair.second == 3);

			if (hasDouble && hasTriple)
			{
				break;
			}
		}

		if (hasDouble)
		{
			++doubleTotal;
		}

		if (hasTriple)
		{
			++tripleTotal;
		}
	}

	int checksum = doubleTotal * tripleTotal;
	std::cout << "Answer: " << checksum << std::endl;
}

void Day02_1::CleanUp()
{

}
