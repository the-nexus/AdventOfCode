#pragma once

#include "../../Utilities/AOCHelper.h"

class Day03_1
{
public:
	Day03_1();
	virtual ~Day03_1();

	bool SetUp(std::string const& inputFileName);
	void Run();
	void CleanUp();

protected:
	std::vector<std::string> m_inputLines;
};