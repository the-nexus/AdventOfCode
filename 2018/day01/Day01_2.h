#pragma once

#include "../../Utilities/AOCHelper.h"
#include <map>

class Day01_2
{
public:
	Day01_2();
	virtual ~Day01_2();

	bool SetUp(std::string const& inputFileName);
	void Run();
	void CleanUp();

protected:
	std::vector<std::string> m_inputLines;
	std::map<int, int> m_resultMap;
};