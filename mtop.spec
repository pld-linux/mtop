%include	/usr/lib/rpm/macros.perl
Summary:	mtop/mkill - MySQL Monitoring Tools
Summary(pl.UTF-8):	mtop/mkill - narzędzia do monitorowania MySQL
Name:		mtop
Version:	0.6.6
Release:	0.1
License:	GPL
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/mtop/%{name}-%{version}.tar.gz
# Source0-md5:	f1beb021351f937a74cb0e9d3fcedae7
URL:		http://mtop.sourceforge.net/
BuildRequires:	perl-DBD-mysql
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Curses
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mtop (MySQL top) monitors a MySQL server showing the queries which are
taking the most amount of time to complete. Features include 'zooming'
in on a process to show the complete query, 'explaining' the query
optimizer information for a query and 'killing' queries. In addition,
server performance statistics, configuration information, and tuning
tips are provided.

mkill (MySQL kill) monitors a MySQL server for long
running queries and kills them after a specified time interval.
Queries can be selected based on regexes on the user, host, command,
database, state and query.

%description -l pl.UTF-8
mtop (MySQL top) monitoruje serwer MySQL pokazując zapytania, których
wykonanie zajmuje najwięcej czasu. Możliwości obejmują "powiększanie"
procesów, aby pokazać pełne zapytania, objaśnianie (explain)
informacji o optymalizacji zapytania oraz "zabijanie" zapytań. Ponadto
dostępne są statystyki wydajności, informacje o konfiguracji oraz
wskazówki dotyczące strojenia.

mkill (MySQL kill) monitoruje serwer MySQL pod kątem długo trwających
zapytań i zabija je po określonym czasie. Zapytania mogą być wybierane
na podstawie wyrażeń regularnych dla użytkownika, hosta, komendy, bazy
danych, stanu i samego zapytania.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	--prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/m*
%{_mandir}/man1/*
