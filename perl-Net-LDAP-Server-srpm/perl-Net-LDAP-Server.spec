Name:           perl-Net-LDAP-Server
Version:        0.43
#Release:        5%{?dist}
Release:        0.1%{?dist}
Summary:        Net::LDAP::Server Perl module
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Net-LDAP-Server/
Source0:        http://www.cpan.org/authors/id/A/AA/AAR/Net-LDAP-Server-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators

BuildRequires:  perl(Convert::ASN1)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::LDAP::ASN)
BuildRequires:  perl(Net::LDAP::Constant)
BuildRequires:  perl(Net::LDAP::Entry)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  perl(fields)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

BuildRequires:  %{__make}

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Net::LDAP::Server provides the protocol handling for an LDAP server. You
can subclass it and implement the methods you need. Then you just
instantiate your subclass and call its C<handle> method to establish a
connection with the client.

%prep
%setup -q -n Net-LDAP-Server-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changelog README
%doc examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 28 2018 Nico Kadel-Garcia <nkadel@gmail.com> - 0.43-0.1
- Flush .packlist and emptry directories

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.43-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 29 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.43-2
* Reflect feedback from package review.

* Wed Aug 24 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.43-1
- Initial Fedora package.
