; CLW file contains information for the MFC ClassWizard

[General Info]
Version=1
LastClass=CDlgTestDlg
LastTemplate=CPropertySheet
NewFileInclude1=#include "stdafx.h"
NewFileInclude2=#include "DlgTest.h"

ClassCount=6
Class1=CDlgTestApp
Class2=CDlgTestDlg
Class3=CAboutDlg

ResourceCount=5
Resource1=IDD_PROPPAGE_LARGE (中立国)
Resource2=IDR_MAINFRAME
Class4=CNewButton
Resource3=IDD_ABOUTBOX
Class5=CProp1
Class6=CPropSheet
Resource4=IDD_DLGTEST_DIALOG
Resource5=IDD_PROPPAGE_LARGE1 (English (U.S.))

[CLS:CDlgTestApp]
Type=0
HeaderFile=DlgTest.h
ImplementationFile=DlgTest.cpp
Filter=N
LastObject=CDlgTestApp

[CLS:CDlgTestDlg]
Type=0
HeaderFile=DlgTestDlg.h
ImplementationFile=DlgTestDlg.cpp
Filter=D
LastObject=CDlgTestDlg
BaseClass=CDialog
VirtualFilter=dWC

[CLS:CAboutDlg]
Type=0
HeaderFile=DlgTestDlg.h
ImplementationFile=DlgTestDlg.cpp
Filter=D

[DLG:IDD_ABOUTBOX]
Type=1
Class=CAboutDlg
ControlCount=4
Control1=IDC_STATIC,static,1342177283
Control2=IDC_STATIC,static,1342308480
Control3=IDC_STATIC,static,1342308352
Control4=IDOK,button,1342373889

[DLG:IDD_DLGTEST_DIALOG]
Type=1
Class=CDlgTestDlg
ControlCount=4
Control1=IDC_BUTTON1,button,1342242817
Control2=IDC_BUTTON2,button,1342242816
Control3=IDC_STATIC,static,1342308352
Control4=IDC_BUTTON3,button,1342242816

[CLS:CNewButton]
Type=0
HeaderFile=NewButton.h
ImplementationFile=NewButton.cpp
BaseClass=CButton
Filter=W
LastObject=CNewButton
VirtualFilter=BWC

[CLS:CProp1]
Type=0
HeaderFile=Prop1.h
ImplementationFile=Prop1.cpp
BaseClass=CPropertyPage
Filter=D
VirtualFilter=idWC
LastObject=CProp1

[CLS:CPropSheet]
Type=0
HeaderFile=PropSheet.h
ImplementationFile=PropSheet.cpp
BaseClass=CPropertySheet
Filter=W
LastObject=CPropSheet

[DLG:IDD_PROPPAGE_LARGE1 (English (U.S.))]
Type=1
Class=?
ControlCount=1
Control1=IDC_STATIC,static,1342308352

[DLG:IDD_PROPPAGE_LARGE (中立国)]
Type=1
Class=CProp1
ControlCount=3
Control1=IDC_STATIC,static,1342308352
Control2=IDC_RADIO1,button,1342308361
Control3=IDC_RADIO2,button,1342308361

