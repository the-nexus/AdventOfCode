#include "Day03_1.h"


Day03_1::Day03_1()
{

}

Day03_1::~Day03_1()
{

}

bool Day03_1::SetUp(std::string const& inputFileName)
{
	return AOCHelper::ReadFile(inputFileName, m_inputLines);
}

void Day03_1::Run()
{
	for (size_t lineIdx = 0; lineIdx < m_inputLines.size(); ++lineIdx)
	{
		std::cout << m_inputLines[lineIdx] << std::endl;
	}
}

void Day03_1::CleanUp()
{

}
