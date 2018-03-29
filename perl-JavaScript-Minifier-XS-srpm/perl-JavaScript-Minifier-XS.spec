Name:           perl-JavaScript-Minifier-XS
Version:        0.11
Release:        9%{?dist}
Summary:        XS based JavaScript minifier
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/JavaScript-Minifier-XS/
Source0:        http://search.cpan.org/CPAN/authors/id/G/GT/GTERMARS/JavaScript-Minifier-XS-%{version}.tar.gz
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build) > 0.35
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
# Tests
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(JavaScript::Minifier)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
JavaScript::Minifier::XS is a JavaScript "minifier"; it's designed
to remove unnecessary white space and comments from JavaScript
files without breaking the JavaScript.

%prep
%setup -q -n JavaScript-Minifier-XS-%{version}

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test --test_files="xt/*.t"

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/JavaScript*
%{_mandir}/man3/*

%changelog
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-2
- Perl 5.22 rebuild

* Thu Jan 29 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-1
- 0.11 bump, update BRs
- Modernize spec file

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-12
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.09-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.09-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.09-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov  8 2010 Petr Sabata <psabata@redhat.com> - 0.09-1
- New upstream release, v0.09

* Wed Sep 29 2010 jkeating - 0.08-3
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Petr Pisar <ppisar@redhat.com> - 0.08-2
- Require perl(Test::Pod::Coverage) for tests

* Wed Sep 15 2010 Petr Pisar <ppisar@redhat.com> - 0.08-1
- 0.08 bump
- Correct description spelling

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.06-2
- rebuild against perl 5.10.1

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.06-1
- update filtering
- auto-update to 0.06 (by cpan-spec-update 0.01)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May  5 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.05-2
- add BR, remove useless provides

* Wed Apr 29 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.05-1
- Specfile autogenerated by cpanspec 1.78.
