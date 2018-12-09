#include "Day03_2.h"


Day03_2::Day03_2()
{

}

Day03_2::~Day03_2()
{

}

bool Day03_2::SetUp(std::string const& inputFileName)
{
	return AOCHelper::ReadFile(inputFileName, m_inputLines);
}

void Day03_2::Run()
{
	int const fabricWidth = 1000;
	int const fabricHeight = 1000;
	int** fabricUsage = AOCHelper::CreateDoubleArray<int>(fabricWidth, fabricHeight, 0);

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

	int validClaimId = 0;
	for (size_t lineIndex = 0; lineIndex < m_inputLines.size(); ++lineIndex)
	{
		int id = 0;
		int anchorX = 0;
		int anchorY = 0;
		int width = 0;
		int height = 0;

		ParseInputString(m_inputLines[lineIndex], id, anchorX, anchorY, width, height);

		bool validClaim = true;
		for (int j = 0; validClaim && j < height; ++j)
		{
			int y = anchorY + j;
			for (int i = 0; validClaim && i < width; ++i)
			{
				int x = anchorX + i;
				validClaim &= fabricUsage[y][x] == id;
			}
		}

		if (validClaim)
		{
			validClaimId = id;
			break;
		}
	}

	if (validClaimId > 0)
	{
		std::cout << "Answer: " << validClaimId << std::endl;
	}

	AOCHelper::DestroyDoubleArray(fabricUsage, fabricHeight);
}

void Day03_2::CleanUp()
{

}

void Day03_2::ParseInputString(std::string const& inputString, int& outId, int& outX, int& outY, int& outWidth, int& outHeight) const
{
	std::vector<std::string> args;
	std::vector<std::string> pos;
	std::vector<std::string> size;

	AOCHelper::SplitString(inputString, " ", args);
	AOCHelper::SplitString(args[2], ",", pos);
	AOCHelper::SplitString(args[3], "x", size);

	outId = stoi(args[0].substr(1, args[0].size() - 1));
	outX = stoi(pos[0]);
	outY = stoi(pos[1].substr(0, pos[1].size() - 1));
	outWidth = stoi(size[0]);
	outHeight = stoi(size[1]);
}
