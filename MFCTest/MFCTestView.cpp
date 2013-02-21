// MFCTestView.cpp : implementation of the CMFCTestView class
//

#include "stdafx.h"
#include "MFCTest.h"

#include "MFCTestDoc.h"
#include "MFCTestView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CMFCTestView

IMPLEMENT_DYNCREATE(CMFCTestView, CView)

BEGIN_MESSAGE_MAP(CMFCTestView, CView)
	//{{AFX_MSG_MAP(CMFCTestView)
	ON_WM_LBUTTONDOWN()
	ON_WM_LBUTTONUP()
	ON_WM_MOUSEMOVE()
	ON_WM_CREATE()
	ON_WM_CHAR()
	ON_WM_TIMER()
	ON_WM_RBUTTONDOWN()
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CMFCTestView construction/destruction

CMFCTestView::CMFCTestView()
{
	// TODO: add construction code here

}

CMFCTestView::~CMFCTestView()
{
}

BOOL CMFCTestView::PreCreateWindow(CREATESTRUCT& cs)
{
	// TODO: Modify the Window class or styles here by modifying
	//  the CREATESTRUCT cs
	// cs.dwExStyle = cs.dwExStyle &&~CS_HREDRAW;
	cs.cx = 0;
	cs.cy = 0;
	cs.x = 1;
	cs.y = 10;
	return CView::PreCreateWindow(cs);
}

/////////////////////////////////////////////////////////////////////////////
// CMFCTestView drawing

void CMFCTestView::OnDraw(CDC* pDC)
{
	CMFCTestDoc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	// TODO: add draw code for native data here
//	HCURSOR hCursor = LoadCursor(NULL, IDC_CROSS);
//	SetCursor(hCursor);
//	::MessageBox(NULL, "", "", MB_OK);

	CString str("sdf");
	pDC->TextOut(0,0, str);

	
	str.LoadString(IDS_STRING_TEXT);
	pDC->TextOut(0,50, str);
	CSize sz = pDC->GetTextExtent(str);
	

	
	pDC->BeginPath();
	pDC->Rectangle(0, 50, sz.cx, 50 + sz.cy);
	pDC->EndPath();
	
	pDC->SelectClipPath(RGN_DIFF);
	for (int i=0; i<300; i+=10) {
		pDC->MoveTo(0, i);
		pDC->LineTo(300, i);

		pDC->MoveTo(i, 0);
		pDC->LineTo(i, 300);
	}
	
}

/////////////////////////////////////////////////////////////////////////////
// CMFCTestView diagnostics

#ifdef _DEBUG
void CMFCTestView::AssertValid() const
{
	CView::AssertValid();
}

void CMFCTestView::Dump(CDumpContext& dc) const
{
	CView::Dump(dc);
}

CMFCTestDoc* CMFCTestView::GetDocument() // non-debug version is inline
{
	ASSERT(m_pDocument->IsKindOf(RUNTIME_CLASS(CMFCTestDoc)));
	return (CMFCTestDoc*)m_pDocument;
}
#endif //_DEBUG

/////////////////////////////////////////////////////////////////////////////
// CMFCTestView message handlers

//DEL void CMFCTestView::OnLButtonDblClk(UINT nFlags, CPoint point) 
//DEL {
//DEL 	// TODO: Add your message handler code here and/or call default
//DEL 	MessageBox("dclick");
//DEL 	CView::OnLButtonDblClk(nFlags, point);
//DEL }

void CMFCTestView::OnLButtonDown(UINT nFlags, CPoint point) 
{
//	// TODO: Add your message handler code here and/or call default
//	m_ptOrigin=point;
//	m_ptOld = point;
//	m_bDraw = TRUE;

	SetCaretPos(point);
	m_strLine.Empty();
	m_ptTextPos = point;
	
	CView::OnLButtonDown(nFlags, point);
}

void CMFCTestView::OnLButtonUp(UINT nFlags, CPoint point) 
{
//	HDC hdc;
//	hdc = ::GetDC(m_hWnd);
//	MoveToEx(hdc, m_ptOrigin.x, m_ptOrigin.y, NULL);
//	LineTo(hdc, point.x, point.y);
//	::ReleaseDC(m_hWnd, hdc);

//	CDC* pDC = GetDC();
//	pDC->MoveTo(m_ptOrigin);
//	pDC->LineTo(point);
//	ReleaseDC(pDC);
	
//	CClientDC dc(GetParent());
//	dc.MoveTo(m_ptOrigin);
//	dc.LineTo(point);

//	CWindowDC dc(GetParent());
//	dc.MoveTo(m_ptOrigin);
//	dc.LineTo(point);

//	CWindowDC dc(GetDesktopWindow());
//	dc.MoveTo(m_ptOrigin);
//	dc.LineTo(point);
//	

//	CPen pen(PS_DASH, 1, RGB(255, 0, 0));
//	CClientDC dc(this);
//	CPen* pOldPen = dc.SelectObject(&pen);
//	dc.MoveTo(m_ptOrigin);
//	dc.LineTo(point);
// 	dc.SelectObject(pOldPen);
	
//
//	CBrush brush(RGB(255, 0, 0));
//	CClientDC dc(this);
//	dc.FillRect(CRect(m_ptOrigin, point), &brush);

//	CBitmap bitMap;
//	bitMap.LoadBitmap(IDB_BITMAP1);
//	
//	CBrush brush(&bitMap);
//	CClientDC dc(this);
// 	dc.FillRect(CRect(m_ptOrigin, point), &brush);
	

//	CClientDC dc(this);
//
//	CBrush* pBrush = CBrush::FromHandle((HBRUSH)GetStockObject(NULL_BRUSH));
//	CBrush* pOldBrush = dc.SelectObject(pBrush);
//
//	dc.Rectangle(CRect(m_ptOrigin, point));
//	dc.SelectObject(pOldBrush);
	
//	m_bDraw = FALSE;
	CView::OnLButtonUp(nFlags, point);
}

void CMFCTestView::OnMouseMove(UINT nFlags, CPoint point) 
{
	// TODO: Add your message handler code here and/or call default
//	
//	CClientDC dc(this);
//	
//	CPen pen(PS_SOLID, 12, RGB(255,0,0));
//	CPen* pOldPen = dc.SelectObject(&pen);
//	if (m_bDraw == TRUE) {
//		CClientDC dc(this);
//		dc.MoveTo(m_ptOrigin);
//		dc.LineTo(point);
//		dc.LineTo(m_ptOld);
//		m_ptOld = point;
//	}
//	dc.SelectObject(pOldPen);
	
	CView::OnMouseMove(nFlags, point);
}

BOOL CMFCTestView::Create(LPCTSTR lpszClassName, LPCTSTR lpszWindowName, DWORD dwStyle, const RECT& rect, CWnd* pParentWnd, UINT nID, CCreateContext* pContext) 
{
	// TODO: Add your specialized code here and/or call the base class
	
	return CWnd::Create(lpszClassName, lpszWindowName, dwStyle, rect, pParentWnd, nID, pContext);
}

int CMFCTestView::OnCreate(LPCREATESTRUCT lpCreateStruct) 
{
	if (CView::OnCreate(lpCreateStruct) == -1)
		return -1;
	
	// TODO: Add your specialized creation code here
	m_nTimerTextWidth = 0;
	CClientDC dc(this);
	TEXTMETRIC tm;
	dc.GetTextMetrics(&tm);
	CreateSolidCaret(tm.tmAveCharWidth/8, tm.tmHeight);
	ShowCaret();
	SetTimer(1, 10, NULL);
	return 0;
}

void CMFCTestView::OnChar(UINT nChar, UINT nRepCnt, UINT nFlags) 
{
	// TODO: Add your message handler code here and/or call default
	
	CClientDC dc(this);
	CFont font;
	font.CreatePointFont(120, "华文行楷", NULL);
	CFont* pOldFont = dc.SelectObject(&font);

	TEXTMETRIC tm;
	dc.GetTextMetrics(&tm);
	
	if (0x0d == nChar) {
		// 换行
		m_strLine.Empty();
		m_ptTextPos.y += tm.tmHeight;
	}
	else if (0x08 == nChar) {
		COLORREF clr = dc.SetTextColor(dc.GetBkColor());
		dc.TextOut(m_ptTextPos.x, m_ptTextPos.y, m_strLine);
		m_strLine = m_strLine.Left(m_strLine.GetLength() - 1);
		dc.SetTextColor(clr);
	}
	else{
		m_strLine += nChar;
	}
	
	
	dc.TextOut(m_ptTextPos.x, m_ptTextPos.y, m_strLine);
	CSize sz = dc.GetTextExtent(m_strLine);
	CPoint pt;
	pt.x = m_ptTextPos.x + sz.cx;
	pt.y = m_ptTextPos.y;
	SetCaretPos(pt);

	dc.SelectObject(pOldFont);
	CView::OnChar(nChar, nRepCnt, nFlags);
}

void CMFCTestView::OnTimer(UINT nIDEvent) 
{
	// TODO: Add your message handler code here and/or call default
	m_nTimerTextWidth += 1;
	
	CClientDC dc(this);
	TEXTMETRIC tm;
	dc.GetTextMetrics(&tm);
	
	CRect rect;
	rect.left = 0;
	rect.top = 444;
	rect.right = m_nTimerTextWidth;
	rect.bottom = rect.top + tm.tmHeight;

	dc.SetTextColor(RGB(0, 255, 0));
	CString str;
	str.LoadString(IDS_STRING_TEXT);
	dc.DrawText(str, rect, DT_LEFT);
	

	rect.top = 555;
	rect.bottom = rect.top + tm.tmHeight;
	dc.DrawText(str, rect, DT_RIGHT);
	
	CSize sz = dc.GetTextExtent(str);
	if (m_nTimerTextWidth > sz.cx) {
		m_nTimerTextWidth = 0;
		dc.SetTextColor(RGB(0, 0, 0));
		dc.TextOut(0, 444, str);
	}
	CView::OnTimer(nIDEvent);
}


void CMFCTestView::OnContextMenu(CWnd*, CPoint point)
{
	CMenu menu;
	menu.LoadMenu(IDR_MENU1);

	CMenu* pPopup = menu.GetSubMenu(0);
	CWnd* pPopupOwner = this;
	
//	while (pPopupOwner->GetStyle() & WS_CHILD) {
//		pPopupOwner = pPopupOwner->GetParent();
//	}

	pPopup->TrackPopupMenu(TPM_LEFTALIGN|TPM_RIGHTBUTTON,  point.x, point.y, pPopupOwner);
}


void CMFCTestView::OnRButtonDown(UINT nFlags, CPoint point) 
{
	// TODO: Add your message handler code here and/or call default
	//OnContextMenu(NULL, point);
	
	CMenu menu;
	menu.LoadMenu(IDR_MENU1);

	CMenu* pPopup = menu.GetSubMenu(0);
	CWnd* pPopupOwner = this;
	ClientToScreen(&point);
	pPopup->TrackPopupMenu(TPM_LEFTALIGN|TPM_RIGHTBUTTON,  point.x, point.y, pPopupOwner);

	CView::OnRButtonDown(nFlags, point);
}
