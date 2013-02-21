// PhoneNumView.cpp : implementation of the CPhoneNumView class
//

#include "stdafx.h"
#include "PhoneNum.h"


#include "PhoneNumView.h"
#include "TestDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CPhoneNumView

IMPLEMENT_DYNCREATE(CPhoneNumView, CView)

BEGIN_MESSAGE_MAP(CPhoneNumView, CView)
	//{{AFX_MSG_MAP(CPhoneNumView)
	ON_WM_CHAR()
	ON_COMMAND(IDM_DLG1, OnDlg1)
	//}}AFX_MSG_MAP
	// Standard printing commands
	ON_COMMAND(200, CPhoneNumView::OnPhone1)
	ON_COMMAND(ID_FILE_PRINT, CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_DIRECT, CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_PREVIEW, CView::OnFilePrintPreview)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CPhoneNumView construction/destruction

CPhoneNumView::CPhoneNumView()
{
	// TODO: add construction code here
	m_nIndex = -1;
	m_nMenuID = IDM_PHONE;
}

CPhoneNumView::~CPhoneNumView()
{
}

BOOL CPhoneNumView::PreCreateWindow(CREATESTRUCT& cs)
{
	// TODO: Modify the Window class or styles here by modifying
	//  the CREATESTRUCT cs

	return CView::PreCreateWindow(cs);
}

/////////////////////////////////////////////////////////////////////////////
// CPhoneNumView drawing

void CPhoneNumView::OnDraw(CDC* pDC)
{
	CPhoneNumDoc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	// TODO: add draw code for native data here
}

/////////////////////////////////////////////////////////////////////////////
// CPhoneNumView printing

BOOL CPhoneNumView::OnPreparePrinting(CPrintInfo* pInfo)
{
	// default preparation
	return DoPreparePrinting(pInfo);
}

void CPhoneNumView::OnBeginPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: add extra initialization before printing
}

void CPhoneNumView::OnEndPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: add cleanup after printing
}

/////////////////////////////////////////////////////////////////////////////
// CPhoneNumView diagnostics

#ifdef _DEBUG
void CPhoneNumView::AssertValid() const
{
	CView::AssertValid();
}

void CPhoneNumView::Dump(CDumpContext& dc) const
{
	CView::Dump(dc);
}

CPhoneNumDoc* CPhoneNumView::GetDocument() // non-debug version is inline
{
	ASSERT(m_pDocument->IsKindOf(RUNTIME_CLASS(CPhoneNumDoc)));
	return (CPhoneNumDoc*)m_pDocument;
}
#endif //_DEBUG

/////////////////////////////////////////////////////////////////////////////
// CPhoneNumView message handlers

void CPhoneNumView::OnChar(UINT nChar, UINT nRepCnt, UINT nFlags) 
{
	// TODO: Add your message handler code here and/or call default
	CClientDC dc(this);
	
	if (0x0d == nChar) {
		if (0 == ++m_nIndex) {
			m_menu.CreateMenu();
			GetParent()->GetMenu()->AppendMenu(MF_POPUP, (UINT)m_menu.m_hMenu, "phone");
			GetParent()->DrawMenuBar();
		}
		m_menu.AppendMenu(MF_STRING, m_nMenuID++, m_strLine.Left(m_strLine.Find(' ')));
		m_menu.EnableMenuItem(m_nMenuID, MF_BYCOMMAND|MF_ENABLED);

		m_strArray.Add(m_strLine);
		m_strLine.Empty();
		Invalidate();
	}else{
		m_strLine += nChar;
		dc.TextOut(0, 0, m_strLine);
	}
	CView::OnChar(nChar, nRepCnt, nFlags);
}


void CPhoneNumView::OnPhone1()
{
	
	CClientDC dc(this);
	dc.TextOut(0, 0, m_strArray.GetAt(0));
}


void CPhoneNumView::OnDlg1() 
{
	// TODO: Add your command handler code here
	//CTestDlg dlg;
	//dlg.DoModal();
	//dlg.Create(IDD_DIALOG1, this);
	//dlg.ShowWindow(SW_SHOW);

	CTestDlg* pDlg = new CTestDlg;
	pDlg->Create(IDD_DIALOG1, this);
	pDlg->ShowWindow(SW_SHOW);
}
