// MainFrm.cpp : implementation of the CMainFrame class
//

#include "stdafx.h"
#include "MFCTest.h"
#include "MainFrm.h"
#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CMainFrame

IMPLEMENT_DYNCREATE(CMainFrame, CFrameWnd)

BEGIN_MESSAGE_MAP(CMainFrame, CFrameWnd)
	//{{AFX_MSG_MAP(CMainFrame)
	ON_WM_CREATE()
	ON_COMMAND(ID_TEST, OnTest)
	ON_COMMAND(IDM_SHOWMSG, OnShowmsg)
	ON_COMMAND(1111, OnVCTEST)
	ON_UPDATE_COMMAND_UI(ID_EDIT_CUT, OnUpdateEditCut)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

static UINT indicators[] =
{
	ID_SEPARATOR,           // status line indicator
	ID_INDICATOR_CAPS,
	ID_INDICATOR_NUM,
	ID_INDICATOR_SCRL,
};

/////////////////////////////////////////////////////////////////////////////
// CMainFrame construction/destruction

CMainFrame::CMainFrame()
{
	// TODO: add member initialization code here
	m_bAutoMenuEnable = FALSE;
}

CMainFrame::~CMainFrame()
{
}

int CMainFrame::OnCreate(LPCREATESTRUCT lpCreateStruct)
{
	if (CFrameWnd::OnCreate(lpCreateStruct) == -1)
		return -1;

	if (!m_wndToolBar.CreateEx(this, TBSTYLE_FLAT, WS_CHILD | WS_VISIBLE | CBRS_TOP
		| CBRS_GRIPPER | CBRS_TOOLTIPS | CBRS_FLYBY | CBRS_SIZE_DYNAMIC) ||
		!m_wndToolBar.LoadToolBar(IDR_MAINFRAME))
	{
		TRACE0("Failed to create toolbar\n");
		return -1;      // fail to create
	}

	if (!m_wndStatusBar.Create(this) ||
		!m_wndStatusBar.SetIndicators(indicators,
		  sizeof(indicators)/sizeof(UINT)))
	{
		TRACE0("Failed to create status bar\n");
		return -1;      // fail to create
	}

	// TODO: Delete these three lines if you don't want the toolbar to
	//  be dockable
	m_wndToolBar.EnableDocking(CBRS_ALIGN_ANY);
	EnableDocking(CBRS_ALIGN_ANY);
	DockControlBar(&m_wndToolBar); 
	
	//GetMenu()->GetSubMenu(0)->CheckMenuItem(0, MF_BYPOSITION|MF_CHECKED);
	GetMenu()->GetSubMenu(0)->CheckMenuItem(ID_FILE_NEW, MF_BYCOMMAND|MF_CHECKED);
	GetMenu()->GetSubMenu(0)->SetDefaultItem(0, TRUE);
	
	CString str;
	str.Format("x= %d, y=%d", GetSystemMetrics(SM_CXMENUCHECK), GetSystemMetrics(SM_CYMENUCHECK));


	m_btChecked.LoadBitmap(IDB_CHECKED);
	m_btUnchecked.LoadBitmap(IDB_UNCHECKED);
	GetMenu()->GetSubMenu(0)->SetMenuItemBitmaps(0, MF_BYPOSITION, &m_btUnchecked, &m_btChecked);
	GetMenu()->GetSubMenu(0)->EnableMenuItem(1, MF_BYPOSITION|MF_DISABLED|MF_GRAYED);

	m_btn.Create("button", WS_CHILD|BS_DEFPUSHBUTTON, CRect(0, 0, 100, 100), this, IDB_Test);
	//m_btn.ShowWindow(SW_SHOWNORMAL);

//	CMenu menu;
//	menu.LoadMenu(IDR_MENU1);
//	SetMenu(&menu);
	
	CMenu menu;
	menu.CreateMenu();
	//GetMenu()->AppendMenu(MF_POPUP, (UINT)menu.m_hMenu, "Test");
	GetMenu()->InsertMenu(2, MF_POPUP|MF_BYPOSITION, (UINT)menu.m_hMenu, "Test");
	menu.AppendMenu(MF_STRING, 111, "HEL");
	
	GetMenu()->GetSubMenu(0)->InsertMenu(ID_FILE_NEW, MF_BYCOMMAND|MF_STRING,  1111, "VC");
	menu.Detach();

	return 0;
}

BOOL CMainFrame::PreCreateWindow(CREATESTRUCT& cs)
{
	if( !CFrameWnd::PreCreateWindow(cs) )
		return FALSE;
	// TODO: Modify the Window class or styles here by modifying
	//  the CREATESTRUCT cs

	return TRUE;
}

/////////////////////////////////////////////////////////////////////////////
// CMainFrame diagnostics

#ifdef _DEBUG
void CMainFrame::AssertValid() const
{
	CFrameWnd::AssertValid();
}

void CMainFrame::Dump(CDumpContext& dc) const
{
	CFrameWnd::Dump(dc);
}

#endif //_DEBUG

/////////////////////////////////////////////////////////////////////////////
// CMainFrame message handlers


void CMainFrame::OnTest() 
{
MessageBox("aa", NULL, MB_OK);	
}

void CMainFrame::OnVCTEST() 
{
MessageBox("OnVCTEST");	
}



//DEL void CMainFrame::OnLButtonDown(UINT nFlags, CPoint point) 
//DEL {
//DEL 	// TODO: Add your message handler code here and/or call default
//DEL 	
//DEL 	MessageBox("", NULL, MB_OK);
//DEL 	CFrameWnd::OnLButtonDown(nFlags, point);
//DEL }

//DEL void CMainFrame::OnLButtonUp(UINT nFlags, CPoint point) 
//DEL {
//DEL 	// TODO: Add your message handler code here and/or call default
//DEL 	
//DEL 	CFrameWnd::OnLButtonUp(nFlags, point);
//DEL }

void CMainFrame::OnShowmsg() 
{
	// TODO: Add your command handler code here
	AfxMessageBox("fram click");
}

void CMainFrame::OnUpdateEditCut(CCmdUI* pCmdUI) 
{
	// TODO: Add your command update UI handler code here
	pCmdUI->Enable(TRUE);
	//pCmdUI->SetText("adfas");
}
