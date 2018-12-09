#include "Day02_2.h"


Day02_2::Day02_2()
{

}

Day02_2::~Day02_2()
{

}

bool Day02_2::SetUp(std::string const& inputFileName)
{
	return AOCFunctionLibrary::ReadFile(inputFileName, m_inputLines);
}

void Day02_2::Run()
{
	// Handle everything has indices of the lines to use to lighten the processing load
	int lineCount = (int)m_inputLines.size();
	std::vector<int> inputLineIndices;
	inputLineIndices.resize(lineCount);
	for (int index = 0; index < lineCount; ++index)
	{
		inputLineIndices[index] = index;
	}

	// Reset the RNG to avoid always getting the same results when running the program
	AOCFunctionLibrary::ResetRNG();

	// Run a divide-to-conquer algorithm by splitting the load into sub-solutions
	int const itemsPerGroup = (int)sqrt(lineCount) + 1;
	bool foundSolution = false;
	int solutionIndexA = 0;
	int solutionIndexB = 0;
	int iterationCount = 0;

	while (!foundSolution)
	{
		std::cout << "Iteration #" << ++iterationCount << std::endl;

		// Shuffle the indices to generate new sub-solutions to process
		AOCFunctionLibrary::ShuffleVector(inputLineIndices);

		int firstIndex = 0;
		int lastIndex = itemsPerGroup < lineCount ? itemsPerGroup : lineCount;
		while (firstIndex < lastIndex)
		{
			// Process the current sub-solution
			if (ProcessSubSolution(inputLineIndices, firstIndex, lastIndex, solutionIndexA, solutionIndexB))
			{
				// End the search if we found a valid result
				foundSolution = true;
				break;
			}

			firstIndex = lastIndex;
			lastIndex += itemsPerGroup;
			lastIndex = lastIndex < lineCount ? lastIndex : lineCount;
		}
	}

	// Parse the results to obtain the identical characters in the order they appear
	std::string const& solutionA = m_inputLines[solutionIndexA];
	std::string const& solutionB = m_inputLines[solutionIndexB];

	std::string commonSymbols = "";
	for (size_t symbolIndex = 0; symbolIndex < solutionA.length(); ++symbolIndex)
	{
		char symbolA = solutionA[symbolIndex];
		char symbolB = solutionB[symbolIndex];

		if (symbolA == symbolB)
		{
			commonSymbols += symbolA;
		}
	}
	std::cout << "Answer: " << commonSymbols << std::endl;
}

void Day02_2::CleanUp()
{

}

bool Day02_2::ProcessSubSolution(std::vector<int> const& indices, int const firstIndex, int const lastIndex, int& solutionIndexA, int& solutionIndexB) const
{
	for (int i = firstIndex; i < lastIndex; ++i)
	{
		for (int j = i + 1; j < lastIndex; ++j)
		{
			int indexA = indices[i];
			int indexB = indices[j];

			std::string const& itemA = m_inputLines[indexA];
			std::string const& itemB = m_inputLines[indexB];

			// Compare each symbol of the strings by position
			int differentSymbolCount = 0;
			for (size_t symbolIndex = 0; symbolIndex < itemA.length(); ++symbolIndex)
			{
				char symbolA = itemA[symbolIndex];
				char symbolB = itemB[symbolIndex];

				if (symbolA != symbolB)
				{
					++differentSymbolCount;
				}
			}

			// We have found the problem's solution when there is only 1 symbol that is different
			if (differentSymbolCount == 1)
			{
				solutionIndexA = indexA;
				solutionIndexB = indexB;
				return true;
			}
		}
	}

	return false;
}
