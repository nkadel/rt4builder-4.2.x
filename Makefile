#
# Makefile - build wrapper for Rt 4 on RHEL 6
#
#	git clone RHEL 7 SRPM building tools from
#	https://github.com/nkadel/rt4repo

# Base directory for yum repository
REPOBASE=file://$(PWD)
#REPOBASE=http://localhost

REPOS+=rt4repo/el/7
REPOS+=rt4repo/fedora/29
REPOS+=rt4repo/fedora/30
REPOS+=rt4repo/fedora/rawhide

REPODIRS := $(patsubst %,%/x86_64,$(REPOS)) $(patsubst %,%/SRPMS,$(REPOS))

# These build with normal mock "epel-*" setups
EPELPKGS+=google-droid-sans-fonts-srpm
EPELPKGS+=perl-Apache-DBI-srpm
EPELPKGS+=perl-Authen-Simple-srpm
EPELPKGS+=perl-CGI-PSGI-srpm
EPELPKGS+=perl-CPAN-Meta-YAML-srpm
EPELPKGS+=perl-CSS-Minifier-XS-srpm
EPELPKGS+=perl-CSS-Minifier-srpm
EPELPKGS+=perl-Cache-Simple-TimedExpiry-srpm
EPELPKGS+=perl-Calendar-Simple-srpm
EPELPKGS+=perl-Capture-Tiny-srpm
EPELPKGS+=perl-Carp-Assert-More-srpm
EPELPKGS+=perl-Class-Accessor-Chained-srpm
EPELPKGS+=perl-Class-Accessor-Lite-srpm
EPELPKGS+=perl-Class-Accessor-srpm
EPELPKGS+=perl-Class-Container-srpm
EPELPKGS+=perl-Class-ReturnValue-srpm
EPELPKGS+=perl-Crypt-Eksblowfish-srpm
EPELPKGS+=perl-Crypt-X509-srpm
EPELPKGS+=perl-DBIx-DBschema-srpm
EPELPKGS+=perl-Data-GUID-srpm
EPELPKGS+=perl-Data-ICal-srpm
EPELPKGS+=perl-Data-Page-srpm
EPELPKGS+=perl-Digest-JHash-srpm
EPELPKGS+=perl-Email-Address-List-srpm
EPELPKGS+=perl-Email-Address-srpm
EPELPKGS+=perl-Encode-srpm
EPELPKGS+=perl-Expect-Simple-srpm
EPELPKGS+=perl-GDGraph-srpm
EPELPKGS+=perl-GnuP{G-Interface-srpm
EPELPKGS+=perl-HTML-FormatText-WithLinks-AndTables-srpm
EPELPKGS+=perl-HTTP-Parser-XS-srpm
EPELPKGS+=perl-IPC-Run-SafeHandles-srpm
EPELPKGS+=perl-JSON-PP-srpm
EPELPKGS+=perl-List-UtilsBy-srpm
EPELPKGS+=perl-Locale-Maketext-Fuzzy-srpm
EPELPKGS+=perl-Locale-Maketext-Lexicon-srpm
EPELPKGS+=perl-Log-Dispatch-Perl-srpm
EPELPKGS+=perl-Module-Util-srpm
EPELPKGS+=perl-Net-DNS-Lite-srpm
EPELPKGS+=perl-Net-LDAP-SID-srpm
EPELPKGS+=perl-Net-LDAP-Server-srpm
EPELPKGS+=perl-PadWalker-srpm
EPELPKGS+=perl-PerlIO-eol-srpm
EPELPKGS+=perl-Proc-Wait3-srpm
EPELPKGS+=perl-Regexp-Common-Net-CIDR-srpm
EPELPKGS+=perl-Role-Basic-srpm
EPELPKGS+=perl-Scope-Guard-srpm
EPELPKGS+=perl-Scope-Upper-srpm
EPELPKGS+=perl-Set-IntSpan-srpm
EPELPKGS+=perl-Set-Tiny-srpm
EPELPKGS+=perl-String-RewritePrefix-srpm
EPELPKGS+=perl-Symbol-Global-Name-srpm
EPELPKGS+=perl-Test-CheckManifest-srpm
EPELPKGS+=perl-Test-HTTP-Server-Simple-srpm
EPELPKGS+=perl-Test-Log-Dispatch-srpm
EPELPKGS+=perl-Test-SharedFork-srpm
EPELPKGS+=perl-Test-Simple-srpm
EPELPKGS+=perl-Text-Password-Pronounceable-srpm
EPELPKGS+=perl-Text-Quoted-srpm
EPELPKGS+=perl-Text-WikiFormat-srpm
EPELPKGS+=perl-Text-Wrapper-srpm
EPELPKGS+=perl-URI-srpm
EPELPKGS+=perl-accessors-srpm
EPELPKGS+=perl-capitalization-srpm
EPELPKGS+=perl-inc-latest-srpm
EPELPKGS+=publicsuffixlist-srpm

# Require customized rt4repo local repository for dependencies
# Needed by various packages

RT4PKGS+=perl-Authen-Simple-Passwd-srpm
RT4PKGS+=perl-Business-Hours-srpm
RT4PKGS+=perl-CPAN-Meta-srpm

RT4PKGS+=perl-Data-Page-Pageset-srpm

RT4PKGS+=perl-DateTime-Format-Natural-srpm
RT4PKGS+=perl-Date-Extract-srpm

# Now requires perl-Cache-Simple-TimedExpiry-srpm
RT4PKGS+=perl-DBIx-SearchBuilder-srpm

# Now requires perl-Test-CheckManifest-srpm
RT4PKGS+=perl-Hash-MoreUtils-srpm

# Dependencies for perl-Test-Harness-srpm
RT4PKGS+=perl-TAP-Formatter-HTML-srpm
RT4PKGS+=perl-Test-Harness-srpm
# Dependendencies for perl-Module-Build-srpm
RT4PKGS+=perl-Module-Build-srpm
RT4PKGS+=perl-Module-Build-Deprecated-srpm
RT4PKGS+=perl-JavaScript-Minifier-XS-srpm

RT4PKGS+=perl-Net-LDAP-Server-srpm

RT4PKGS+=perl-Test-WWW-Mechanize-srpm

# Dependencies for perl-Test-TCP-srpm
RT4PKGS+=perl-Test-TCP-srpm

# Dependencies for perl-CHI
RT4PKGS+=perl-Module-Mask-srpm
RT4PKGS+=perl-CHI-srpm

RT4PKGS+=perl-Convert-Color-srpm

# Dependencies for perl-Module-Util-srpm
RT4PKGS+=perl-TAP-Formatter-HTML-srpm
RT4PKGS+=perl-Module-Util-srpm

# Dependency for perl-Data-ICal-srpm
RT4PKGS+=perl-Text-vFile-asData-srpm
RT4PKGS+=perl-Data-ICal-srpm

# Dependency for perl-HTML-Mason-PSGIHandler-srpm
RT4PKGS+=perl-HTML-Mason-srpm
RT4PKGS+=perl-HTML-Mason-PSGIHandler-srpm

RT4PKGS+=perl-HTML-Quoted-srpm
RT4PKGS+=perl-HTML-RewriteAttributes-srpm

#Dependencies for perl-HTTP-CookieHar-srpm
RT4PKGS+=perl-Mozilla-PublicSuffix-srpm
# Dependencies for perl-Furl-srpm
RT4PKGS+=perl-HTTP-CookieJar-srpm
RT4PKGS+=perl-HTTP-Server-Simple-Mason-srpm
# Dependencies for perl-File-Dropbox-srpm
RT4PKGS+=perl-Furl-srpm
RT4PKGS+=perl-File-Dropbox-srpm

RT4PKGS+=perl-Net-LDAP-Server-Test-srpm

# Dependency for perl-Parallel-Prefork-srpm
RT4PKGS+=perl-Parallel-Scoreboard-srpm
RT4PKGS+=perl-Parallel-Prefork-srpm

RT4PKGS+=perl-Plack-Middleware-Test-StashWarnings-srpm

RT4PKGS+=perl-Regexp-IPv6-srpm
RT4PKGS+=perl-Server-Starter-srpm
RT4PKGS+=perl-Starlet-srpm

RT4PKGS+=perl-Test-Expert-srpm

RT4PKGS+=perl-Test-HTTP-Server-Simple-StashWarnings-srpm

# Needed for rt4-Test building
RT4PKGS+=perl-Test-WWW-Mechanize-PSGI-srpm

RT4PKGS+=perl-Tree-Simple-srpm

# Binary target
RT4PKGS+=rt-srpm

# Add-on utilities, can be compiled with rt3 from EPEL,
# but use rt4 from local builds
RT4PKGS+=perl-RT-Client-REST-srpm
RT4PKGS+=perl-RT-Extension-CommandByMail-srpm
RT4PKGS+=perl-RT-Extension-MandatoryFields-srpm

# Set up config files for local rt4repo and mock
all:: cfg

all:: dirs

# Populate rt4repo with packages compatible with just EPEL
all:: epel-install

# Populate rt4repo with packages that require rt4repo
all:: rt4-install

install:: cfg epel-install rt4-install

.FORCE: cfg
cfg:: epel-7-x86_64.cfg
cfg:: fedora-30-x86_64.cfg
cfg:: rt4repo-7-x86_64.cfg
cfg:: rt4repo-f30-x86_64.cfg

epel-7-x86_64.cfg:: /etc/mock/epel-7-x86_64.cfg
	ln -sf $? $@

fedora-30-x86_64.cfg:: /etc/mock/fedora-30-x86_64.cfg
	ln -sf $? $@

rt4repo-7-x86_64.cfg: epel-7-x86_64.cfg
	@echo Generating $@ from $?
	@cat $? > $@
	@sed -i 's/epel-7-x86_64/rt4repo-7-x86_64/g' $@
	@echo '"""' >> $@
	@echo >> $@
	@echo '[rt4repo]' >> $@
	@echo 'name=rt4repo' >> $@
	@echo 'enabled=1' >> $@
	@echo 'baseurl=$(REPOBASE)/rt4repo/el/7/x86_64/' >> $@
	@echo 'failovermethod=priority' >> $@
	@echo 'skip_if_unavailable=False' >> $@
	@echo 'metadata_expire=3' >> $@
	@echo 'gpgcheck=0' >> $@
	@echo '#cost=2000' >> $@
	@echo '"""' >> $@
	@uniq -u $@ > $@.out
	@mv $@.out $@

rt4repo-f30-x86_64.cfg: fedora-30-x86_64.cfg
	@echo Generating $@ from $?
	@cat $? > $@
	@sed -i 's/fedora-30-x86_64/rt4repo-f30-x86_64/g' $@
	@echo '"""' >> $@
	@echo >> $@
	@echo '[rt4repo]' >> $@
	@echo 'name=rt4repo' >> $@
	@echo 'enabled=1' >> $@
	@echo 'baseurl=$(REPOBASE)/rt4repo/fedora/30/x86_64/' >> $@
	@echo 'failovermethod=priority' >> $@
	@echo 'skip_if_unavailable=False' >> $@
	@echo 'metadata_expire=3' >> $@
	@echo 'gpgcheck=0' >> $@
	@echo '#cost=2000' >> $@
	@echo '"""' >> $@
	@uniq -u $@ > $@.out
	@mv $@.out $@

# Used for make build with local components
rt4repo.repo:: rt4repo.repo.in
	sed "s|@@@REPOBASE@@@|$(REPOBASE)|g" $? > $@

rt4repo.repo:: FORCE
	@cmp -s $@ /etc/yum.repos.d/$@ || \
		(echo Warning: /etc/yum.repos.d/$@ does not match $@, exiting; exit 1)

epel:: cfg
epel:: $(EPELPKGS)

dirs:: $(REPODIRS)
$(REPODIRS)::
	install -d -m 755 $@
	createrepo -q $@

epel-install:: $(REPODIRS)

epel-install:: FORCE
	@for name in $(EPELPKGS); do \
		(cd $$name && $(MAKE) all install) || exit 1; \
	done

rt4:: cfg
rt4:: $(RT4PKGS)

rt4-install:: FORCE
	@for name in $(RT4PKGS); do \
		(cd $$name && $(MAKE) all install) || exit 1; \
	done

# Dependencies
perl-Authen-Simple-Passwd-srpm:: perl-Authen-Simple-srpm
perl-Business-Hours-srpm:: perl-Set-IntSpan-srpm
perl-CHI-srpm:: perl-Digest-JHash-srpm
perl-CHI-srpm:: perl-Hash-MoreUtils-srpm
perl-CHI-srpm:: perl-Log-Any-Adapter-Dispatch-srpm
perl-CHI-srpm:: perl-Log-Any-Adapter-srpm
perl-CHI-srpm:: perl-Module-Mask-srpm
perl-CHI-srpm:: perl-String-RewritePrefix-srpm
perl-CHI-srpm:: perl-Test-Log-Dispatch-srpm
perl-CPAN-Meta-srpm:: perl-CPAN-Meta-YAML-srpm
perl-CPAN-Meta-srpm:: perl-JSON-PP-srpm
perl-DateTime-Format-Natural-srpm:: perl-Module-Util-srpm
perl-Date-Extract-srpm:: perl-DateTime-Format-Natural-srpm
perl-Class-Accessor-Lite-srpm:: perl-Cache-Simple-TimedExpiry-srpm
perl-Convert-Color-srpm:: perl-List-UtilsBy-srpm
perl-DBIx-SearchBuilder-srpm:: perl-Cache-Simple-TimedExpiry-srpm
perl-DBIx-SearchBuilder-srpm:: perl-capitalization-srpm
perl-Data-ICal-srpm:: perl-Class-ReturnValue-srpm
perl-Data-ICal-srpm:: perl-Text-vFile-asData-srpm
perl-Devel-StackTrace-WithLexicals-srpm:: perl-PadWalker-srpm
perl-Furl-srpm:: perl-HTTP-CookieJar-srpm
perl-Furl-srpm:: perl-HTTP-Parser-XS-srpm
perl-Furl-srpm:: perl-HTTP-Server-Simple-Mason-srpm
perl-Furl-srpm:: perl-Net-DNS-Lite-srpm
perl-HTML-Mason-PSGIHandler-srpm:: perl-HTML-Mason-srpm
perl-HTML-Mason-PSGIHandler-srpm:: perl-Test-Log-Dispatch-srpm
perl-HTML-Mason-srpm:: perl-Class-Container-srpm
perl-HTTP-CookieJar-srpm:: perl-Mozilla-PublicSuffix-srpm
perl-Hash-MoreUtils-srpm:: perl-Test-CheckManifest-srpm
perl-Log-Any-Aapter-srpm:: perl-Log-Any-srpm
perl-Log-Any-Adapter-Dispatch-srpm:: perl-Log-Any-Adapter-srpm
perl-Module-Build-srpm:: perl-inc-latest-srpm
perl-Module-Mask-srpm:: perl-Module-Util-srpm
perl-Mozilla-PublicSuffix-srpm:: publicsuffixlist-srpm
perl-Net-LDAP-Server-Test-srpm:: perl-Net-LDAP-SID-srpm
perl-Net-LDAP-Server-Test-srpm:: perl-Net-LDAP-Server-srpm
perl-Parallel-Prefork-srpm:: perl-Class-Accessor-Lite-srpm
perl-Parallel-Prefork-srpm:: perl-Parallel-Scoreboard-srpm
perl-Parallel-Scoreboard-srpm:: perl-Class-Accessor-Lite-srpm
perl-Server-Starter-srpm:: perl-Encode-srpm
perl-Server-Starter-srpm:: perl-Proc-Wait3-srpm
perl-Starlet-srpm:: perl-Parallel-Prefork-srpm
perl-Starlet-srpm:: perl-Server-Starter-srpm
perl-TAP-Formatter-HTML-srpm:: perl-accessors-srpm
perl-Test-Expert-srpm:: perl-Class-Accessor-Chained-srpm
perl-Test-Expert-srpm:: perl-Expect-Simple-srpm
perl-Test-HTTP-Server-Simple-StashWarnings-srpm:: perl-Test-HTTP-Server-Simple-srpm
perl-Test-TCP-srpm:: perl-Test-SharedFork-srpm
perl-Test-TCP-srpm:: perl-Test-Simple-srpm
perl-Test-WWW-Mechanize-PSGI-srpm:: perl-Test-WWW-Mechanize-srpm
perl-Test-WWW-Mechanize-srpm:: perl-Carp-Assert-More-srpm
perl-Text-vFile-asData-srpm:: perl-Class-Accessor-Chained-srpm
perl-Tree-Simple-srpm:: perl-Test-Simple-srpm

rt4:: google-droid-sans-fonts-srpm
rt4:: perl-CGI-PSGI-srpm
rt4:: perl-Calendar-Simple-srpm
rt4:: perl-Class-Accessor-srpm
rt4:: perl-Class-ReturnValue-srpm
rt4:: perl-Convert-Color-srpm
rt4:: perl-DBIx-DBschema-srpm
rt4:: perl-DBIx-SearchBuilder-srpm
rt4:: perl-Encode-srpm
rt4:: perl-GnuP{G-Interface-srpm
rt4:: perl-HTML-Mason-PSGIHandler-srpm
rt4:: perl-HTML-Mason-srpm
rt4:: perl-HTML-Quoted-srpm
rt4:: perl-HTML-RewriteAttributes-srpm
rt4:: perl-HTTP-Server-Simple-Mason-srpm
rt4:: perl-IPC-Run-SafeHandles-srpm
rt4:: perl-JavaScript-Minifier-XS-srpm
rt4:: perl-Locale-Maketext-Fuzzy-srpm
rt4:: perl-Locale-Maketext-Lexicon-srpm
rt4:: perl-Log-Dispatch-Perl-srpm
rt4:: perl-Plack-Middleware-Test-StashWarnings-srpm
rt4:: perl-Regexp-IPv6-srpm
rt4:: perl-Role-Basic-srpm
rt4:: perl-Symbol-Global-Name-srpm
rt4:: perl-Test-Expert-srpm
rt4:: perl-Test-HTTP-Server-Simple-srpm
rt4:: perl-Text-Password-Pronounceable-srpm
rt4:: perl-Text-Quoted-srpm
rt4:: perl-Text-WikiFormat-srpm
rt4:: perl-Text-Wrapper-srpm
rt4:: perl-Text-vFile-asData-srpm

perl-RT-Client-REST-srpm:: rt-srpm
perl-RT-Extension-CommandByMail:: rt-srpm
perl-RT-Extension-MandatoryFields:: rt-srpm

# Git clone operations, not normally required
# Targets may change

# Build EPEL compatible softwaer in place
$(EPELPKGS):: FORCE
	(cd $@ && $(MAKE) $(MLAGS)) || exit 1

$(RT4PKGS):: rt4repo-6-x86_64.cfg
$(RT4PKGS):: rt4repo-7-x86_64.cfg

$(RT4PKGS):: FORCE
	(cd $@ && $(MAKE) $(MLAGS)) || exit 1

# Needed for local compilation, only use for dev environments
build:: rt4repo.repo

build clean realclean distclean:: FORCE
	@for name in $(EPELPKGS) $(RT4PKGS); do \
	     (cd $$name && $(MAKE) $(MFLAGS) $@); \
	done

realclean distclean:: clean

clean::
	find . -name \*~ -exec rm -f {} \;

# Use this only to build completely from scratch
# Leave the rest of rt4repo alone.
maintainer-clean:: clean
	@echo Clearing local yum repository
	find rt4repo -type f ! -type l -exec rm -f {} \; -print

# Leave a safe repodata subdirectory
maintainer-clean:: FORCE

safe-clean:: maintainer-clean FORCE
	@echo Populate rt4repo with empty, safe repodata
	find rt4repo -noleaf -type d -name repodata | while read name; do \
		createrepo -q $$name/..; \
	done

# This is only for upstream repository publication.
# Modify for local use as needed, but do try to keep passwords and SSH
# keys out of the git repository fo this software.
RSYNCTARGET=rsync://localhost/rt4repo
RSYNCOPTS=-a -v --ignore-owner --ignore-group --ignore-existing
RSYNCSAFEOPTS=-a -v --ignore-owner --ignore-group
publish:: all
publish:: FORCE
	@echo Publishing RPMs to $(RSYNCTARGET)
	rsync $(RSYNCSAFEOPTS) --exclude=repodata $(RSYNCTARGET)/

publish:: FORCE
	@echo Publishing repodata to $(RSYNCTARGET)
	find repodata/ -type d -name repodata | while read name; do \
	     rsync $(RSYNCOPTS) $$name/ $(RSYNCTARGET)/$$name/; \
	done

FORCE::
