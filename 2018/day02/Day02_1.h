#pragma once

#include "../../Utilities/AOCFunctionLibrary.h"

class Day02_1
{
public:
	Day02_1();
	virtual ~Day02_1();

	bool SetUp(std::string const& inputFileName);
	void Run();
	void CleanUp();

protected:
	std::vector<std::string> m_inputLines;
};