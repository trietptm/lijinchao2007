// PhoneNumView.h : interface of the CPhoneNumView class
//
/////////////////////////////////////////////////////////////////////////////

#if !defined(AFX_PHONENUMVIEW_H__61856EDE_4C6E_4B96_84CE_EB8B4C04EA36__INCLUDED_)
#define AFX_PHONENUMVIEW_H__61856EDE_4C6E_4B96_84CE_EB8B4C04EA36__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "PhoneNumDoc.h"

class CPhoneNumView : public CView
{
protected: // create from serialization only
	CPhoneNumView();
	DECLARE_DYNCREATE(CPhoneNumView)

// Attributes
public:
	CPhoneNumDoc* GetDocument();

// Operations
public:

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CPhoneNumView)
	public:
	virtual void OnDraw(CDC* pDC);  // overridden to draw this view
	virtual BOOL PreCreateWindow(CREATESTRUCT& cs);
	protected:
	virtual BOOL OnPreparePrinting(CPrintInfo* pInfo);
	virtual void OnBeginPrinting(CDC* pDC, CPrintInfo* pInfo);
	virtual void OnEndPrinting(CDC* pDC, CPrintInfo* pInfo);
	//}}AFX_VIRTUAL

// Implementation
public:
	CStringArray m_strArray;
	int m_nMenuID;
	virtual ~CPhoneNumView();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// Generated message map functions
protected:
	//{{AFX_MSG(CPhoneNumView)
	afx_msg void OnChar(UINT nChar, UINT nRepCnt, UINT nFlags);
	afx_msg void OnDlg1();
	//}}AFX_MSG
	afx_msg void OnPhone1();
	DECLARE_MESSAGE_MAP()
private:

	CString m_strLine;
	CMenu m_menu;
	int m_nIndex;
};

#ifndef _DEBUG  // debug version in PhoneNumView.cpp
inline CPhoneNumDoc* CPhoneNumView::GetDocument()
   { return (CPhoneNumDoc*)m_pDocument; }
#endif

/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_PHONENUMVIEW_H__61856EDE_4C6E_4B96_84CE_EB8B4C04EA36__INCLUDED_)
