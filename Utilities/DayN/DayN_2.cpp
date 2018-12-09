#include "DayN_2.h"


DayN_2::DayN_2()
{

}

DayN_2::~DayN_2()
{

}

bool DayN_2::SetUp(std::string const& inputFileName)
{
	return AOCFunctionLibrary::ReadFile(inputFileName, m_inputLines);
}

void DayN_2::Run()
{
	for (size_t lineIdx = 0; lineIdx < m_inputLines.size(); ++lineIdx)
	{
		std::cout << m_inputLines[lineIdx] << std::endl;
	}
}

void DayN_2::CleanUp()
{

}
