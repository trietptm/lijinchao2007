// MFCTestDoc.h : interface of the CMFCTestDoc class
//
/////////////////////////////////////////////////////////////////////////////

#if !defined(AFX_MFCTESTDOC_H__7B961517_4159_4DF9_B963_654CFEA044D2__INCLUDED_)
#define AFX_MFCTESTDOC_H__7B961517_4159_4DF9_B963_654CFEA044D2__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000


class CMFCTestDoc : public CDocument
{
protected: // create from serialization only
	CMFCTestDoc();
	DECLARE_DYNCREATE(CMFCTestDoc)

// Attributes
public:

// Operations
public:

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CMFCTestDoc)
	public:
	virtual BOOL OnNewDocument();
	virtual void Serialize(CArchive& ar);
	//}}AFX_VIRTUAL

// Implementation
public:
	virtual ~CMFCTestDoc();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// Generated message map functions
protected:
	//{{AFX_MSG(CMFCTestDoc)
	afx_msg void OnShowmsg();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_MFCTESTDOC_H__7B961517_4159_4DF9_B963_654CFEA044D2__INCLUDED_)
