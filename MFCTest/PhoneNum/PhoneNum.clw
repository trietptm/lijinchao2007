; CLW file contains information for the MFC ClassWizard

[General Info]
Version=1
LastClass=CTestDlg
LastTemplate=CDialog
NewFileInclude1=#include "stdafx.h"
NewFileInclude2=#include "PhoneNum.h"
LastPage=0

ClassCount=6
Class1=CPhoneNumApp
Class2=CPhoneNumDoc
Class3=CPhoneNumView
Class4=CMainFrame

ResourceCount=3
Resource1=IDD_ABOUTBOX
Class5=CAboutDlg
Resource2=IDR_MAINFRAME
Class6=CTestDlg
Resource3=IDD_DIALOG1

[CLS:CPhoneNumApp]
Type=0
HeaderFile=PhoneNum.h
ImplementationFile=PhoneNum.cpp
Filter=N

[CLS:CPhoneNumDoc]
Type=0
HeaderFile=PhoneNumDoc.h
ImplementationFile=PhoneNumDoc.cpp
Filter=N

[CLS:CPhoneNumView]
Type=0
HeaderFile=PhoneNumView.h
ImplementationFile=PhoneNumView.cpp
Filter=C
BaseClass=CView
VirtualFilter=VWC
LastObject=IDM_DLG1


[CLS:CMainFrame]
Type=0
HeaderFile=MainFrm.h
ImplementationFile=MainFrm.cpp
Filter=T
BaseClass=CFrameWnd
VirtualFilter=fWC
LastObject=CMainFrame




[CLS:CAboutDlg]
Type=0
HeaderFile=PhoneNum.cpp
ImplementationFile=PhoneNum.cpp
Filter=D
LastObject=CAboutDlg

[DLG:IDD_ABOUTBOX]
Type=1
Class=CAboutDlg
ControlCount=4
Control1=IDC_STATIC,static,1342177283
Control2=IDC_STATIC,static,1342308480
Control3=IDC_STATIC,static,1342308352
Control4=IDOK,button,1342373889

[MNU:IDR_MAINFRAME]
Type=1
Class=CMainFrame
Command1=ID_FILE_NEW
Command2=ID_FILE_OPEN
Command3=ID_FILE_SAVE
Command4=ID_FILE_SAVE_AS
Command5=ID_FILE_PRINT
Command6=ID_FILE_PRINT_PREVIEW
Command7=ID_FILE_PRINT_SETUP
Command8=ID_FILE_MRU_FILE1
Command9=ID_APP_EXIT
Command10=ID_EDIT_UNDO
Command11=ID_EDIT_CUT
Command12=ID_EDIT_COPY
Command13=ID_EDIT_PASTE
Command14=ID_VIEW_TOOLBAR
Command15=ID_VIEW_STATUS_BAR
Command16=ID_APP_ABOUT
Command17=IDM_DLG1
CommandCount=17

[ACL:IDR_MAINFRAME]
Type=1
Class=CMainFrame
Command1=ID_FILE_NEW
Command2=ID_FILE_OPEN
Command3=ID_FILE_SAVE
Command4=ID_FILE_PRINT
Command5=ID_EDIT_UNDO
Command6=ID_EDIT_CUT
Command7=ID_EDIT_COPY
Command8=ID_EDIT_PASTE
Command9=ID_EDIT_UNDO
Command10=ID_EDIT_CUT
Command11=ID_EDIT_COPY
Command12=ID_EDIT_PASTE
Command13=ID_NEXT_PANE
Command14=ID_PREV_PANE
CommandCount=14

[TB:IDR_MAINFRAME]
Type=1
Class=?
Command1=ID_FILE_NEW
Command2=ID_FILE_OPEN
Command3=ID_FILE_SAVE
Command4=ID_EDIT_CUT
Command5=ID_EDIT_COPY
Command6=ID_EDIT_PASTE
Command7=ID_FILE_PRINT
Command8=ID_APP_ABOUT
CommandCount=8

[DLG:IDD_DIALOG1]
Type=1
Class=CTestDlg
ControlCount=6
Control1=IDC_EDIT1,edit,1350631556
Control2=IDC_BUTTON1,button,1342242816
Control3=IDC_BUTTON2,button,1342242816
Control4=IDC_EDIT2,edit,1350631556
Control5=IDC_EDIT3,edit,1350631556
Control6=IDC_SEPERATOR,static,1342181383

[CLS:CTestDlg]
Type=0
HeaderFile=TestDlg.h
ImplementationFile=TestDlg.cpp
BaseClass=CDialog
Filter=D
LastObject=CTestDlg
VirtualFilter=dWC

