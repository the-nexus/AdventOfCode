#include "Day04_1.h"


Day04_1::Day04_1()
{

}

Day04_1::~Day04_1()
{

}

bool Day04_1::SetUp(std::string const& inputFileName)
{
	return AOCFunctionLibrary::ReadFile(inputFileName, m_inputLines);
}

void Day04_1::Run()
{
	std::vector<GuardLog> guardLogs;
	guardLogs.resize(m_inputLines.size());
	for (size_t lineIndex = 0; lineIndex < m_inputLines.size(); ++lineIndex)
	{
		ProcessInputString(m_inputLines[lineIndex], guardLogs[lineIndex]);
	}

	std::sort(guardLogs.begin(), guardLogs.end(), GuardLog::LessThanComparator());

	int lastGuardId = -1;
	for (size_t logIndex = 0; logIndex < guardLogs.size(); ++logIndex)
	{
		if (guardLogs[logIndex].m_id == -1)
		{
			guardLogs[logIndex].m_id = lastGuardId;
		}
		else
		{
			lastGuardId = guardLogs[logIndex].m_id;
		}
	}

	std::map<int, std::vector<int>> guardTimelines;
	int wasAsleep = false;
	int sleepStartTime = 60;
	for (size_t logIndex = 0; logIndex < guardLogs.size(); ++logIndex)
	{
		if (!guardLogs[logIndex].m_awake)
		{
			wasAsleep = true;
			sleepStartTime = guardLogs[logIndex].m_time.GetMinutes();
		}
		else if (wasAsleep)
		{
			int guardId = guardLogs[logIndex].m_id;
			std::vector<int>& dataVec = guardTimelines[guardId];
			dataVec.resize(60);

			int sleepEndTime = guardLogs[logIndex].m_time.GetMinutes();
			for (int minute = sleepStartTime; minute < sleepEndTime; ++minute)
			{
				dataVec[minute] += 1;
			}

			wasAsleep = false;
			sleepStartTime = 60;
		}
	}

	int bestGuardId = 0;
	int bestTotal = 0;
	int bestMinute = 0;
	for (std::pair<int, std::vector<int>> const& guardTimeline : guardTimelines)
	{
		int localGuardId = guardTimeline.first;
		int localBestMinute = 0;
		int localBestCount = 0;
		int localTotal = 0;
		for (int minute = 0; minute < guardTimeline.second.size(); ++minute)
		{
			int count = guardTimeline.second[minute];
			localTotal += count;
			
			if (count > localBestCount)
			{
				localBestCount = count;
				localBestMinute = minute;
			}
		}

		if (localTotal > bestTotal)
		{
			bestGuardId = localGuardId;
			bestTotal = localTotal;
			bestMinute = localBestMinute;
		}
	}

	int resultValue = bestGuardId * bestMinute;
	std::cout << "Answer: " << resultValue << std::endl;
}

void Day04_1::CleanUp()
{

}

void Day04_1::ProcessInputString(std::string const& inputString, GuardLog& outGuardLog) const
{
	outGuardLog.m_time.SetYears(std::stoi(inputString.substr(1, 4)));
	outGuardLog.m_time.SetMonths(std::stoi(inputString.substr(6, 2)));
	outGuardLog.m_time.SetDays(std::stoi(inputString.substr(9, 2)));
	outGuardLog.m_time.SetHours(std::stoi(inputString.substr(12, 2)));
	outGuardLog.m_time.SetMinutes(std::stoi(inputString.substr(15, 2)));
	outGuardLog.m_time.SetSeconds(0);

	if (inputString[25] == '#')
	{
		outGuardLog.m_id = std::stoi(inputString.substr(26, inputString.find(' ', 26) - 26));
		outGuardLog.m_awake = true;
	}
	else
	{
		outGuardLog.m_awake = inputString[19] == 'w';
	}
}
