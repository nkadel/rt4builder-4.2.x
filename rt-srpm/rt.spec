#
# Copyright (c) 2005-2018, Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# --with devel_mode/--without devel_mode
#	enable/disable building/installing devel files
#	Default: enabled
%bcond_without devel_mode

# --with runtests
#	run testsuite when building the rpm
#	Default: disabled (does not work in chroots.)
%bcond_with runtests

# --with mysql
#	configure for use with mysql
%bcond_with mysql
# --with pg
#	configure for use with postgress
%bcond_with pg

# default to mysql
%if !%{with mysql} && !%{with pg}
%global with_mysql 1
%endif

%global RT_BINDIR		%{_bindir}
%global RT_SBINDIR		%{_sbindir}
%global RT_FONTSDIR		%{_datadir}/%{name}/fonts
%global RT_LIBDIR		%{perl_vendorlib}
%global RT_WWWDIR		%{_datadir}/%{name}/html
%global RT_LEXDIR		%{_datadir}/%{name}/po
%global RT_LOGDIR		%{_localstatedir}/log/%{name}
%global RT_CACHEDIR		%{_localstatedir}/cache/%{name}
%global RT_LOCALSTATEDIR	%{_localstatedir}/lib/%{name}
%global RT_STATICDIR		%{_datadir}/%{name}/static

Name:		rt
Version:	4.4.4
Release:	0%{?dist}
Summary:	Request tracker

Group:		Applications/Internet
License:	GPLv2+
URL:		https://bestpractical.com/request-tracker
Source0:	https://download.bestpractical.com/pub/rt/release/rt-%{version}.tar.gz
# Notes on running the testsuite
Source1:	README.tests
# rt Apache configuration
Source2:	rt.conf.in
# Fedora-specific installation notes
Source3:	README.fedora.in
# rt logrotate configuration
Source4:	rt.logrotate.in

Patch1: 0001-Add-Fedora-configuration.patch
Patch2: 0002-Use-usr-bin-perl-instead-of-usr-bin-env-perl.patch
Patch3: 0003-Remove-fixperms-font-install.patch
Patch4: 0004-Fix-permissions.patch

BuildArch:	noarch

Obsoletes:	rt3 < %{version}-%{release}
Provides:	rt3 = %{version}-%{release}
Obsoletes:	rt4 < %{version}-%{release}
Provides:	rt4 = %{version}-%{release}

# This list is alpha sorted
BuildRequires: autoconf
BuildRequires: perl-generators
BuildRequires: perl(Apache::DBI)
BuildRequires: perl(Apache::Session) >= 1.53
BuildRequires: perl(Business::Hours)
BuildRequires: perl(Cache::Simple::TimedExpiry)
BuildRequires: perl(CGI::Cookie) >= 1.20
BuildRequires: perl(CGI::PSGI)
BuildRequires: perl(CGI::Emulate::PSGI)
BuildRequires: perl(Class::ReturnValue) >= 0.40
BuildRequires: perl(Convert::Color)
BuildRequires: perl(CPAN)
BuildRequires: perl(Crypt::Eksblowfish)
BuildRequires: perl(Crypt::SSLeay)
BuildRequires: perl(Crypt::X509)
BuildRequires: perl(CSS::Minifier::XS)
BuildRequires: perl(CSS::Squish) >= 0.06
BuildRequires: perl(Data::GUID)
BuildRequires: perl(Data::ICal)
BuildRequires: perl(Data::Page::Pageset)
BuildRequires: perl(Date::Extract) >= 0.02
BuildRequires: perl(Date::Manip)
BuildRequires: perl(DateTime::Format::Natural) >= 0.67
BuildRequires: perl(Date::Format)
BuildRequires: perl(DateTime) >= 0.44
BuildRequires: perl(DateTime::Locale) >= 0.40
%{?with_mysql:BuildRequires: perl(DBD::mysql) >= 2.1018}
%{?with_pg:BuildRequires: perl(DBD::Pg) >= 1.43}
BuildRequires: perl(DBI) >= 1.37
BuildRequires: perl(DBIx::SearchBuilder) >= 1.59
BuildRequires: perl(Devel::StackTrace) >= 1.19
BuildRequires: perl(Devel::GlobalDestruction)
BuildRequires: perl(Digest::base)
BuildRequires: perl(Digest::MD5) >= 2.27
# Email::Address < 1.908 is vulnerable to CVE-2015-7686
BuildRequires: perl(Email::Address) >= 1.908
BuildRequires: perl(Email::Address::List) >= 0.06
BuildRequires: perl(Encode) >= 2.64
BuildRequires: perl(Errno)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Glob)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::Spec) >= 0.8
BuildRequires: perl(File::Temp) >= 0.19
BuildRequires: perl(File::Which)
BuildRequires: perl(GD)
BuildRequires: perl(GD::Graph) >= 1.47
BuildRequires: perl(GD::Text)
BuildRequires: perl(GnuPG::Interface)
BuildRequires: perl(GraphViz)
BuildRequires: perl(Getopt::Long) >= 2.24
BuildRequires: perl(HTML::Entities)
%{?with_devel_mode:BuildRequires: perl(HTML::Form)}
BuildRequires: perl(HTML::FormatText)
BuildRequires: perl(HTML::FormatText::WithLinks) >= 0.14
BuildRequires: perl(HTML::FormatText::WithLinks::AndTables) >= 0.06
BuildRequires: perl(HTML::Mason) >= 1.43
BuildRequires: perl(HTML::Mason::PSGIHandler)
BuildRequires: perl(HTML::Quoted)
BuildRequires: perl(HTML::RewriteAttributes) >= 0.02
BuildRequires: perl(HTML::Scrubber) >= 0.08
BuildRequires: perl(HTML::TreeBuilder)
BuildRequires: perl(HTTP::Request::Common)
BuildRequires: perl(HTTP::Server::Simple) >= 0.34
BuildRequires: perl(HTTP::Server::Simple::Mason) >= 0.09
BuildRequires: perl(HTTP::Status)
BuildRequires: perl(IPC::Run)
BuildRequires: perl(IPC::Run3)
BuildRequires: perl(IPC::Run::SafeHandles)
BuildRequires: perl(JSON)
BuildRequires: perl(JavaScript::Minifier)
BuildRequires: perl(JavaScript::Minifier::XS)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Locale::Maketext) >= 1.06
BuildRequires: perl(Locale::Maketext::Fuzzy) >= 0.11
BuildRequires: perl(Locale::Maketext::Lexicon) >= 0.32
BuildRequires: perl(Locale::PO)
BuildRequires: perl(Log::Dispatch) >= 2.23
BuildRequires: perl(Net::LDAP::Server::Test)
%{?with_devel_mode:BuildRequires: perl(Log::Dispatch::Perl)}
BuildRequires: perl(LWP)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(LWP::Protocol::https)
BuildRequires: perl(Mail::Mailer) >= 1.57
BuildRequires: perl(MIME::Entity) >= 5.425
BuildRequires: perl(MIME::Types)
%{?with_devel_mode:BuildRequires: perl(Module::Refresh) >= 0.03}
BuildRequires: perl(Module::Versions::Report) >= 1.05
BuildRequires: perl(Mozilla::CA)
BuildRequires: perl(Mojo::DOM)
BuildRequires: perl(Net::CIDR)
BuildRequires: perl(Net::IP)
BuildRequires: perl(Net::Server)
BuildRequires: perl(Net::Server::PreFork)
BuildRequires: perl(Net::SMTP)
BuildRequires: perl(Net::SSL)
BuildRequires: perl(PerlIO::eol)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Pod::Select)
BuildRequires: perl(Plack)
BuildRequires: perl(Plack::Handler::Starlet)
%{?with_devel_mode:BuildRequires: perl(Plack::Middleware::Test::StashWarnings) >= 0.06}
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Regexp::Common::net::CIDR)
BuildRequires: perl(Regexp::IPv6)
BuildRequires: perl(Role::Basic) >= 0.12
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Scope::Upper)
BuildRequires: perl(Set::Tiny)
BuildRequires: perl(Storable) >= 2.08
%{?with_devel_mode:BuildRequires: perl(String::ShellQuote)}
BuildRequires: perl(Symbol::Global::Name) >= 0.04
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Term::ReadLine)
%{?with_devel_mode:BuildRequires: perl(Test::Builder) >= 0.77}
%{?with_devel_mode:BuildRequires: perl(Test::Deep)}
%{?with_devel_mode:BuildRequires: perl(Test::Email)}
%{?with_devel_mode:BuildRequires: perl(Email::Abstract)}
%{?with_devel_mode:BuildRequires: perl(Test::Expect) >= 0.31}
%{?with_devel_mode:BuildRequires: perl(Test::MockTime)}
%{?with_devel_mode:BuildRequires: perl(Test::NoWarnings)}
%{?with_devel_mode:BuildRequires: perl(Test::Pod) >= 1.14}
%{?with_devel_mode:BuildRequires: perl(Test::Warn)}
%{?with_devel_mode:BuildRequires: perl(Test::WWW::Mechanize)}
%{?with_devel_mode:BuildRequires: perl(Test::WWW::Mechanize::PSGI)}
BuildRequires: perl(Text::ParseWords)
BuildRequires: perl(Text::Password::Pronounceable)
BuildRequires: perl(Text::Quoted) >= 2.02
BuildRequires: perl(Text::Template)
BuildRequires: perl(Text::WikiFormat) >= 0.76
BuildRequires: perl(Text::Wrapper)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(Time::ParseDate)
BuildRequires: perl(Tree::Simple) >= 1.04
BuildRequires: perl(UNIVERSAL::require)
%{?with_devel_mode:BuildRequires: perl(WWW::Mechanize)}
BuildRequires: perl(XML::RSS) >= 1.05
%{?with_devel_mode:BuildRequires: perl(XML::Simple)}

%{?with_runtests:BuildRequires: perl(DBD::SQLite)}
%{?with_runtests:BuildRequires: perl(Test::Warn)}
%{?with_runtests:BuildRequires: perl(Test::MockTime)}
%{?with_runtests:BuildRequires: perl(String::ShellQuote)}
%{?with_runtests:BuildRequires: perl(Test::Expect)}

BuildRequires:	/usr/bin/pod2man
BuildRequires:	/usr/sbin/apachectl

# the original sources carry bundled versions of these ...
Requires:  /usr/share/fonts/google-droid/DroidSansFallback.ttf
Requires:  /usr/share/fonts/google-droid/DroidSans.ttf
# ... we use symlinks to the system-wide versions ...
BuildRequires:	/usr/share/fonts/google-droid/DroidSansFallback.ttf
BuildRequires:	/usr/share/fonts/google-droid/DroidSans.ttf

Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:	%{_sysconfdir}/httpd/conf.d

Requires(postun): %{__rm}

# rpm does not catch these:
Requires: perl(Apache::Session)
Requires: perl(Business::Hours)
Requires: perl(Calendar::Simple)
Requires: perl(CSS::Squish)
Requires: perl(Data::Page)
Requires: perl(Data::Page::Pageset)
Requires: perl(Data::ICal)
Requires: perl(Data::ICal::Entry::Event)
%{?with_mysql:Requires: perl(DBD::mysql) >= 2.1018}
# This should be: Requires: perl(DBD::Pg) != 3.3.0
# cf. RHBZ#1138926
%{?with_pg:Requires: perl(DBD::Pg)}
%{?with_pg:Conflicts: perl(DBD::Pg) == 3.3.0}
Requires: perl(DateTime::Format::Natural) >= 0.67
Requires: perl(Log::Dispatch::Perl)
Requires: perl(GD::Text)
Requires: perl(GD::Graph::bars)
Requires: perl(GD::Graph::pie)
Requires: perl(HTML::Quoted)
Requires: perl(HTTP::Server::Simple::Mason)
Requires: perl(HTML::Mason::Request)
Requires: perl(I18N::LangTags::List)
Requires: perl(IPC::Run3)
Requires: perl(LWP::MediaTypes)
Requires: perl(mod_perl2)
Requires: perl(Module::Versions::Report)
Requires: perl(Net::Server::PreFork)
Requires: perl(PerlIO::eol)
Requires: perl(Plack::Middleware::Test::StashWarnings) >= 0.06
Requires: perl(Plack::Handler::Starlet)
Requires: perl(Text::Quoted)
Requires: perl(Text::WikiFormat)
Requires: perl(Time::ParseDate)
Requires: perl(URI::URL)
Requires: perl(XML::RSS)

# rpm fails to add these:
Provides: perl(RT::Shredder::Exceptions)

# Split out. Technically, not actually necessary, but ... let us keep it for now.
Requires: rt-mailgate

%{?perl_default_filter}

# Keep FCGI optional
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(FCGI::ProcManager\\)
# Work-around rpm depgenerator defect: 
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DBIx::SearchBuilder::Handle::\\)

# Filter redundant provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(RT\\)$
# Filter bogus provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(HTML::Mason
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(IO::Handle::CRLF\\)$


%description
RT is an enterprise-grade ticketing system which enables a group of people
to intelligently and efficiently manage tasks, issues, and requests submitted
by a community of users.


%package mailgate
Summary: rt mailgate utility
Group:	Applications/Internet
# rpm does not catch these:
Requires:	perl(Pod::Usage)
Requires:	perl(HTML::TreeBuilder)
Requires:	perl(HTML::FormatText)
Obsoletes:	rt3-mailgate < %{version}-%{release}
Provides:	rt3-mailgate = %{version}-%{release}
Obsoletes:	rt4-mailgate < %{version}-%{release}
Provides:	rt4-mailgate = %{version}-%{release}

%description mailgate
%{summary}


%if %{with devel_mode}
%package tests
Summary:	Test suite for package rt
Group:		Development/Debug
Requires:	%{name} = %{version}-%{release}
Requires(postun): %{__rm}
Requires:	/usr/bin/prove
Requires:	perl(RT::Test)
# rpm does not catch these:
Requires:	perl(DBD::SQLite)
Requires:	perl(GnuPG::Interface)
# Bug: The testsuite unconditionally depends upon perl(GraphViz)
Requires:	perl(GraphViz)
Requires:	perl(Net::LDAP::Server::Test)
Requires:	perl(Plack::Handler::Apache2)
Requires:	perl(Set::Tiny)
Requires:	perl(String::ShellQuote)
Requires:	perl(Test::Deep)
Requires:	perl(Test::Expect)
Requires:	perl(Test::MockTime)
Requires:	perl(Test::Warn)

Obsoletes:	rt3-tests < %{version}-%{release}
Provides:	rt3-tests = %{version}-%{release}
Obsoletes:	rt4-tests < %{version}-%{release}
Provides:	rt4-tests = %{version}-%{release}

%description tests
%{summary}

# Running the tests leaves stray files
# remove everything by brute force.
%postun tests
if [ $1 -eq 0 ]; then
  %{__rm} -rf %{perl_testdir}/%{name}
fi


%package -n perl-RT-Test
Summary: rt test utility module
Group:	Applications/Internet
Requires:	rt = %{version}-%{release}
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# rpm does not catch these:
Requires:	perl(Test::WWW::Mechanize::PSGI)
Requires:	perl(Mojo::DOM)

%description -n perl-RT-Test
%{summary}

%endif # devel_mode

%prep
%setup -q -n rt-%{version}

# Lower Email::Address dependency version
sed -i.version 's/^Email::Address 1.912/Email::Address 1.908/g' sbin/rt-test-dependencies.in

sed -e 's,@RT_CACHEDIR@,%{RT_CACHEDIR},' %{SOURCE3} \
  > README.fedora
sed -e 's,@RT_LOGDIR@,%{RT_LOGDIR},' %{SOURCE4} \
  > rt.logrotate

# remove auto*generated files
find -name '*.in' | \
while read a; do b=$(echo "$a" | sed -e 's,\.in$,,'); rm -f "$b"; done

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# Propagate rpm directories to config.layout
cat << \EOF >> config.layout

#   Fedora directory layout.
<Layout Fedora>
  bindir:		%{RT_BINDIR}
  sbindir:		%{RT_SBINDIR}
  sysconfdir:		%{_sysconfdir}/%{name}
  libdir:		%{RT_LIBDIR}
  manualdir:		%{_pkgdocdir}/docs
  lexdir:		%{RT_LEXDIR}
  localstatedir:	%{RT_LOCALSTATEDIR}
  htmldir:		%{RT_WWWDIR}
  fontdir:		%{RT_FONTSDIR}
  staticdir:		%{RT_STATICDIR}
  logfiledir:		%{RT_LOGDIR}
  masonstatedir:	%{RT_CACHEDIR}/mason_data
  sessionstatedir:	%{RT_CACHEDIR}/session_data
  customdir:		%{_prefix}/local/lib/%{name}
  custometcdir:		%{_prefix}/local/etc/%{name}
  customhtmldir:	${customdir}/html
  customlexdir:		${customdir}/po
  customlibdir:		${customdir}/lib
</Layout>
EOF

# Comment out the Makefile trying to change groups/owners
# Fix DESTDIR support
sed -i \
	-e 's,	chgrp,	: chrgp,g' \
	-e 's,	chown,	: chown,g' \
	-e 's,$(DESTDIR)/,$(DESTDIR),g' \
	-e 's,-o $(BIN_OWNER) -g $(RTGROUP),,g' \
Makefile.in

# Install upgrade/ into %%{_datadir}/%%{name}/upgrade
sed -i -e 's,$(RT_ETC_PATH)/upgrade,%{_datadir}/%{name}/upgrade,g' Makefile.in

%build
# Added for rt-4.4.4
%{__autoconf}
%configure \
--with-apachectl=/usr/sbin/apachectl \
--with-web-user=apache --with-web-group=apache \
--with-db-type=%{?with_mysql:mysql}%{?with_pg:Pg} \
--enable-layout=Fedora \
--with-web-handler=modperl2 \
--libdir=%{RT_LIBDIR}

make %{?_smp_mflags}

# Explicitly check for devel-mode deps
%{?with_devel_mode:%{__perl} ./sbin/rt-test-dependencies --verbose --with-%{?with_mysql:mysql}%{?with_pg:pg} --with-modperl2 --with-dev}

# Generate man-pages
for file in \
bin/rt \
bin/rt-crontool \
bin/rt-mailgate \
sbin/rt-attributes-viewer \
sbin/rt-clean-sessions \
sbin/rt-dump-metadata \
sbin/rt-email-dashboards \
sbin/rt-email-digest \
sbin/rt-email-group-admin \
sbin/rt-externalize-attachments \
sbin/rt-fulltext-indexer \
sbin/rt-importer \
sbin/rt-preferences-viewer \
sbin/rt-server \
sbin/rt-server.fcgi \
sbin/rt-session-viewer \
sbin/rt-setup-database \
sbin/rt-setup-fulltext-index \
sbin/rt-serializer \
sbin/rt-shredder \
sbin/rt-validate-aliases \
sbin/rt-validator \
sbin/standalone_httpd \
; do
/usr/bin/pod2man $file > $file.1
done


%install
make install DESTDIR=${RPM_BUILD_ROOT}

# Work-around to regression in rpm >= 4.12.90:
# Cannot mix %%doc with directly installed docs, anymore.
# Need to install all files directly.
install -m 644 README README.fedora ${RPM_BUILD_ROOT}%{_pkgdocdir}

# We do not want CPAN
rm -f ${RPM_BUILD_ROOT}%{_sbindir}/rt-test-dependencies

# Install apache configuration
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d
sed -e 's,@RT_WWWDIR@,%{RT_WWWDIR},g' \
  -e 's,@RT_SBINDIR@,%{RT_SBINDIR},g' \
  -e 's,@RT_BINDIR@,%{RT_BINDIR},g' \
  %{SOURCE2} > ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d/%{name}.conf

mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
for file in bin/*.1 sbin/*.1; do
install -m 0644 $file ${RPM_BUILD_ROOT}%{_mandir}/man1
done

# missed by "make install"
install -d -m755 ${RPM_BUILD_ROOT}%{RT_LOGDIR}
# missed by "make install"
install -d -m755 ${RPM_BUILD_ROOT}%{RT_LOCALSTATEDIR}

# install log rotation stuff
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
install -m 644 rt.logrotate ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}

# Symlink, %%{_sysconfdir}/%%{name}/upgrade is hard-coded at various places
ln -s %{_datadir}/%{name}/upgrade ${RPM_BUILD_ROOT}%{_sysconfdir}/%{name}/upgrade

install -d -m755 ${RPM_BUILD_ROOT}%{RT_FONTSDIR}
ln -s /usr/share/fonts/google-droid/DroidSans.ttf ${RPM_BUILD_ROOT}%{RT_FONTSDIR}
ln -s /usr/share/fonts/google-droid/DroidSansFallback.ttf ${RPM_BUILD_ROOT}%{RT_FONTSDIR}

install -d -m755 ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}
cp -R t ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}

# Uninstalled stuff the testsuite accesses
install -d -m755 ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/devel
cp -R devel/tools ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/devel
cp -R devel/docs ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/devel
# Some parts of the testsuite want relative paths
cp %{SOURCE1} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}
install -d -m755 ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/share
ln -s %{RT_WWWDIR} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/share/html
ln -s %{RT_STATICDIR} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/share/static
ln -s %{_bindir} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/bin
ln -s %{_sbindir} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/sbin
ln -s %{_sysconfdir}/%{name} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/etc
ln -s %{RT_LIBDIR} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/lib
ln -s %{_pkgdocdir}/docs ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/docs


# These files should not be installed
rm ${RPM_BUILD_ROOT}%{RT_LEXDIR}/*.pot
rm ${RPM_BUILD_ROOT}%{RT_LIBDIR}/RT/Generated.pm.in

# Fix permissions
find ${RPM_BUILD_ROOT}%{RT_WWWDIR} \
  -type f -exec chmod a-x {} \;

# Silence rpmlint
chmod a+x \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/3.8-ical-extension \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/4.0-customfield-checkbox-extension \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/generate-rtaddressregexp \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/sanity-check-stylesheets \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/shrink-cgm-table \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/shrink-transactions-table \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/switch-templates-to \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/time-worked-history \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/upgrade-articles \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/upgrade-mysql-schema.pl \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/vulnerable-passwords

%check
# The tests do not work in buildroots, they
# - require to be run as root
# - require an operational rt system
%{?with_runtests:make test}

%{!?with_runtests:/usr/bin/prove -l t/pod.t}

%postun
if [ $1 -eq 0 ]; then
  %{__rm} -rf %{RT_CACHEDIR}
fi


%files
%{_pkgdocdir}
%license COPYING
%{_bindir}/*
%{_sbindir}/*
%exclude %{_bindir}/rt-mailgate
%{_mandir}/man1/*
%exclude %{_mandir}/man1/rt-mailgate*
%{RT_LIBDIR}/*
%exclude %{RT_LIBDIR}/RT/Test*
%attr(0700,apache,apache) %{RT_LOGDIR}
%attr(0760,apache,apache) %{RT_LOCALSTATEDIR}

%dir %{_sysconfdir}/%{name}
%attr(-,root,root)%{_datadir}/%{name}/upgrade
%attr(-,root,root)%{_sysconfdir}/%{name}/upgrade
%attr(-,root,root)%{_sysconfdir}/%{name}/acl*
%attr(-,root,root)%{_sysconfdir}/%{name}/schema*
%attr(-,root,root)%{_sysconfdir}/%{name}/init*
%{?!with_pg:%exclude %{_sysconfdir}/%{name}/*.Pg}
%{?!with_pg:%exclude %{_datadir}/%{name}/upgrade/*/*.Pg}
%exclude %{_sysconfdir}/%{name}/*.Oracle
%exclude %{_datadir}/%{name}/upgrade/*/*.Oracle
%exclude %{_sysconfdir}/%{name}/*.SQLite
%exclude %{_datadir}/%{name}/upgrade/*/*.SQLite
%{?!with_mysql:%exclude %{_sysconfdir}/%{name}/*.mysql}
%{?!with_mysql:%exclude %{_datadir}/%{name}/upgrade/*/*.mysql}
%attr(0750,apache,apache) %{_sysconfdir}/%{name}/RT_SiteConfig.d
%config(noreplace) %attr(0640,apache,apache) %{_sysconfdir}/%{name}/RT_*.pm

%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%dir %{_datadir}/%{name}
%{RT_WWWDIR}
%{RT_LEXDIR}
%{RT_FONTSDIR}
%{RT_STATICDIR}

%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf

%dir %{RT_CACHEDIR}
%attr(0770,apache,apache) %{RT_CACHEDIR}/mason_data
%attr(0770,apache,apache) %{RT_CACHEDIR}/session_data

%files mailgate
%license COPYING
%{_bindir}/rt-mailgate
%{_mandir}/man1/rt-mailgate*

%if %{with devel_mode}
%files tests
%dir %{perl_testdir}
%{perl_testdir}/%{name}
# Does not work outside of the source tree
%exclude %{perl_testdir}/%{name}/t/pod.t
# Required by t/shredder/*t
%{_sysconfdir}/%{name}/*.SQLite

%files -n perl-RT-Test
%license COPYING
%dir %{RT_LIBDIR}/RT
%{RT_LIBDIR}/RT/Test*
%endif

%changelog
* Sat May 4 2019  Nico Kadel-Garcia <nkadel@gmail.com> - 4.4.4-0
- Update to 4.4.4
- Obsolete rt4 packages as well as rt3 packages

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 24 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.3-2
- Change permissions on /etc/rt/RT_SiteConfig.d to 0750 (RHBZ#1652560).

* Sun Jul 22 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.3-1
- Update to rt-4.4.3.
- Modernize spec.
- BR: perl(File::Find), perl(HTTP::Status).
- Rebase patches.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.4.2-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.2-1
- Update to rt-4.4.2.

* Wed Jul 26 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.1-9
- Add missing %%patch6.

* Wed Jul 26 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.1-8
- Add 0006-Apply-security-2017-06-15-rt-4.4.1.patch.patch (RHBZ#1475084).
  Supposed to address CVE-2016-6127, CVE-2017-5361, CVE-2017-5943,
  CVE-2017-5944.
- Update README.fedora.

* Thu Jun 15 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.4.1-7
- Perl 5.26 rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.4.1-6
- Perl 5.26 re-rebuild of bootstrapped packages

* Wed Mar 15 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.1-5
- Fix testsuite failure in t/web/cf_groupings.t caused by Mojolicious >= 7.0
  incompatibilty (Add 0005-Fix-tests-for-Mojolicious-7.0.patch).

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.1-3
- Add R: perl(Data::Page) and R: perl(Data::Page::Pageset) (RHBZ#1415825).

* Tue Dec 20 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.1-2
- Add perl(Net::LDAP::Server::Test).

* Thu Jul 28 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.1-1
- Update to rt-4.4.1.
- Reflect upstream URLs having changed.
- Add man-pages for rt-importer, rt-serializer, rt-validate-aliases,
  rt-externalize-attachments.
- Rebase patches.
- Update README.fedora.in.
- Misc. spec file massaging.

* Mon May 30 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.0-2
- Rebuild for perl-5.24 (RHBZ#1339296).

* Fri Feb 26 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.0-1
- Update to rt-4.4.0.
- Rebase patches.
- Update deps.
- Update README.fedora.in.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.2.12-1
- Update to rt-4.2.12.
- Rebase 0001-Remove-configure-time-generated-files.patch.

* Tue Aug 04 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.2.11-2
- Install README* directly into %%_pkgdocdir (Work-around regression introduced
  by rpm-4.12.90 (RHBZ#1249716).

* Wed Jun 17 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.2.11-1
- Update to 4.2.11.
- Rebase patches.
- Install devel/docs.

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 4.2.10-3
- Perl 5.22 rebuild

* Tue Mar 24 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.2.10-2
- Update patches.
- R: perl(Time::ParseDate).
- Add docs symlink.
- Add %%license.
- Spec cleanup.

* Mon Mar 09 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 4.2.10-1
- Update to 4.2.10.
- Remove 0001-Remove-configure-time-generated-files.patch and delete the files
  directly instead; the patch would require a complete rebase any time any of
  those files changes.
- Remove 0008-Adjust-path-to-html-autohandler.patch and
  0009-Work-around-testsuite-failure.patch as they have been upstreamed.
- Adjust to new filenames in /usr/share/rt/upgrade.

* Tue Jan 27 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.2.9-2
- Remove --with/without gpg.
- Remove --with/without gd.
- Remove --with/without graphviz.

* Mon Jan 26 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.2.9-1
- Update to rt-4.2.9.
