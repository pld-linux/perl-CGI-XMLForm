%include	/usr/lib/rpm/macros.perl
Summary:	CGI-XMLForm perl module
Summary(pl):	Modu³ perla CGI-XMLForm
Name:		perl-CGI-XMLForm
Version:	0.10
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-XMLForm-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-XML-Parser >= 2.20
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-XMLForm - Extension of CGI.pm which reads/generates formated XML.

%description -l pl
CGI-XMLForm - rozszerzenie CGI.pm umo¿liwiaj±ce czytanie/generowanie
dokumentów w formacie XML.

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
