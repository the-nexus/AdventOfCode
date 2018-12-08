#pragma once

#include "../../Utilities/AOCHelper.h"

class Day03_2
{
public:
	Day03_2();
	virtual ~Day03_2();

	bool SetUp(std::string const& inputFileName);
	void Run();
	void CleanUp();

protected:
	std::vector<std::string> m_inputLines;
};