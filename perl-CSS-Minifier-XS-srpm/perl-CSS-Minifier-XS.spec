Name:       perl-CSS-Minifier-XS
Version:    0.09
#Release:    6%{?dist}
Release:    0.6%{?dist}
# lib/CSS/Minifier/XS.pm -> GPL+ or Artistic
License:    GPL+ or Artistic
Group:      Development/Libraries
Summary:    XS based CSS minifier
Source:     http://search.cpan.org/CPAN/authors/id/G/GT/GTERMARS/CSS-Minifier-XS-%{version}.tar.gz
Url:        http://search.cpan.org/dist/CSS-Minifier-XS
Requires:   perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires: perl(CSS::Minifier)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)

%{?perl_default_filter}

%description
'CSS::Minifier::XS' is a CSS "minifier". It's designed to remove
unnecessary white-space and comments from CSS files, while also
*not* breaking the CSS. 'CSS::Minifier::XS' is similar in function
to 'CSS::Minifier', but is substantially faster as it's written
in XS and not just pure Perl.


%prep
%setup -q -n CSS-Minifier-XS-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
%{_mandir}/man3/*.3*

%changelog
* Sat Mar 19 2016 Nico Kadel-Garcia <nkadel@gmail.com> - 0.09-0.6
- Backport to RHEL 7

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-5
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 03 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.09-1
- Update to 0.09
- Modify description to fix rpmlint warnings

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.08-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.08-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 02 2011 Iain Arnell <iarnell@gmail.com> 0.08-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.07-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Aug 08 2010 Iain Arnell <iarnell@gmail.com> 0.07-1
- update to latest upstream version
- use perl_default_filter and DESTDIR

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-3
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.04-2
- rebuild against perl 5.10.1

* Tue Aug 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.04-1
- auto-update to 0.04 (by cpan-spec-update 0.01)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 10 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.03-1
- update for submission

* Fri Apr 10 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.03-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
