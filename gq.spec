Summary:	Interactive graphical LDAP browser
Summary(pl):	Klientem i przegl±darka LDAP
Summary(pt_BR):	Navegador gráfico para LDAP
Name:		gq
Version:	0.6.0beta2
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://biot.com/gq/download/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-init.patch
Patch1:		%{name}-passwd_visibility.patch
URL:		http://biot.com/gq/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libtool
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

%description -l pt_BR
GQ é um client LDAP feito em GTK+. Ele pode ser usado para pesquisar
diretórios LDAP e também para visualizar um diretório em forma de
árvore. Também existem recursos de edição e inserção de registros,
embora um pouco limitados.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Misc,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc/gq.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README* ChangeLog NEWS TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Misc/gq.desktop
%{_pixmapsdir}/*
