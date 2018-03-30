Name:           perl-Net-LDAP-Server-Test
Version:        0.22
#Release:        4%{?dist}
Release:        0.1%{?dist}
Summary:        Test Net::LDAP code
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Net-LDAP-Server-Test/
Source0:        http://www.cpan.org/authors/id/K/KA/KARMAN/Net-LDAP-Server-Test-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter >= 0:5.008003

BuildRequires:  perl-generators

BuildRequires:  perl(Carp)
BuildRequires:  perl(Convert::ASN1)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::LDAP::ASN)
BuildRequires:  perl(Net::LDAP::Constant)
BuildRequires:  perl(Net::LDAP::Control)
BuildRequires:  perl(Net::LDAP::Entry)
BuildRequires:  perl(Net::LDAP::Filter)
BuildRequires:  perl(Net::LDAP::FilterMatch)
BuildRequires:  perl(Net::LDAP::LDIF)
BuildRequires:  perl(Net::LDAP::Server) >= 0.3
BuildRequires:  perl(Net::LDAP::SID)
BuildRequires:  perl(Net::LDAP::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(fields)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Optional
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

BuildRequires:  %{__make}
BuildRequires:  %{__perl}

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Test your Net::LDAP code without having a real LDAP server available.

%prep
%setup -q -n Net-LDAP-Server-Test-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.22-1
- Initial Fedora package.
