// MFCTestView.h : interface of the CMFCTestView class
//
/////////////////////////////////////////////////////////////////////////////

#if !defined(AFX_MFCTESTVIEW_H__B227DD36_24AE_4BF9_99AE_77EFFF0A7FFF__INCLUDED_)
#define AFX_MFCTESTVIEW_H__B227DD36_24AE_4BF9_99AE_77EFFF0A7FFF__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000


class CMFCTestView : public CView
{
protected: // create from serialization only
	CMFCTestView();
	DECLARE_DYNCREATE(CMFCTestView)

// Attributes
public:
	CMFCTestDoc* GetDocument();

// Operations
public:

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CMFCTestView)
	public:
	virtual void OnDraw(CDC* pDC);  // overridden to draw this view
	virtual BOOL PreCreateWindow(CREATESTRUCT& cs);
	virtual BOOL Create(LPCTSTR lpszClassName, LPCTSTR lpszWindowName, DWORD dwStyle, const RECT& rect, CWnd* pParentWnd, UINT nID, CCreateContext* pContext = NULL);
	//}}AFX_VIRTUAL

// Implementation
public:
	virtual ~CMFCTestView();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// Generated message map functions
protected:
	//{{AFX_MSG(CMFCTestView)
	afx_msg void OnLButtonDown(UINT nFlags, CPoint point);
	afx_msg void OnLButtonUp(UINT nFlags, CPoint point);
	afx_msg void OnMouseMove(UINT nFlags, CPoint point);
	afx_msg int OnCreate(LPCREATESTRUCT lpCreateStruct);
	afx_msg void OnChar(UINT nChar, UINT nRepCnt, UINT nFlags);
	afx_msg void OnTimer(UINT nIDEvent);
	afx_msg void OnRButtonDown(UINT nFlags, CPoint point);
	afx_msg void OnContextMenu(CWnd*, CPoint point);
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
private:
	int m_nTimerTextWidth;
	CPoint m_ptTextPos;
	CString m_strLine;
	CPoint m_ptOld;
	BOOL m_bDraw;
	CPoint m_ptOrigin;
};

#ifndef _DEBUG  // debug version in MFCTestView.cpp
inline CMFCTestDoc* CMFCTestView::GetDocument()
   { return (CMFCTestDoc*)m_pDocument; }
#endif

/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_MFCTESTVIEW_H__B227DD36_24AE_4BF9_99AE_77EFFF0A7FFF__INCLUDED_)
