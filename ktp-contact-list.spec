Summary:	KDE Telepathy contact list handler
Name:		ktp-contact-list
Version:	23.04.3
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5ScriptTools)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5WebKit)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(TelepathyQt5)
BuildRequires:	cmake(KTp)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5WebKit)
BuildRequires:	cmake(Qca-qt5)
BuildRequires:	cmake(AccountsQt5)
BuildRequires:	cmake(SignOnQt5)
BuildRequires:	cmake(KAccounts)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5People)
BuildRequires:	cmake(TelepathyLoggerQt)
BuildRequires:	pkgconfig(shared-mime-info)

%description
KDE Telepathy contact list handler

%files -f ktp-contactlist.lang
%{_bindir}/ktp-contactlist
%{_datadir}/applications/org.kde.ktpcontactlist.desktop
%{_datadir}/dbus-1/services/org.kde.ktpcontactlist.service

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang ktp-contactlist
