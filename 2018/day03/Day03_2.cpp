#include "Day03_2.h"


Day03_2::Day03_2()
{

}

Day03_2::~Day03_2()
{

}

bool Day03_2::SetUp(std::string const& inputFileName)
{
	return AOCHelper::ReadFile(inputFileName, m_inputLines);
}

void Day03_2::Run()
{
	for (size_t lineIdx = 0; lineIdx < m_inputLines.size(); ++lineIdx)
	{
		std::cout << m_inputLines[lineIdx] << std::endl;
	}
}

void Day03_2::CleanUp()
{

}
