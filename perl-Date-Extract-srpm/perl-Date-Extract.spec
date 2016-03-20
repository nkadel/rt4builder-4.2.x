Name:           perl-Date-Extract
Version:        0.05
#Release:        4%{?dist}
Release:        0.4%{?dist}
Summary:        Date::Extract Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Date-Extract/
Source0:        http://www.cpan.org/authors/id/S/SH/SHARYANTO/Date-Extract-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(DateTime::Format::Natural) >= 0.60
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::More)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Search a string for something that looks like a date string, and build a
DateTime object out of it.

%prep
%setup -q -n Date-Extract-%{version}

%build
# --skipdeps causes ExtUtils::AutoInstall not to try auto-installing
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Mar 19 2016 Nico Kadel-Garcia <nkadel@gmail.com> - 0.05-0.4
- Backport to RHEL 7

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-3
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-2
- Perl 5.20 rebuild

* Mon Jun 23 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.05-1
- Upstream update.
- Spec file cosmetics.
- Reflect Source0:-URL having changed.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 19 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.04-1
- Initial Fedora package.
