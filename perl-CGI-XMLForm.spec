%include	/usr/lib/rpm/macros.perl
Summary:	CGI-XMLForm perl module
Summary(pl):	Modu³ perla CGI-XMLForm
Name:		perl-CGI-XMLForm
Version:	0.10
Release:	1
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-XMLForm-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-XML-Parser >= 2.20
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
CGI-XMLForm - Extension of CGI.pm which reads/generates formated XML.

%description -l pl
CGI-XMLForm - rozszerzenie CGI.pm umo¿liwiaj±ce czytanie/generowanie
dokumentów w formacie XML.

%prep
%setup -q -n CGI-XMLForm-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/CGI/XMLForm
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README TODO *html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,TODO,example.html,example2.html}.gz example.pl

%{perl_sitelib}/CGI/XMLForm.pm
%{perl_sitelib}/CGI/XMLForm
%{perl_sitearch}/auto/CGI/XMLForm

%{_mandir}/man3/*
