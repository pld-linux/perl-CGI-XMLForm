%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	CGI-XMLForm perl module
Summary(pl):	Modu³ perla CGI-XMLForm
Name:		perl-CGI-XMLForm
Version:	0.07
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-XMLForm-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
CGI-XMLForm - Extension of CGI.pm which reads/generates formated XML.

%description -l pl
CGI-XMLForm - rozszerzenie CGI.pm umozliwiaj±ce czytanie/generowanie
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
%doc {Changes,README,TODO,example.html,example2.html}.gz

%{perl_sitelib}/CGI/XMLForm.pm
%{perl_sitelib}/CGI/XMLForm
%{perl_sitelib}/CGI/example.pl
%{perl_sitearch}/auto/CGI/XMLForm

%{_mandir}/man3/*
