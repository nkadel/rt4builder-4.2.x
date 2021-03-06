#
# --with oracle 
#	Build perl-DBIx-SearchBuilder-Oracle subpackage. 
#	Disabled by default, because it depends on packages outside of Fedora
#	at run-time
#

Name:		perl-DBIx-SearchBuilder
Version:	1.66
#Release:	4%{?dist}
Release:	0.4%{?dist}
Summary:	Encapsulate SQL queries and rows in simple perl objects
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/DBIx-SearchBuilder/
Source0:	http://www.cpan.org/authors/id/A/AL/ALEXMV/DBIx-SearchBuilder-%{version}.tar.gz

Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:	noarch

BuildRequires:	perl(Cache::Simple::TimedExpiry) >= 0.21
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Class::ReturnValue) >= 0.4
# Urgh ...
BuildRequires:	perl(CPAN)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBI)
BuildRequires:	perl(Encode)
BuildRequires:	perl(ExtUtils::AutoInstall) >= 0.49
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:	perl(Test::More) >= 0.52
BuildRequires:	perl(Want)

# Improved tests:
BuildRequires:	perl(Test::Pod)

# Optional features
BuildRequires:	perl(capitalization) >= 0.03
BuildRequires:	perl(Clone)
BuildRequires:	perl(DBIx::DBSchema)


%description
This module provides an object-oriented mechanism for retrieving and
updating data in a DBI-accessible database.

%prep
%setup -q -n DBIx-SearchBuilder-%{version}

# Perms in tarball are broken 
find -type f -exec chmod -x {} \;

%build
# --skipdeps causes ExtUtils::AutoInstall not to try auto-installing 
# missing optional features
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps

make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%doc README ROADMAP
%{perl_vendorlib}/DBIx
%{_mandir}/man3/*
%exclude %{perl_vendorlib}/DBIx/SearchBuilder/Handle/Oracle*
%exclude %{_mandir}/man3/DBIx::SearchBuilder::Handle::Oracle*


%if "%{?_with_oracle}"
%package Oracle
Summary:	DBIx::SearchBuilder bindings for Oracle
Group:		Development/Libraries
Requires:	%name = %{version}-%{release}

%description Oracle
DBIx::SearchBuilder bindings for Oracle

%files Oracle
%{perl_vendorlib}/DBIx/SearchBuilder/Handle/Oracle*
%{_mandir}/man3/DBIx::SearchBuilder::Handle::Oracle*
%endif

%changelog
* Sat Mar 19 2016 Nico Kadel-Garcia <nkadel@gmail.com> - 1.66-0.4
- Backport to RHEL 7

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.66-3
- Perl 5.22 rebuild

* Tue Sep 09 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.66-2
- Perl 5.20 mass

* Mon Sep 08 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.66-1
- Upstream update.
- Spec cleanup.
- Reflect Source0 having changed.

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.65-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.65-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.65-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 1.65-2
- Perl 5.18 rebuild

* Fri Jul 12 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.65-1
- Upstream update.
- BR: perl(Scalar::Util).
- Fix up bogus dates in %%changelog.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 16 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.63-1
- Upstream update.
- Reflect upstream URL having changed.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.62-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 1.62-2
- Perl 5.16 rebuild

* Thu Apr 12 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.62-1
- Upstream update.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.61-1
- Upstream update.

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.59-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 06 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.59-1
- Upstream update.

* Tue Nov 02 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.58-1
- Upstream update.
- Spec cleanup.

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.56-5
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.56-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.56-2
- rebuild against perl 5.10.1

* Wed Jul 29 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.56-1
- Upstream update.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.55-1
- Upstream update.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 08 2008 Ralf Corsépius <rc040203@freenet.de> - 1.54-1
- Upstream update.

* Fri Apr 25 2008 Ralf Corsépius <rc040203@freenet.de> - 1.53-1
- Upstream update.

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.51-2
- rebuild for new perl

* Mon Jan 21 2008 Ralf Corsépius <rc040203@freenet.de> - 1.51-1
- Upstream update.

* Sun Nov 25 2007 Ralf Corsépius <rc040203@freenet.de> - 1.50-1
- Upstream update.

* Tue Sep 04 2007 Ralf Corsépius <rc040203@freenet.de> - 1.49-1
- Upstream update.
- Update license tag.

* Mon Mar 12 2007 Ralf Corsépius <rc040203@freenet.de> - 1.48-1
- Upstream update.
- BR: perl(ExtUtils::MakeMaker).

* Fri Mar 02 2007 Ralf Corsépius <rc040203@freenet.de> - 1.46-1
- Upstream update.
- Use "by-modules" Source0 (upstream maintainer has changed).

* Wed Oct 04 2006 Ralf Corsépius <rc040203@freenet.de> - 1.45-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.43-2
- Mass rebuild.

* Sat Apr 22 2006 Ralf Corsépius <rc040203@freenet.de> - 1.43-1
- Upstream update.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 1.38-2
- Rebuild for perl-5.8.8.

* Wed Jan 11 2006 Ralf Corsépius <rc040203@freenet.de> - 1.38-1
- Upstream update.
- Spec cleanup.

* Mon Nov 14 2005 Ralf Corsepius <rc040203@freenet.de> - 1.33-1
- Upstream update to 1.33.

* Sun Nov 13 2005 Ralf Corsepius <rc040203@freenet.de>
- BR: perl(Clone) for 1.35.

* Sun Nov 06 2005 Ralf Corsepius <rc040203@freenet.de>
- BR: perl(DBIx::DBSchema) and perl(capitalization) for 1.33
  (Now in FE >= 5).

* Mon Oct 10 2005 Ralf Corsepius <rc040203@freenet.de> - 1.27-2
- chmod -x *.pm.
- BR: perl(Test::Pod).
- Add --with oracle to allow users to conditionally build the 
  perl-DBIx-SearchBuilder-Oracle subpackage.

* Wed Sep 14 2005 Ralf Corsepius <rc040203@freenet.de> - 1.27-1
- Preps for 1.32.
- Split out Oracle.
- FE submission.
