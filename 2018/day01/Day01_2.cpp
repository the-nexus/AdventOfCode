#include "Day01_2.h"


Day01_2::Day01_2()
{

}

Day01_2::~Day01_2()
{

}

bool Day01_2::SetUp(std::string const& inputFileName)
{
	return AOCHelper::ReadFile(inputFileName, m_inputLines);
}

void Day01_2::Run()
{
	size_t lineIndex = 0;
	int resultFrequency = 0;
	while (m_resultMap.find(resultFrequency) == m_resultMap.end())
	{
		m_resultMap[resultFrequency] = 0;

		std::string const& line = m_inputLines[lineIndex];
		lineIndex = (lineIndex + 1) % m_inputLines.size();

		resultFrequency += std::stoi(line);
	}

	std::cout << "Answer: " << resultFrequency << std::endl;
}

void Day01_2::CleanUp()
{

}
