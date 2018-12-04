#include "Day01_1.h"


Day01_1::Day01_1()
{

}

Day01_1::~Day01_1()
{

}

bool Day01_1::SetUp(std::string const& inputFileName)
{
	return AOCHelper::ReadFile(inputFileName, m_inputLines);
}

void Day01_1::Run()
{
	int resultFrequency = 0;
	for (std::string const& line : m_inputLines)
	{
		if (line.length() > 1 && (line[0] == '+' || line[0] == '-'))
		{
			resultFrequency += std::stoi(line);
		}
	}

	std::cout << "Answer: " << resultFrequency << std::endl;
}

void Day01_1::CleanUp()
{

}
