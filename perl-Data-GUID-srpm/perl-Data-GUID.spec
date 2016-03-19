Name:           perl-Data-GUID
Version:        0.048
Release:        5%{?dist}
Summary:        Globally unique identifiers
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-GUID/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Data-GUID-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::UUID) >= 1.148
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Sub::Exporter) >= 0.90
BuildRequires:  perl(Sub::Install) >= 0.03
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Data::GUID provides a simple interface for generating and using globally
unique identifiers.

%prep
%setup -q -n Data-GUID-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.048-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.048-4
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.048-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.048-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 19 2013 Ralf Corsépius <corsepiu@fedoraproject.org> 0.048-1
- Initial Fedora package.
