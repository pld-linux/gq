# $Revision: 1.1 $
Name:		gq
Summary:	Interactive graphical LDAP browser
Version:	0.2.2
Release:	1
Copyright:	GPL
Group:		Networking/Utilities
URL:		http://biot.com/gq/
Packager:	Borek Lupomesky <Borek.Lupomesky@ujep.cz>
Source:		http://biot.com/gq/download/gq-%{version}.tar.gz
Source1:	gq.desktop
BuildRoot:	/tmp/gq-%{version}-%{release}
Requires:	gtk+ >= 1.2.0

%define	_prefix		/usr/X11R6

%description
GQ is GTK+ LDAP client and browser utility. It can be used
for searching LDAP directory as well as browsing it using
tree view. It has limited modify/add functionality, too.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
make prefix=$RPM_BUILD_ROOT/%{_prefix} install-strip

gzip -9nf {README,INSTALL,COPYING,ChangeLog,NEWS,TODO,AUTHORS}

install -d $RPM_BUILD_ROOT%{_datadir}/applnk/Networking
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applnk/Networking/gq.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,INSTALL,COPYING,ChangeLog,NEWS,TODO,AUTHORS}.gz
%attr(755,root,root) %{_prefix}/bin/*
%{_datadir}/applnk/Networking/gq.desktop
