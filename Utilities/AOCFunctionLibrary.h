#pragma once

#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <map>

class AOCFunctionLibrary
{
public:
	//////////////////////////////////////////////////////////////////////////////////////////////////
	// File I/O
	static bool ReadFile(std::string const& fileName, std::vector<std::string>& outLines);



	//////////////////////////////////////////////////////////////////////////////////////////////////
	// String
	static void SplitString(std::string const& stringToSplit, std::string const& delimiter, std::vector<std::string>& outStrings);



	//////////////////////////////////////////////////////////////////////////////////////////////////
	// Random
	static void ResetRNG();



	//////////////////////////////////////////////////////////////////////////////////////////////////
	// Vector
	template<typename T>
	static void ShuffleVector(std::vector<T>& target)
	{
		std::random_shuffle(target.begin(), target.end());
	}



	//////////////////////////////////////////////////////////////////////////////////////////////////
	// Arrays
	template<typename T>
	static T* CreateArray(int width, T defaultValue)
	{
		T* values = new T[width];
		for (int index = 0; index < width; ++index)
		{
			values[index] = defaultValue;
		}
		return values;
	}

	template<typename T>
	static void DestroyArray(T* values)
	{
		delete values;
		values = nullptr;
	}

	template<typename T>
	static T** CreateDoubleArray(int width, int height, T defaultValue)
	{
		T** values = CreateArray<T*>(width, nullptr);
		for (int index = 0; index < height; ++index)
		{
			values[index] = CreateArray<T>(width, defaultValue);
		}
		return values;
	}

	template<typename T>
	static void DestroyDoubleArray(T** values, int height)
	{
		for (int index = 0; index < height; ++index)
		{
			DestroyArray<T>(values[index]);
		}
		DestroyArray<T*>(values);
	}
};
