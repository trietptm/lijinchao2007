// PhoneNum.h : main header file for the PHONENUM application
//

#if !defined(AFX_PHONENUM_H__BE890C89_64AB_42F5_BEF5_DF395DE29367__INCLUDED_)
#define AFX_PHONENUM_H__BE890C89_64AB_42F5_BEF5_DF395DE29367__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"       // main symbols

/////////////////////////////////////////////////////////////////////////////
// CPhoneNumApp:
// See PhoneNum.cpp for the implementation of this class
//

class CPhoneNumApp : public CWinApp
{
public:
	CPhoneNumApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CPhoneNumApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation
	//{{AFX_MSG(CPhoneNumApp)
	afx_msg void OnAppAbout();
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_PHONENUM_H__BE890C89_64AB_42F5_BEF5_DF395DE29367__INCLUDED_)
