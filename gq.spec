# TODO: "Schema" tab crashes
Summary:	Interactive graphical LDAP browser
Summary(pl):	Klient i przegl±darka LDAP
Summary(pt_BR):	Navegador gráfico para LDAP
Name:		gq
Version:	1.2.0
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/gqclient/%{name}-%{version}.tar.gz
# Source0-md5:	d3f974e5e1844ccfafbb6df77e7520c8
Source1:	http://dl.sourceforge.net/gqclient/%{name}-%{version}-langpack-1.tar.gz
# Source1-md5:	d2dfc43f6602e7c3f8178d63fb038cae
Source2:	%{name}.desktop
Source3:	%{name}.png
Patch0:		%{name}-iconv-in-libc.patch
URL:		http://biot.com/gq/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cyrus-sasl-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GQ is GTK+ LDAP client and browser utility. It can be used for
searching LDAP directory as well as browsing it using tree view. It
has limited modify/add functionality, too.

%description -l pl
GQ jest napisanym przy u¿yciu GTK+ klientem oraz przegl±dark± LDAP.
Mo¿na go u¿yæ do przeszukiwania katalogu LDAP oraz przegl±dania go w
formie drzewa. Posiada równie¿ (w ograniczonym stopniu) mo¿liwo¶æ
dodawania i modyfikacji danych.

%description -l pt_BR
GQ é um client LDAP feito em GTK+. Ele pode ser usado para pesquisar
diretórios LDAP e também para visualizar um diretório em forma de
árvore. Também existem recursos de edição e inserção de registros,
embora um pouco limitados.

%prep
%setup -q -a1
cp %{name}-%{version}-langpack-1/po/* po/
%patch0 -p1

%build
ALL_LINGUAS=`cat po/LINGUAS`
%configure --enable-browser-dnd \
	--disable-update-mimedb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/gq.desktop
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gq
%{_datadir}/mime/packages/gq-ldif.xml
%{_pixmapsdir}/gq
%{_pixmapsdir}/gq.png
%{_desktopdir}/*.desktop
