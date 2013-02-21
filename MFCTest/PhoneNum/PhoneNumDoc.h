// PhoneNumDoc.h : interface of the CPhoneNumDoc class
//
/////////////////////////////////////////////////////////////////////////////

#if !defined(AFX_PHONENUMDOC_H__A02A5D3F_7A64_4D0D_B4EE_623E7628FA4C__INCLUDED_)
#define AFX_PHONENUMDOC_H__A02A5D3F_7A64_4D0D_B4EE_623E7628FA4C__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000


class CPhoneNumDoc : public CDocument
{
protected: // create from serialization only
	CPhoneNumDoc();
	DECLARE_DYNCREATE(CPhoneNumDoc)

// Attributes
public:

// Operations
public:

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CPhoneNumDoc)
	public:
	virtual BOOL OnNewDocument();
	virtual void Serialize(CArchive& ar);
	//}}AFX_VIRTUAL

// Implementation
public:
	virtual ~CPhoneNumDoc();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// Generated message map functions
protected:
	//{{AFX_MSG(CPhoneNumDoc)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_PHONENUMDOC_H__A02A5D3F_7A64_4D0D_B4EE_623E7628FA4C__INCLUDED_)
