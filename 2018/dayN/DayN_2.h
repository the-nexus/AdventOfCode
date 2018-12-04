#pragma once

#include "../../Utilities/AOCHelper.h"

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