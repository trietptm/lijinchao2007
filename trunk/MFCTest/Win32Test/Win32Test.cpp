// Win32Test.cpp : Defines the entry point for the application.
//

#include "stdafx.h"

int APIENTRY WinMain(HINSTANCE hInstance,
                     HINSTANCE hPrevInstance,
                     LPSTR     lpCmdLine,
                     int       nCmdShow)
{
 	// TODO: Place code here.
	HCURSOR hCursor = LoadCursor(NULL, IDC_CROSS);
	SetCursor(hCursor);
	MessageBox(NULL, "", "", MB_OK);
	return 0;
}



