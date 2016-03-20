%global revdate 20150831

Name:           publicsuffix-list
Version:        %{revdate}
#Release:        1%{?dist}
Release:        0.1%{?dist}
Summary:        Cross-vendor public domain suffix database

License:        MPLv2.0
URL:            https://publicsuffix.org/
Source0:        https://publicsuffix.org/list/public_suffix_list.dat
Source1:        https://www.mozilla.org/MPL/2.0/index.txt
Source2:        https://github.com/publicsuffix/list/raw/master/tests/test_psl.txt

BuildArch:      noarch


%description
The Public Suffix List is a cross-vendor initiative to provide
an accurate list of domain name suffixes, maintained by the hard work 
of Mozilla volunteers and by submissions from registries.
Software using the Public Suffix List will be able to determine where 
cookies may and may not be set, protecting the user from being 
tracked across sites.


%prep
%setup -c -T
# https://github.com/publicsuffix/list/pull/21
sed -i -e "s/'c.il\,/'c.il'\,/" %{SOURCE2}
cp -av %{SOURCE1} COPYING


%build


%install
install -m 644 -p -D %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/publicsuffix/public_suffix_list.dat
install -m 644 -p -D %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/publicsuffix/test_psl.txt
ln -s public_suffix_list.dat $RPM_BUILD_ROOT/%{_datadir}/publicsuffix/effective_tld_names.dat


%files
%license COPYING
%{_datadir}/publicsuffix


%changelog
* Sat Mar 19 2016 Nico Kadel-Garcia <nkadel@gmail.com> - 20150831-0.1
- Backport to RHEL 7

* Tue Sep  1 2015 Yanko Kaneti <yaneti@declera.com> - 20150831-1
- The latest revision - 20150831
- Add test data - bug 1251921

* Mon Aug  3 2015 Yanko Kaneti <yaneti@declera.com> - 20150731-1
- The latest revision - 20150731
- Move to the new upstream filename. Install a compat symlink for now

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150506-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May  7 2015 Yanko Kaneti <yaneti@declera.com> - 20150506-1
- The latest revision - 20150506

* Thu Apr 30 2015 Yanko Kaneti <yaneti@declera.com> - 20150430-1
- The latest revision - 20150430

* Tue Apr  7 2015 Yanko Kaneti <yaneti@declera.com> - 20150407-1
- The latest revision - 20150407

* Sat Apr  4 2015 Yanko Kaneti <yaneti@declera.com> - 20150404-1
- The latest revision - 20150404

* Thu Feb 26 2015 Yanko Kaneti <yaneti@declera.com> - 20150226-1
- The latest revision - 20150226

* Wed Feb 18 2015 Yanko Kaneti <yaneti@declera.com> - 20150217-1
- The latest revision - 20150217

* Thu Feb  5 2015 Yanko Kaneti <yaneti@declera.com> - 20150204-1
- The latest revision - 20150204

* Tue Dec 30 2014 Yanko Kaneti <yaneti@declera.com> - 20141230-1
- Initial version for review - 20141124-1
- Today's revision. Add license file - 20141218-1
- Today's revision - 20141223-1
- Today's revision - 20141230-1
