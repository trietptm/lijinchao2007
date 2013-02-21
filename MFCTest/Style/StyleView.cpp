// StyleView.cpp : implementation of the CStyleView class
//

#include "stdafx.h"
#include "Style.h"

#include "StyleDoc.h"
#include "StyleView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CStyleView

IMPLEMENT_DYNCREATE(CStyleView, CView)

BEGIN_MESSAGE_MAP(CStyleView, CView)
	//{{AFX_MSG_MAP(CStyleView)
		// NOTE - the ClassWizard will add and remove mapping macros here.
		//    DO NOT EDIT what you see in these blocks of generated code!
	//}}AFX_MSG_MAP
	// Standard printing commands
	ON_COMMAND(ID_FILE_PRINT, CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_DIRECT, CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_PREVIEW, CView::OnFilePrintPreview)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CStyleView construction/destruction

CStyleView::CStyleView()
{
	// TODO: add construction code here

}

CStyleView::~CStyleView()
{
}

BOOL CStyleView::PreCreateWindow(CREATESTRUCT& cs)
{
	// TODO: Modify the Window class or styles here by modifying
	//  the CREATESTRUCT cs

	return CView::PreCreateWindow(cs);
}

/////////////////////////////////////////////////////////////////////////////
// CStyleView drawing

void CStyleView::OnDraw(CDC* pDC)
{
	CStyleDoc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	// TODO: add draw code for native data here
}

/////////////////////////////////////////////////////////////////////////////
// CStyleView printing

BOOL CStyleView::OnPreparePrinting(CPrintInfo* pInfo)
{
	// default preparation
	return DoPreparePrinting(pInfo);
}

void CStyleView::OnBeginPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: add extra initialization before printing
}

void CStyleView::OnEndPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: add cleanup after printing
}

/////////////////////////////////////////////////////////////////////////////
// CStyleView diagnostics

#ifdef _DEBUG
void CStyleView::AssertValid() const
{
	CView::AssertValid();
}

void CStyleView::Dump(CDumpContext& dc) const
{
	CView::Dump(dc);
}

CStyleDoc* CStyleView::GetDocument() // non-debug version is inline
{
	ASSERT(m_pDocument->IsKindOf(RUNTIME_CLASS(CStyleDoc)));
	return (CStyleDoc*)m_pDocument;
}
#endif //_DEBUG

/////////////////////////////////////////////////////////////////////////////
// CStyleView message handlers
