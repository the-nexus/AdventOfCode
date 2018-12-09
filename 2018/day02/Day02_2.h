#pragma once

#include "../../Utilities/AOCFunctionLibrary.h"

class Day02_2
{
public:
	Day02_2();
	virtual ~Day02_2();

	bool SetUp(std::string const& inputFileName);
	void Run();
	void CleanUp();

protected:
	bool ProcessSubSolution(std::vector<int> const& indices, int const firstIndex, int const lastIndex, int& solutionIndexA, int& solutionIndexB) const;

	std::vector<std::string> m_inputLines;
};