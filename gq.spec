Summary:	Interactive graphical LDAP browser
Name:		gq
Version:	0.2.2
Release:	1
Copyright:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Packager:	Borek Lupomesky <Borek.Lupomesky@ujep.cz>
Source:		http://biot.com/gq/download/gq-%{version}.tar.gz
Source1:	gq.desktop
URL:		http://biot.com/gq/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	openldap-devel
BuildRequires:	XFree86-devel
BuildRoot:	/tmp/gq-%{version}-%{release}

%define		_prefix		/usr/X11R6

%description
GQ is GTK+ LDAP client and browser utility. It can be used
for searching LDAP directory as well as browsing it using
tree view. It has limited modify/add functionality, too.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/applnk/Networking

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applnk/Networking/gq.desktop

gzip -9nf {README,ChangeLog,NEWS,TODO,AUTHORS}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_prefix}/bin/*
%{_datadir}/applnk/Networking/gq.desktop
