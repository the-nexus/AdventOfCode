#include "DayN_2.h"


DayN_2::DayN_2()
{

}

DayN_2::~DayN_2()
{

}

bool DayN_2::SetUp(std::string const& inputFileName)
{
	return AOCHelper::ReadFile(inputFileName, m_inputLines);
}

void DayN_2::Run()
{
	for (std::string const& line : m_inputLines)
	{
		std::cout << line << std::endl;
	}
}

void DayN_2::CleanUp()
{

}
