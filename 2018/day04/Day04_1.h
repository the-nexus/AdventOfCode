#pragma once

#include "../../Utilities/AOCFunctionLibrary.h"
#include "../../Utilities/TimeStamp.h"

class Day04_1
{
public:
	struct GuardLog
	{
		GuardLog() :
			m_id(-1),
			m_awake(true)
		{}

		int m_id;
		bool m_awake;
		TimeStamp m_time;

		struct LessThanComparator
		{
			bool operator() (const GuardLog& lhs, const GuardLog& rhs)
			{
				return lhs.m_time < rhs.m_time;
			}
		};
	};

	Day04_1();
	virtual ~Day04_1();

	bool SetUp(std::string const& inputFileName);
	void Run();
	void CleanUp();

protected:
	void ProcessInputString(std::string const& inputString, GuardLog& outGuardData) const;

	std::vector<std::string> m_inputLines;
};
