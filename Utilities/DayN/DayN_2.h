#pragma once

#include "../../Utilities/AOCFunctionLibrary.h"

class DayN_2
{
public:
	DayN_2();
	virtual ~DayN_2();

	bool SetUp(std::string const& inputFileName);
	void Run();
	void CleanUp();

protected:
	std::vector<std::string> m_inputLines;
};