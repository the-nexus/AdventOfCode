#include "TimeStamp.h"


TimeStamp::TimeStamp() :
	m_years(0),
	m_months(0),
	m_days(0),
	m_hours(0),
	m_minutes(0),
	m_seconds(0)
{

}

TimeStamp::~TimeStamp()
{

}

void TimeStamp::Reset()
{
	m_years = 0;
	m_months = 0;
	m_days = 0;
	m_hours = 0;
	m_minutes = 0;
	m_seconds = 0;
}

bool operator< (TimeStamp const& lhs, TimeStamp const& rhs)
{
	return lhs.GetYears() < rhs.GetYears()
		&& lhs.GetMonths() < rhs.GetMonths()
		&& lhs.GetDays() < rhs.GetDays()
		&& lhs.GetHours() < rhs.GetHours()
		&& lhs.GetMinutes() < rhs.GetMinutes()
		&& lhs.GetSeconds() < rhs.GetSeconds();
}
