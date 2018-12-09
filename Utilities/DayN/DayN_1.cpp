#include "DayN_1.h"


DayN_1::DayN_1()
{

}

DayN_1::~DayN_1()
{

}

bool DayN_1::SetUp(std::string const& inputFileName)
{
	return AOCFunctionLibrary::ReadFile(inputFileName, m_inputLines);
}

void DayN_1::Run()
{
	for (size_t lineIdx = 0; lineIdx < m_inputLines.size(); ++lineIdx)
	{
		std::cout << m_inputLines[lineIdx] << std::endl;
	}
}

void DayN_1::CleanUp()
{

}
