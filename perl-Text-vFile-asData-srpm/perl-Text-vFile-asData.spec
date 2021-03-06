Name:           perl-Text-vFile-asData
Version:        0.07
#Release:        2%{?dist}
Release:        0.2%{?dist}
Summary:        Parse vFile formatted files into data structures
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Text-vFile-asData/
Source0:        http://www.cpan.org/authors/id/R/RC/RCLAMP/Text-vFile-asData-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Class::Accessor::Chained)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

# To be dropped in Fedora 16
Obsoletes:      %{name}-utils < %{version}-%{release}
Provides:       %{name}-utils = %{version}-%{release}

# for improved tests
BuildRequires:  perl(Test::Pod) >= 1.00

# rpm doesn't catch this
Requires:       perl(Class::Accessor::Chained::Fast)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Text::vFile::asData reads vFile format files, such as vCard (RFC 2426) and
vCalendar (RFC 2445).

%prep
%setup -q -n Text-vFile-asData-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Sep  5 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> 0.07-0.2
- Port to RHEL 7, roll back release number to avoid upsream conflict.

* Sat Sep 12 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.07-2
- Remove Text-vFile-asData-0.07.diff.
- Remove *-utils.

* Sat Sep 11 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.07-1
- Upstream update.
- Install */bin (Add Text-vFile-asData-0.07.diff).
- spec overhaul.

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-6
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.05-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 26 2008 Ralf Corsépius <rc040203@freenet.de> 0.05-2
- Split out applications into *-utils.
- Fedora submission.

* Mon Aug 11 2008 Ralf Corsépius <rc040203@freenet.de> 0.05-1
- Specfile autogenerated by cpanspec 1.77.
