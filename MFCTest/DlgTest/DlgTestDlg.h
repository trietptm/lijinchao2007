// DlgTestDlg.h : header file
//

#if !defined(AFX_DLGTESTDLG_H__95E81607_DBA8_4481_8DE9_71C0C7032690__INCLUDED_)
#define AFX_DLGTESTDLG_H__95E81607_DBA8_4481_8DE9_71C0C7032690__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "NewButton.h"
#include "PropSheet.h"
/////////////////////////////////////////////////////////////////////////////
// CDlgTestDlg dialog

class CDlgTestDlg : public CDialog
{
// Construction
public:
	int m_iOccupation;
	CDlgTestDlg(CWnd* pParent = NULL);	// standard constructor

// Dialog Data
	//{{AFX_DATA(CDlgTestDlg)
	enum { IDD = IDD_DLGTEST_DIALOG };
	CNewButton	m_btn2;
	CNewButton	m_btn1;
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CDlgTestDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	//{{AFX_MSG(CDlgTestDlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg void OnButton3();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_DLGTESTDLG_H__95E81607_DBA8_4481_8DE9_71C0C7032690__INCLUDED_)
