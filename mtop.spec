Summary:	mtop/mkill - MySQL Monitoring Tools
Name:		mtop
Version:	0.6.4
Release:	0.1
License:	GPL
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/mtop/%{name}-%{version}.tar.gz
# Source0-md5:	3a7b400982e9dba8243a1424b9fdd244
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
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

%prep
%setup -q

%build
%{__perl} Makefile.PL --prefix=%{_prefix}
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
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/m*
