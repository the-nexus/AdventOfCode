#include "DayN_1.h"


DayN_1::DayN_1()
{

}

DayN_1::~DayN_1()
{

}

bool DayN_1::SetUp(std::string const& inputFileName)
{
	return AOCHelper::ReadFile(inputFileName, m_inputLines);
}

void DayN_1::Run()
{
	for (std::string const& line : m_inputLines)
	{
		std::cout << line << std::endl;
	}
}

void DayN_1::CleanUp()
{

}
