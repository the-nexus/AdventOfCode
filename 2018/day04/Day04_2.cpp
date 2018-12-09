#include "Day04_2.h"


Day04_2::Day04_2()
{

}

Day04_2::~Day04_2()
{

}

bool Day04_2::SetUp(std::string const& inputFileName)
{
	return AOCFunctionLibrary::ReadFile(inputFileName, m_inputLines);
}

void Day04_2::Run()
{
	for (size_t lineIdx = 0; lineIdx < m_inputLines.size(); ++lineIdx)
	{
		std::cout << m_inputLines[lineIdx] << std::endl;
	}
}

void Day04_2::CleanUp()
{

}
