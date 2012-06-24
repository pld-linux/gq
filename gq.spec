Summary:	Interactive graphical LDAP browser
Name:		gq
Version:	0.2.3
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narz�dzia
Source0:	http://download.sourceforge.net/gqclient/%{name}-%{version}.tar.gz
Source1:	gq.desktop
URL:		http://biot.com/gq/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	openldap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GQ is GTK+ LDAP client and browser utility. It can be used for
searching LDAP directory as well as browsing it using tree view. It
has limited modify/add functionality, too.

%description -l pl
GQ jest napisanym przy u�yciu GTK+ klientem oraz przegl�dark� LDAP.
Mo�na go uzy� do przeszukiwania katalogu LDAP oraz przegl�dania go w
formie drzewa. Posiada r�wnie� (w ograniczonym stopniu) mo�liwo��
dodawania i modyfikacji danych.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Networking

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Networking/gq.desktop

gzip -9nf {README,ChangeLog,NEWS,TODO,AUTHORS}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Networking/gq.desktop
