// PhoneNumDoc.cpp : implementation of the CPhoneNumDoc class
//

#include "stdafx.h"
#include "PhoneNum.h"

#include "PhoneNumDoc.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CPhoneNumDoc

IMPLEMENT_DYNCREATE(CPhoneNumDoc, CDocument)

BEGIN_MESSAGE_MAP(CPhoneNumDoc, CDocument)
	//{{AFX_MSG_MAP(CPhoneNumDoc)
		// NOTE - the ClassWizard will add and remove mapping macros here.
		//    DO NOT EDIT what you see in these blocks of generated code!
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CPhoneNumDoc construction/destruction

CPhoneNumDoc::CPhoneNumDoc()
{
	// TODO: add one-time construction code here

}

CPhoneNumDoc::~CPhoneNumDoc()
{
}

BOOL CPhoneNumDoc::OnNewDocument()
{
	if (!CDocument::OnNewDocument())
		return FALSE;

	// TODO: add reinitialization code here
	// (SDI documents will reuse this document)

	return TRUE;
}



/////////////////////////////////////////////////////////////////////////////
// CPhoneNumDoc serialization

void CPhoneNumDoc::Serialize(CArchive& ar)
{
	if (ar.IsStoring())
	{
		// TODO: add storing code here
	}
	else
	{
		// TODO: add loading code here
	}
}

/////////////////////////////////////////////////////////////////////////////
// CPhoneNumDoc diagnostics

#ifdef _DEBUG
void CPhoneNumDoc::AssertValid() const
{
	CDocument::AssertValid();
}

void CPhoneNumDoc::Dump(CDumpContext& dc) const
{
	CDocument::Dump(dc);
}
#endif //_DEBUG

/////////////////////////////////////////////////////////////////////////////
// CPhoneNumDoc commands
