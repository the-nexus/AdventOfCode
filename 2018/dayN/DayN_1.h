#pragma once

#include "../../Utilities/AOCHelper.h"

class DayN_1
{
public:
	DayN_1();
	virtual ~DayN_1();

	bool SetUp(std::string const& inputFileName);
	void Run();
	void CleanUp();

protected:
	std::vector<std::string> m_inputLines;
};