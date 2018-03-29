Name:           perl-Net-LDAP-SID
Version:        0.001
#7Release:        4%{?dist}
Release:        0.1%{?dist}
Summary:        Net::LDAP::SID Perl module
License:        Artistic 2.0
URL:            http://search.cpan.org/dist/Net-LDAP-SID/
Source0:        http://www.cpan.org/authors/id/K/KA/KARMAN/Net-LDAP-SID-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-interpreter >= 0:5.008003
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Active Directory Security Identifier manipulation

%prep
%setup -q -n Net-LDAP-SID-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.001-1
- Initial Fedora package.
