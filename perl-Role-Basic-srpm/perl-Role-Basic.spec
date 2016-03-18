Name:           perl-Role-Basic
Version:        0.13
Release:        5%{?dist}
Summary:        Just roles. Nothing else
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Role-Basic/
Source0:        http://www.cpan.org/authors/id/O/OV/OVID/Role-Basic-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Simplified Moose-like roles.

%prep
%setup -q -n Role-Basic-%{version}
# Convert to utf-8
iconv -f ISO-8859-1 -t utf-8 Changes > Changes~
mv Changes~ Changes

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 19 2013 Ralf Corsépius <corsepiu@fedoraproject.org> 0.13-1
- Initial Fedora submission.
