// StyleView.h : interface of the CStyleView class
//
/////////////////////////////////////////////////////////////////////////////

#if !defined(AFX_STYLEVIEW_H__38E95D44_5EF5_41A4_8EC9_2BE88A7F781F__INCLUDED_)
#define AFX_STYLEVIEW_H__38E95D44_5EF5_41A4_8EC9_2BE88A7F781F__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000


class CStyleView : public CView
{
protected: // create from serialization only
	CStyleView();
	DECLARE_DYNCREATE(CStyleView)

// Attributes
public:
	CStyleDoc* GetDocument();

// Operations
public:

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CStyleView)
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
	virtual ~CStyleView();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// Generated message map functions
protected:
	//{{AFX_MSG(CStyleView)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

#ifndef _DEBUG  // debug version in StyleView.cpp
inline CStyleDoc* CStyleView::GetDocument()
   { return (CStyleDoc*)m_pDocument; }
#endif

/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_STYLEVIEW_H__38E95D44_5EF5_41A4_8EC9_2BE88A7F781F__INCLUDED_)
