# TODO: "Schema" tab crashes
Summary:	Interactive graphical LDAP browser
Summary(pl):	Klient i przegl±darka LDAP
Summary(pt_BR):	Navegador gráfico para LDAP
Name:		gq
Version:	1.0
%define	bver	beta1
Release:	0.%{bver}.2
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/gqclient/%{name}-%{version}%{bver}.tar.gz
# Source0-md5:	c904ff52f513a58516d9543f8dc3fe5b
Source1:	http://dl.sourceforge.net/gqclient/%{name}-%{version}%{bver}-langpack-1.tar.gz
# Source1-md5:	4194453e76aed15994c5c4e5c3aee6d5
Source2:	%{name}.desktop
Source3:	%{name}.png
Patch0:		%{name}-iconv-in-libc.patch
Patch1:		%{name}-po.patch
URL:		http://biot.com/gq/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cyrus-sasl-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	openldap-devel >= 2.0.0
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q -n %{name}-%{version}%{bver} -a1
mv -f %{name}-%{version}%{bver}-langpack-*/po/*.po po
%patch0 -p1
%patch1 -p1

%{__perl} -pi -e 's/(ALL_LINGUAS=)/$1"cs de ja zh_CN"/' configure.in

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
%doc AUTHORS ChangeLog NEWS README README.TLS TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/gq
%{_pixmapsdir}/gq.png
%{_desktopdir}/*.desktop
