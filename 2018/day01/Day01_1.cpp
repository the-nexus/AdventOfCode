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
	for (std::string const& line : m_inputLines)
	{
		std::cout << line << std::endl;
	}
}

void Day01_1::CleanUp()
{

}
