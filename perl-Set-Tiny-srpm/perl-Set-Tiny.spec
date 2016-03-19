Name:           perl-Set-Tiny
Version:        0.03
#Release:        1%{?dist}
Release:        0.1%{?dist}
Summary:        Simple sets of strings
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Set-Tiny/
Source0:        http://www.cpan.org/authors/id/T/TR/TRENDELS/Set-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Set::Tiny is a thin wrapper around regular Perl hashes to perform often
needed set operations, such as testing two sets of strings for equality, or
checking whether one is contained within the other.

%prep
%setup -q -n Set-Tiny-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Mar 19 2016 Nico Kadel-Garcia <nkdel@gmail.com> - 0.03-0.1
- Backport to RHEL 7

* Sun Aug 30 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.03-1
- Upstream update.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-2
- Perl 5.22 rebuild

* Mon Sep 29 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.02-1
- Upstream update.

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.01-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Ralf Corsépius <corsepiu@fedoraproject.org> 0.01-1
- Initial package.
