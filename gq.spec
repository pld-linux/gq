Summary:	Interactive graphical LDAP browser
Summary(pl):	Klientem i przegl±darka LDAP
Name:		gq
Version:	0.4.0
Release:	3
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	http://biot.com/gq/download/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-init.patch
URL:		http://biot.com/gq/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	openldap-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GQ is GTK+ LDAP client and browser utility. It can be used for
searching LDAP directory as well as browsing it using tree view. It
has limited modify/add functionality, too.

%description -l pl
GQ jest napisanym przy u¿yciu GTK+ klientem oraz przegl±dark± LDAP.
Mo¿na go uzyæ do przeszukiwania katalogu LDAP oraz przegl±dania go w
formie drzewa. Posiada równie¿ (w ograniczonym stopniu) mo¿liwo¶æ
dodawania i modyfikacji danych.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Misc,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc/gq.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README ChangeLog NEWS TODO AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Misc/gq.desktop
%{_pixmapsdir}/*
