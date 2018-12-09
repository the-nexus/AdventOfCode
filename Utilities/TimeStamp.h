#pragma once
#include <iostream>

class TimeStamp
{
public:
	TimeStamp();

	~TimeStamp();

	void Reset();

	void SetYears(unsigned int years) { m_years = years; }
	void SetMonths(unsigned int months) { m_months = months % 12; }
	void SetDays(unsigned int days) { m_days = days % 31; }
	void SetHours(unsigned int hours) { m_hours = hours % 24; }
	void SetMinutes(unsigned int minutes) { m_minutes = minutes % 60; }
	void SetSeconds(unsigned int seconds) { m_seconds = seconds % 60; }

	inline unsigned int GetYears() const { return m_years; }
	inline unsigned int GetMonths() const { return m_months; }
	inline unsigned int GetDays() const { return m_days; }
	inline unsigned int GetHours() const { return m_hours; }
	inline unsigned int GetMinutes() const { return m_minutes; }
	inline unsigned int GetSeconds() const { return m_seconds; }

	friend bool operator< (TimeStamp const& a, TimeStamp const& b);

private:
	unsigned int m_years;
	unsigned int m_months;
	unsigned int m_days;
	unsigned int m_hours;
	unsigned int m_minutes;
	unsigned int m_seconds;
};
