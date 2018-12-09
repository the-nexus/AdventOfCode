#pragma once

#include "../../Utilities/AOCFunctionLibrary.h"

class Day01_1
{
public:
	Day01_1();
	virtual ~Day01_1();

	bool SetUp(std::string const& inputFileName);
	void Run();
	void CleanUp();

protected:
	std::vector<std::string> m_inputLines;
};