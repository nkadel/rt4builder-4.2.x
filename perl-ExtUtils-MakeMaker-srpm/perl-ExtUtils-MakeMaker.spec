%global cpan_name ExtUtils-MakeMaker

Name:           perl-%{cpan_name}
Epoch:          1
Version:        7.30
#Release:        2%{?dist}
Release:        0.2%{?dist}
Summary:        Create a module Makefile
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/%{cpan_name}/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/%{cpan_name}-%{version}.tar.gz
# Do not set RPATH to perl shared-library modules by default. Bug #773622.
# This is copy from `perl' package. This is a distributor extension.
Patch0:         %{cpan_name}-7.16-USE_MM_LD_RUN_PATH.patch
# Link to libperl.so explicitly. Bug #960048.
Patch1:         %{cpan_name}-7.12-Link-to-libperl-explicitly-on-Linux.patch
# Unbundle version modules
Patch2:         %{cpan_name}-7.04-Unbundle-version.patch
# Unbundle Encode::Locale module
Patch3:         %{cpan_name}-7.22-Unbundle-Encode-Locale.patch
# Provide maybe_command independently, bug #1129443
Patch4:         %{cpan_name}-7.11-Provide-ExtUtils-MM-methods-as-standalone-ExtUtils-M.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
# Makefile.Pl uses ExtUtils::MakeMaker from ./lib
# B needed only for CPAN::Meta::Requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
# CPAN::Meta::Requirements has a fallback
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# If an XS module is compiled, xsubpp(1) is needed
BuildRequires:  perl-ExtUtils-ParseXS
BuildRequires:  sed
# Tests:
BuildRequires:  perl(AutoSplit)
BuildRequires:  perl(base)
BuildRequires:  perl(CPAN::Meta) >= 2.143240
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Install) >= 1.52
# ExtUtils::Installed not used at tests
BuildRequires:  perl(ExtUtils::Manifest) >= 1.70
# ExtUtils::Packlist not used at tests
# ExtUtils::XSSymSet is not needed (VMS only)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp) >= 0.22
BuildRequires:  perl(Getopt::Long)
# IO::File not used at tests
# IO::Handle not used
BuildRequires:  perl(less)
BuildRequires:  perl(overload)
BuildRequires:  perl(Parse::CPAN::Meta) >= 1.4414
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
# threads::shared not used
BuildRequires:  perl(utf8)
# XSLoader not used
# Optional tests
BuildRequires:  perl-devel
BuildRequires:  perl(B)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(PerlIO)
# Keep YAML optional
# Keep YAML::Tiny optional
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(B)
%if 0%{?fedora}
Recommends:     perl(CPAN::Meta) >= 2.143240
Suggests:       perl(CPAN::Meta::Converter) >= 2.141170
%endif
# CPAN::Meta::Requirements to support version ranges
%if 0%{?fedora}
Recommends:     perl(CPAN::Meta::Requirements) >= 2.130
%endif
Requires:       perl(Data::Dumper)
Requires:       perl(DynaLoader)
# Encode is needed for producing POD with =encoding statement correctly
Requires:       perl(Encode)
%if 0%{?fedora}
Recommends:     perl(Encode::Locale)
%endif
#Requires:       perl(ExtUtils::Command) >= 1.19
Requires:       perl(ExtUtils::Command) >= 7.30
Requires:       perl(ExtUtils::Install) >= 1.54
Requires:       perl(ExtUtils::Manifest) >= 1.70
# ExtUtils::XSSymSet is not needed (VMS only)
Requires:       perl(File::Find)
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(Getopt::Long)
%if 0%{?fedora}
Suggests:       perl(JSON::PP)
%endif
# Optional Pod::Man is needed for generating manual pages from POD
Requires:       perl(Pod::Man)
Requires:       perl(POSIX)
Requires:       perl(Test::Harness)
%if 0%{?fedora}
Recommends:     perl(Time::HiRes)
%endif
# Text::ParseWords is not needed (Win32 only)
# VMS::Filespec is not needed (VMS only)
# Win32 is not needed (Win32 only)
# If an XS module is compiled, xsubpp(1) is needed
Requires:       perl-ExtUtils-ParseXS
# If an XS module is built, code generated from XS will be compiled and it
# includes Perl header files.
# TODO: This dependency will be weaken in order to relieve building noarch
# packages from perl-devel and gcc.
Requires:       perl-devel

# Do not export underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)\s*$
# Do not export private redefinitions
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DynaLoader|ExtUtils::MakeMaker::_version\\)

%description
This utility is designed to write a Makefile for an extension module from a
Makefile.PL. It is based on the Makefile.SH model provided by Andy
Dougherty and the perl5-porters.

%package -n perl-ExtUtils-Command
Summary:        Perl routines to replace common UNIX commands in Makefiles
License:        GPL+ or Artistic
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)
Requires:       perl(File::Copy)
Requires:       perl(File::Find)
Requires:       perl(File::Path)
# File::Spec not used
# VMS::Feature not used

%description -n perl-ExtUtils-Command
This Perl module is used to replace common UNIX commands. In all cases the
functions work with @ARGV rather than taking arguments. This makes them
easier to deal with in Makefiles.

%package -n perl-ExtUtils-MM-Utils
Summary:        ExtUtils::MM methods without dependency on ExtUtils::MakeMaker
License:        GPL+ or Artistic
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description -n perl-ExtUtils-MM-Utils
This is a collection of ExtUtils::MM subroutines that are used by many
other modules but that do not need full-featured ExtUtils::MakeMaker. The
issue with ExtUtils::MakeMaker is it pulls in Perl header files and that
is an overkill for small subroutines.

%prep
%setup -q -n ExtUtils-MakeMaker-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
# Remove bundled modules
rm -rf bundled
sed -i -e '/^bundled\// d' MANIFEST
rm -rf t/lib/Test
sed -i -e '/^t\/lib\/Test\// d' MANIFEST
rm -rf lib/ExtUtils/MakeMaker/version{,.pm}
sed -i -e '/^lib\/ExtUtils\/MakeMaker\/version[\/\.]/ d' MANIFEST
rm -rf lib/ExtUtils/MakeMaker/Locale.pm
sed -i -e '/^lib\/ExtUtils\/MakeMaker\/Locale\.pm/ d' MANIFEST

%build
BUILDING_AS_PACKAGE=1 perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

#%check
#make test

%files
%doc Changes CONTRIBUTING README
%{_bindir}/*
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/ExtUtils/Command.pm
%exclude %dir %{perl_vendorlib}/ExtUtils/MM
%exclude %{perl_vendorlib}/ExtUtils/MM/Utils.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
%exclude %{_mandir}/man3/ExtUtils::Commands.*
%exclude %{_mandir}/man3/ExtUtils::MM::Utils.*

%files -n perl-ExtUtils-Command
%dir %{perl_vendorlib}/ExtUtils
%{perl_vendorlib}/ExtUtils/Command.pm
%if ! 0%{?rhel}
%{_mandir}/man3/ExtUtils::Command.*
%endif

%files -n perl-ExtUtils-MM-Utils
%dir %{perl_vendorlib}/ExtUtils
%dir %{perl_vendorlib}/ExtUtils/MM
%{perl_vendorlib}/ExtUtils/MM/Utils.pm
%if ! 0%{?rhel}
%{_mandir}/man3/ExtUtils::MM::Utils.*
%endif

%changelog
* Sat Mar 24 2018 Nico Kadel-Garcia <nkadel@gmail.com>
- Backport to RHEL 7
- Disable checks, fail on RHEL 7
- Disable publication of Command and MM:Utils pages for RHEL, which has them in perl base package

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Petr Pisar <ppisar@redhat.com> - 1:7.30-1
- 7.30 bump

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:7.28-2
- Perl 5.26 rebuild

* Wed May 31 2017 Petr Pisar <ppisar@redhat.com> - 7.28-1
- 7.28 bump

* Mon May 29 2017 Petr Pisar <ppisar@redhat.com> - 7.26-1
- 7.26 bump
- Fix META generation (CPAN RT#121913)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 25 2016 Jitka Plesnikova <jplesnik@redhat.com> - 7.24-1
- 7.24 bump

* Tue Aug 09 2016 Jitka Plesnikova <jplesnik@redhat.com> - 7.22-1
- 7.22 bump

* Tue May 24 2016 Petr Pisar <ppisar@redhat.com> - 7.18-1
- 7.18 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 7.16-2
- Perl 5.24 rebuild

* Mon May 09 2016 Petr Pisar <ppisar@redhat.com> - 7.16-1
- 7.16 bump

* Mon Apr 25 2016 Petr Pisar <ppisar@redhat.com> - 7.14-1
- 7.14 bump

* Wed Apr 20 2016 Petr Pisar <ppisar@redhat.com> - 7.12-1
- 7.12 bump

* Tue Apr 19 2016 Petr Pisar <ppisar@redhat.com> - 7.10-5
- Own ExtUtils/MM directory by perl-ExtUtils-MM-Utils only
- Require perl-devel by perl-ExtUtils-MakeMaker

* Mon Apr 18 2016 Petr Pisar <ppisar@redhat.com> - 7.10-4
- Provide maybe_command independently (bug #1129443)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 03 2015 Petr Pisar <ppisar@redhat.com> - 7.10-2
- Declare optional dependencies on Recommends level

* Fri Sep 11 2015 Petr Pisar <ppisar@redhat.com> - 7.10-1
- 7.10 bump

* Wed Sep 09 2015 Petr Pisar <ppisar@redhat.com> - 7.08-1
- 7.08 bump

* Tue Sep 01 2015 Jitka Plesnikova <jplesnik@redhat.com> - 7.06-2
- Remove new line from INC (CPAN RT#106808)

* Tue Sep 01 2015 Petr Pisar <ppisar@redhat.com> - 7.06-1
- 7.06 bump
- ExtUtils::Command module is distributed by ExtUtils-MakeMaker

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.04-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 7.04-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 7.04-2
- Perl 5.22 rebuild

* Fri Dec 05 2014 Petr Pisar <ppisar@redhat.com> - 7.04-1
- 7.04 bump

* Tue Nov 11 2014 Petr Pisar <ppisar@redhat.com> - 7.02-1
- 7.02 bump
- Cope with missing Encode::Locale

* Wed Nov 05 2014 Petr Pisar <ppisar@redhat.com> - 7.00-2
- Fix building with older xsubpp

* Mon Oct 27 2014 Petr Pisar <ppisar@redhat.com> - 7.00-1
- 7.00 bump

* Fri Oct 24 2014 Petr Pisar <ppisar@redhat.com> - 6.98-311
- Require perl-ExtUtils-ParseXS because of xsubpp

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 6.98-310
- Increase release to favour standalone package

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 6.98-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Petr Pisar <ppisar@redhat.com> - 6.98-1
- 6.98 bump

* Mon Apr 14 2014 Petr Pisar <ppisar@redhat.com> - 6.96-1
- 6.96 bump

* Wed Mar 26 2014 Petr Pisar <ppisar@redhat.com> - 6.94-1
- 6.94 bump

* Fri Mar 14 2014 Petr Pisar <ppisar@redhat.com> - 6.92-1
- 6.92 bump

* Fri Feb 21 2014 Petr Pisar <ppisar@redhat.com> - 6.90-1
- 6.90 bump

* Mon Feb 03 2014 Petr Pisar <ppisar@redhat.com> - 6.88-1
- 6.88 bump

* Mon Jan 06 2014 Petr Pisar <ppisar@redhat.com> - 6.86-1
- 6.86 bump

* Mon Dec 02 2013 Petr Pisar <ppisar@redhat.com> - 6.84-1
- 6.84 bump

* Tue Nov 05 2013 Petr Pisar <ppisar@redhat.com> - 6.82-1
- 6.82 bump

* Wed Oct 16 2013 Petr Pisar <ppisar@redhat.com> - 6.80-1
- 6.80 bump

* Tue Sep 24 2013 Petr Pisar <ppisar@redhat.com> - 6.78-1
- 6.78 bump

* Mon Sep 16 2013 Petr Pisar <ppisar@redhat.com> - 6.76-2
- Specify all dependencies (bug #1007755)

* Tue Sep 10 2013 Petr Pisar <ppisar@redhat.com> - 6.76-1
- 6.76 bump

* Mon Sep 02 2013 Petr Pisar <ppisar@redhat.com> - 6.74-1
- 6.74 bump

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 6.72-1
- 6.72 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.68-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 6.68-4
- Perl 5.18 rebuild

* Tue Jul 02 2013 Petr Pisar <ppisar@redhat.com> - 6.68-3
- Link to libperl.so explicitly (bug #960048)

* Thu Jun 27 2013 Jitka Plesnikova <jplesnik@redhat.com> - 6.68-2
- Update BRs

* Mon Jun 17 2013 Petr Pisar <ppisar@redhat.com> - 6.68-1
- 6.68 bump

* Mon Apr 22 2013 Petr Pisar <ppisar@redhat.com> - 6.66-1
- 6.66 bump

* Tue Jan 29 2013 Petr Pisar <ppisar@redhat.com> - 6.64-2
- Run-require POD convertors to get manual pages when building other packages

* Mon Dec 17 2012 Petr Pisar <ppisar@redhat.com> - 6.64-1
- 6.64 bump

* Tue Aug 28 2012 Petr Pisar <ppisar@redhat.com> - 6.63.02-241
- Compute RPM version
- Do not build-require itself, the build script runs from ./lib

* Mon Aug 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 6.63.02-240
- update version to the same as in perl.srpm
- Bump release to override sub-package from perl.spec

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.62-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 6.62-3
- Perl 5.16 rebuild

* Thu Jan 12 2012 Petr Pisar <ppisar@redhat.com> - 6.62-2
- Do not set RPATH to perl shared-library modules by default (bug #773622)

* Fri Nov 25 2011 Petr Pisar <ppisar@redhat.com> 6.62-1
- Specfile autogenerated by cpanspec 1.78.
- Remove defattr and BuildRoot from spec.
