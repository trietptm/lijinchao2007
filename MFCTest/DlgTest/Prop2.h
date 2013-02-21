#if !defined(AFX_PROP2_H__7B9BE45A_08AC_4145_B3D9_849E9150F242__INCLUDED_)
#define AFX_PROP2_H__7B9BE45A_08AC_4145_B3D9_849E9150F242__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// Prop2.h : header file
//

/////////////////////////////////////////////////////////////////////////////
// CProp2 dialog

class CProp2 : public CPropertyPage
{
	DECLARE_DYNCREATE(CProp2)

// Construction
public:
	CProp2();
	~CProp2();

// Dialog Data
	//{{AFX_DATA(CProp2)
	enum { IDD = IDD_PROPPAGE_LARGE1 };
		// NOTE - ClassWizard will add data members here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_DATA


// Overrides
	// ClassWizard generate virtual function overrides
	//{{AFX_VIRTUAL(CProp2)
	protected:
	virtual BOOL OnSetActive();
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	// Generated message map functions
	//{{AFX_MSG(CProp2)
		// NOTE: the ClassWizard will add member functions here
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()

};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_PROP2_H__7B9BE45A_08AC_4145_B3D9_849E9150F242__INCLUDED_)
