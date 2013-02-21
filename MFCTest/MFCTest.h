// MFCTest.h : main header file for the MFCTEST application
//

#if !defined(AFX_MFCTEST_H__292014D3_E8E0_4084_A9AC_27B9AD3C5943__INCLUDED_)
#define AFX_MFCTEST_H__292014D3_E8E0_4084_A9AC_27B9AD3C5943__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"       // main symbols

/////////////////////////////////////////////////////////////////////////////
// CMFCTestApp:
// See MFCTest.cpp for the implementation of this class
//

class CMFCTestApp : public CWinApp
{
public:
	CMFCTestApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CMFCTestApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation
	//{{AFX_MSG(CMFCTestApp)
	afx_msg void OnAppAbout();
	afx_msg void OnShowmsg();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_MFCTEST_H__292014D3_E8E0_4084_A9AC_27B9AD3C5943__INCLUDED_)
