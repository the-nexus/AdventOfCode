#pragma once

#include "../../Utilities/AOCFunctionLibrary.h"

class Day04_2
{
public:
	Day04_2();
	virtual ~Day04_2();

	bool SetUp(std::string const& inputFileName);
	void Run();
	void CleanUp();

protected:
	std::vector<std::string> m_inputLines;
};