Summary:	Interactive graphical LDAP browser
Summary(pl.UTF-8):   Klientem i przeglądarka LDAP
Summary(pt_BR.UTF-8):   Navegador gráfico para LDAP
Name:		gq
Version:	1.0beta1
Release:	1
Epoch:		0
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/sourceforge/%{name}client/%{name}-%{version}.tar.gz
# Source0-md5:	c904ff52f513a58516d9543f8dc3fe5b
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-mkinstalldirs.patch
URL:		http://biot.com/gq/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	openldap-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GQ is GTK+ LDAP client and browser utility. It can be used for
searching LDAP directory as well as browsing it using tree view. It
has limited modify/add functionality, too.

%description -l pl.UTF-8
GQ jest napisanym przy użyciu GTK+ klientem oraz przeglądarką LDAP.
Można go uzyć do przeszukiwania katalogu LDAP oraz przeglądania go w
formie drzewa. Posiada również (w ograniczonym stopniu) możliwość
dodawania i modyfikacji danych.

%description -l pt_BR.UTF-8
GQ é um client LDAP feito em GTK+. Ele pode ser usado para pesquisar
diretórios LDAP e também para visualizar um diretório em forma de
árvore. Também existem recursos de edição e inserção de registros,
embora um pouco limitados.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-browser-dnd \
	--disable-rpath \
	--enable-cache
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/gq.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* RELNOTES TODO 
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*
