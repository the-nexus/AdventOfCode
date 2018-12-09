#include "Day03_1.h"


Day03_1::Day03_1()
{

}

Day03_1::~Day03_1()
{

}

bool Day03_1::SetUp(std::string const& inputFileName)
{
	return AOCFunctionLibrary::ReadFile(inputFileName, m_inputLines);
}

void Day03_1::Run()
{
	int const fabricWidth = 1000;
	int const fabricHeight = 1000;
	int** fabricUsage = AOCFunctionLibrary::CreateDoubleArray<int>(fabricWidth, fabricHeight, 0);

	for (size_t lineIndex = 0; lineIndex < m_inputLines.size(); ++lineIndex)
	{
		int id = 0;
		int anchorX = 0;
		int anchorY = 0;
		int width = 0;
		int height = 0;

		ParseInputString(m_inputLines[lineIndex], id, anchorX, anchorY, width, height);

		for (int j = 0; j < height; ++j)
		{
			int y = anchorY + j;
			for (int i = 0; i < width; ++i)
			{
				int x = anchorX + i;
				fabricUsage[y][x] = fabricUsage[y][x] == 0 ? id : -1;
			}
		}
	}

	// Measure the overlapping areas
	int overlappingClaims = 0;
	for (int j = 0; j < fabricHeight; ++j)
	{
		for (int i = 0; i < fabricWidth; ++i)
		{
			if (fabricUsage[j][i] == -1)
			{
				++overlappingClaims;
			}
		}
	}
	std::cout << "Answer: " << overlappingClaims << std::endl;

	AOCFunctionLibrary::DestroyDoubleArray(fabricUsage, fabricHeight);
}

void Day03_1::CleanUp()
{

}

void Day03_1::ParseInputString(std::string const& inputString, int& outId, int& outX, int& outY, int& outWidth, int& outHeight) const
{
	std::vector<std::string> args;
	std::vector<std::string> pos;
	std::vector<std::string> size;

	AOCFunctionLibrary::SplitString(inputString, " ", args);
	AOCFunctionLibrary::SplitString(args[2], ",", pos);
	AOCFunctionLibrary::SplitString(args[3], "x", size);

	outId = stoi(args[0].substr(1, args[0].size() - 1));
	outX = stoi(pos[0]);
	outY = stoi(pos[1].substr(0, pos[1].size() - 1));
	outWidth = stoi(size[0]);
	outHeight = stoi(size[1]);
}
