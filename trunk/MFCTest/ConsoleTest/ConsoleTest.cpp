// ConsoleTest.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <windows.h>

int main(int argc, char* argv[])
{
	HCURSOR hCursor = LoadCursor(NULL, IDC_CROSS);
	SetCursor(hCursor);
	return 0;
}
