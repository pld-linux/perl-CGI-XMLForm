#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	XMLForm
Summary:	CGI::XMLForm Perl module
Summary(cs.UTF-8):	Modul CGI::XMLForm pro Perl
Summary(da.UTF-8):	Perlmodul CGI::XMLForm
Summary(de.UTF-8):	CGI::XMLForm Perl Modul
Summary(es.UTF-8):	Módulo de Perl CGI::XMLForm
Summary(fr.UTF-8):	Module Perl CGI::XMLForm
Summary(it.UTF-8):	Modulo di Perl CGI::XMLForm
Summary(ja.UTF-8):	CGI::XMLForm Perl モジュール
Summary(ko.UTF-8):	CGI::XMLForm 펄 모줄
Summary(nb.UTF-8):	Perlmodul CGI::XMLForm
Summary(pl.UTF-8):	Moduł Perla CGI::XMLForm
Summary(pt.UTF-8):	Módulo de Perl CGI::XMLForm
Summary(pt_BR.UTF-8):	Módulo Perl CGI::XMLForm
Summary(ru.UTF-8):	Модуль для Perl CGI::XMLForm
Summary(sv.UTF-8):	CGI::XMLForm Perlmodul
Summary(uk.UTF-8):	Модуль для Perl CGI::XMLForm
Summary(zh_CN.UTF-8):	CGI::XMLForm Perl 模块
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

%description -l pl.UTF-8
CGI::XMLForm - rozszerzenie CGI.pm umożliwiające czytanie/generowanie
dokumentów w formacie XML.

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
