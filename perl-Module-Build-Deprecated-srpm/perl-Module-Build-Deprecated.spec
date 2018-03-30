Name:           perl-Module-Build-Deprecated
Version:        0.4210
#Release:        9%{?dist}
Release:        0.1%{?dist}
Summary:        Collection of modules removed from Module-Build
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Build-Deprecated/
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/Module-Build-Deprecated-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(CPAN::Meta::YAML) >= 0.002
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build) >= 0.3601
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version) >= 0.87
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(CPAN::Meta::YAML) >= 0.002
Requires:       perl(version) >= 0.87
Conflicts:      perl-Module-Build < 0.42.07

%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}perl\\(CPAN::Meta::YAML|version\\)

%description
This module contains a number of module that have been removed from
Module-Build:
Module::Build::ModuleInfo - This has been superseded by Module::Metadata
Module::Build::Version - This has been replaced by version
Module::Build::YAML - This has been replaced by CPAN::Meta::YAML

%prep
%setup -q -n Module-Build-Deprecated-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Mar 29 2018 Nico Kadel-Garcia <nkadel@gmail.com> - 0.4210-0.1
- Roll back release number for RHEL 7 compilation
- Add cleanup of .packlist

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4210-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.4210-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4210-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.4210-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4210-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4210-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.4210-3
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.4210-2
- Perl 5.20 rebuild

* Wed Aug 20 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.4210-1
- Initial release
