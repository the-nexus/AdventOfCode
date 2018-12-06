#pragma once

#include "../../Utilities/AOCHelper.h"

class Day02_2
{
public:
	Day02_2();
	virtual ~Day02_2();

	bool SetUp(std::string const& inputFileName);
	void Run();
	void CleanUp();

protected:
	std::vector<std::string> m_inputLines;
};