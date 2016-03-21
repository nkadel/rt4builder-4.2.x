Name:           perl-Scope-Upper
Summary:        Act on upper scopes
Version:        0.27
#Release:        3%{?dist}
Release:        0.3%{?dist}
License:        GPL+ or Artistic
Source0:        http://search.cpan.org/CPAN/authors/id/V/VP/VPIT/Scope-Upper-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/Scope-Upper
# Build
BuildRequires:  perl
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX)
# It's either Scalar::Util or B; with the former being preferred
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
# Optional tests only
BuildRequires:  perl(Time::HiRes)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Exporter)
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
This module lets you defer actions that will take place when the control
flow returns into an upper scope. Currently, you can hook an upper scope
end, or localize variables, array/hash values or deletions of elements
in higher contexts. You can also return to an upper level and know which
context was in use then.

%prep
%setup -q -n Scope-Upper-%{version}
sed -i '1s,^#!.*perl,#!%{__perl},' samples/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} +
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README Changes samples
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
%{_mandir}/man3/*.3*

%changelog
* Sat Mar 19 2016 Nico Kadel-Garcia <nkadel@gmail.com> - 0.27-0.3
- Backport to RHEL 7

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-2
- Perl 5.22 rebuild

* Tue Mar 31 2015 Petr Šabata <contyk@redhat.com> - 0.27-1
- 0.27 bugfix bump

* Fri Mar 20 2015 Petr Šabata <contyk@redhat.com> - 0.26-1
- 0.26 bump

* Tue Nov 25 2014 Petr Pisar <ppisar@redhat.com> - 0.25-1
- 0.25 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 05 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-1
- 0.24 bump, update BRs

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Pisar <ppisar@redhat.com> - 0.22-2
- Perl 5.18 rebuild

* Fri Feb 15 2013 Iain Arnell <iarnell@gmail.com> 0.22-1
- udpate to latest upstream version
- drop old tests sub-package obsoletes/provides

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 21 2012 Iain Arnell <iarnell@gmail.com> 0.21-1
- update to latest upstream version

* Fri Sep 07 2012 Iain Arnell <iarnell@gmail.com> 0.19-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 0.18-2
- Perl 5.16 rebuild

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.18-1
- update to latest upstream version
- drop tests subpackage; move tests to main package documentation

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 02 2011 Iain Arnell <iarnell@gmail.com> 0.16-1
- update to latest upstream version

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.14-2
- Perl mass rebuild

* Thu May 12 2011 Iain Arnell <iarnell@gmail.com> 0.14-1
- update to latest upstream version

* Thu Feb 24 2011 Iain Arnell <iarnell@gmail.com> 0.13-1
- update to latest upstream version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.12-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sat Dec 18 2010 Iain Arnell <iarnell@gmail.com> 0.12-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- additional BRs for better test coverage

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.10-2
- Mass rebuild with perl-5.12.0

* Mon Mar 08 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.10-1
- update by Fedora::App::MaintainerTools 0.004
- PERL_INSTALL_ROOT => DESTDIR
- updating to latest GA CPAN version (0.10)
- added a new br on perl(base) (version 0)
- dropped old BR on perl(Test::Pod::Coverage)
- added a new req on perl(Exporter) (version 0)
- added a new req on perl(XSLoader) (version 0)
- added a new req on perl(base) (version 0)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.09-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 09 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.09-1
- auto-update to 0.09 (by cpan-spec-update 0.01)

* Sun May 17 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08-1
- auto-update to 0.08 (by cpan-spec-update 0.01)
- filter private Perl so provides

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.07-1
- update to 0.07

* Tue Feb 10 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.06-1
- brush-up for review submission

* Tue Feb 10 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.06-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
