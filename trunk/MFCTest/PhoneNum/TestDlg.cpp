// TestDlg.cpp : implementation file
//

#include "stdafx.h"
#include "PhoneNum.h"
#include "TestDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CTestDlg dialog


CTestDlg::CTestDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CTestDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CTestDlg)
	m_nNum1 = 0;
	m_nNum2 = 0;
	m_nNum3 = 0;
	//}}AFX_DATA_INIT
}


void CTestDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CTestDlg)
	DDX_Control(pDX, IDC_EDIT3, m_edit3);
	DDX_Text(pDX, IDC_EDIT1, m_nNum1);
	DDX_Text(pDX, IDC_EDIT2, m_nNum2);
	DDX_Text(pDX, IDC_EDIT3, m_nNum3);
	//}}AFX_DATA_MAP
}


BEGIN_MESSAGE_MAP(CTestDlg, CDialog)
	//{{AFX_MSG_MAP(CTestDlg)
	ON_BN_CLICKED(IDC_BUTTON1, OnButton1)
	ON_BN_CLICKED(IDC_BUTTON2, OnButton2)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CTestDlg message handlers

void CTestDlg::OnButton1() 
{
//	// TODO: Add your control notification handler code here
//	if (!m_btn.m_hWnd) {
//		m_btn.Create("new", BS_DEFPUSHBUTTON|WS_VISIBLE|WS_CHILD, CRect(0, 0, 100, 100), this, 123);
//	}else{
//		m_btn.DestroyWindow();
//	}

	int num1, num2, num3;
	//char cha1[10], cha2[10], cha3[10];

	//GetDlgItem(IDC_EDIT1)->GetWindowText(cha1, 10);
	//GetDlgItem(IDC_EDIT2)->GetWindowText(cha2, 10);

	//GetDlgItemText(IDC_EDIT1, cha1, 10);
	//GetDlgItemText(IDC_EDIT2, cha2, 10);

//	num1 = GetDlgItemInt(IDC_EDIT1);
//	num2 = GetDlgItemInt(IDC_EDIT2);
//
//
//	num3 = num1 + num2;
//	SetDlgItemInt(IDC_EDIT3, num3);

	UpdateData();
	m_nNum3 = m_nNum1 + m_nNum2;
	UpdateData(FALSE);
	m_edit3.SetFocus();
}

void CTestDlg::OnButton2() 
{
	// TODO: Add your control notification handler code here
	CString str;
	GetDlgItemText(IDC_BUTTON2, str);

	
	static CRect rectLarge;
	static CRect rectSmall;
	if (rectLarge.IsRectNull()) {
		CRect rectSeparator;
		GetWindowRect(&rectLarge);
		GetDlgItem(IDC_SEPERATOR)->GetWindowRect(&rectSeparator);
		
		rectSmall.left = rectLarge.left;
		rectSmall.top = rectLarge.top;
		rectSmall.right = rectLarge.right;
		rectSmall.bottom = rectSeparator.bottom;
	}
	
	
	if (str=="<<") {
		SetDlgItemText(IDC_BUTTON2, ">>");
		SetWindowPos(NULL, 0, 0, rectSmall.Width(), rectSmall.Height(), 
			SWP_NOMOVE|SWP_NOZORDER);
	}else{
		SetDlgItemText(IDC_BUTTON2, "<<");
		SetWindowPos(NULL, 0, 0, rectLarge.Width(), rectLarge.Height(), 
			SWP_NOMOVE|SWP_NOZORDER);
	}

}


WNDPROC preProc;

LRESULT CALLBACK NewEditProc(
							 HWND hwnd,
							 UINT uMsg,
							 WPARAM wParam,
							 LPARAM lParam)
{
	if (uMsg == WM_CHAR && wParam == 0x0d) {
		SetFocus(::GetNextWindow(hwnd, GW_HWNDNEXT));
		return 1;
	}else{
		return preProc(hwnd, uMsg, wParam, lParam);
	}
}


BOOL CTestDlg::OnInitDialog() 
{
	CDialog::OnInitDialog();
	
//	preProc = (WNDPROC)SetWindowLong(GetDlgItem(IDC_EDIT1)->m_hWnd, 
//		GWL_WNDPROC, (LONG)NewEditProc);
	
	// TODO: Add extra initialization here
	
	return TRUE;  // return TRUE unless you set the focus to a control
	              // EXCEPTION: OCX Property Pages should return FALSE
}

void CTestDlg::OnOK() 
{
	GetFocus()->GetNextWindow()->SetFocus();
	//GetNextDlgTabItem(GetFocus())->SetFocus();
	//CDialog::OnOK();
}
