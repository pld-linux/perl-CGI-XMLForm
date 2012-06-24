#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	XMLForm
Summary:	CGI::XMLForm Perl module
Summary(cs):	Modul CGI::XMLForm pro Perl
Summary(da):	Perlmodul CGI::XMLForm
Summary(de):	CGI::XMLForm Perl Modul
Summary(es):	M�dulo de Perl CGI::XMLForm
Summary(fr):	Module Perl CGI::XMLForm
Summary(it):	Modulo di Perl CGI::XMLForm
Summary(ja):	CGI::XMLForm Perl �⥸�塼��
Summary(ko):	CGI::XMLForm �� ����
Summary(nb):	Perlmodul CGI::XMLForm
Summary(pl):	Modu� Perla CGI::XMLForm
Summary(pt):	M�dulo de Perl CGI::XMLForm
Summary(pt_BR):	M�dulo Perl CGI::XMLForm
Summary(ru):	������ ��� Perl CGI::XMLForm
Summary(sv):	CGI::XMLForm Perlmodul
Summary(uk):	������ ��� Perl CGI::XMLForm
Summary(zh_CN):	CGI::XMLForm Perl ģ��
Name:		perl-CGI-XMLForm
Version:	0.10
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	89d5fcc3f0a3753aa184e9ae85474736
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-XML-Parser >= 2.20
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::XMLForm - Extension of CGI.pm which reads/generates formated XML.

%description -l pl
CGI::XMLForm - rozszerzenie CGI.pm umo�liwiaj�ce czytanie/generowanie
dokument�w w formacie XML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install example* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/CGI/XMLForm.pm
%{perl_vendorlib}/CGI/XMLForm
%dir %{perl_vendorlib}/auto/CGI
%dir %{perl_vendorlib}/auto/CGI/XMLForm
%dir %{perl_vendorlib}/auto/CGI/XMLForm/Path
%{perl_vendorlib}/auto/CGI/XMLForm/Path/autosplit.ix
%{perl_vendorlib}/auto/CGI/XMLForm/Path/*.al
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/*.html
