// Prop1.cpp : implementation file
//

#include "stdafx.h"
#include "DlgTest.h"
#include "Prop1.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CProp1 property page

IMPLEMENT_DYNCREATE(CProp1, CPropertyPage)

CProp1::CProp1() : CPropertyPage(CProp1::IDD)
{
	//{{AFX_DATA_INIT(CProp1)
	m_occupation = -1;
	//}}AFX_DATA_INIT
}

CProp1::~CProp1()
{
}

void CProp1::DoDataExchange(CDataExchange* pDX)
{
	CPropertyPage::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CProp1)
	DDX_Radio(pDX, IDC_RADIO1, m_occupation);
	//}}AFX_DATA_MAP
}


BEGIN_MESSAGE_MAP(CProp1, CPropertyPage)
	//{{AFX_MSG_MAP(CProp1)
		// NOTE: the ClassWizard will add message map macros here
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CProp1 message handlers

BOOL CProp1::OnSetActive() 
{
	// TODO: Add your specialized code here and/or call the base class
	((CPropertySheet*)GetParent())->SetWizardButtons(PSWIZB_NEXT);
	return CPropertyPage::OnSetActive();
}

LRESULT CProp1::OnWizardNext() 
{
	// TODO: Add your specialized code here and/or call the base class
	UpdateData();
	if (m_occupation == -1) {
		MessageBox("asdf");
		return -1;
	}
	return CPropertyPage::OnWizardNext();
}
