#include "Day02_2.h"
#include <map>


Day02_2::Day02_2()
{

}

Day02_2::~Day02_2()
{

}

bool Day02_2::SetUp(std::string const& inputFileName)
{
	return AOCHelper::ReadFile(inputFileName, m_inputLines);
}

void Day02_2::Run()
{
	for (size_t symbolIdx = 0; symbolIdx < m_inputLines[0].length(); ++symbolIdx)
	{
		for (std::string const& line : m_inputLines)
		{

		}
	}

	std::string commonLetters = "N/A";
	std::cout << "Answer: " << commonLetters << std::endl;
}

void Day02_2::CleanUp()
{

}
