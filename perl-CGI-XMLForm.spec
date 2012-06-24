%include	/usr/lib/rpm/macros.perl
Summary:	CGI-XMLForm perl module
Summary(pl):	Modu� perla CGI-XMLForm
Name:		perl-CGI-XMLForm
Version:	0.10
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-XMLForm-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-XML-Parser >= 2.20
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-XMLForm - Extension of CGI.pm which reads/generates formated XML.

%description -l pl
CGI-XMLForm - rozszerzenie CGI.pm umo�liwiaj�ce czytanie/generowanie
dokument�w w formacie XML.

%prep
%setup -q -n CGI-XMLForm-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz *.html example.pl
%{perl_sitelib}/CGI/XMLForm.pm
%{perl_sitelib}/CGI/XMLForm
%{_mandir}/man3/*
