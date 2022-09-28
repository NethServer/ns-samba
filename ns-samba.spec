Name: ns-samba
Version: 4.16.5
Release: 1%{?dist}
Summary: Samba vanilla build

License: GPLv3+
URL: %{url_prefix}/%{name}
Source0: %{name}-%{version}.tar.gz
Source1: https://download.samba.org/pub/samba/stable/samba-%{version}.tar.gz

# Turn off the brp-python-bytecompile automagic
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

BuildRequires: nethserver-devtools
BuildRequires: python36-devel python36-markdown python36-dns
BuildRequires: systemd-devel
BuildRequires: compat-gnutls37-devel
BuildRequires: docbook-xsl
BuildRequires: libacl-devel
BuildRequires: openldap-devel
BuildRequires: pam-devel
BuildRequires: jansson-devel
BuildRequires: gpgme-devel
BuildRequires: libarchive-devel
BuildRequires: zlib-devel
BuildRequires: perl-Parse-Yapp  perl-JSON
BuildRequires: popt-devel

BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: bind-utils
Requires: python36-dns

%description
This is is a vanilla samba-%{version} build for NethServer 7

%prep
%setup 
%setup -q -D -T -b 1

%build
export LANG=en_US.UTF-8
cd %{_builddir}/samba-%{version}
%configure --with-systemd --enable-fhs --without-ldb-lmdb --with-shared-modules='!vfs_snapper'
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

(cd root ; find . -depth -print | cpio -dump %{buildroot})

pushd %{_builddir}/samba-%{version}
%make_install
popd

%{genfilelist} %{buildroot} | grep -v -e '.pyo$' -e '.pyc$' > %{name}-%{version}.filelist

%files -f %{name}-%{version}.filelist
%defattr(-,root,root)
%doc COPYING
%dir /var/lib/samba
%config(noreplace) %ghost %{_sysconfdir}/samba/smb.conf

%post
%systemd_post samba.service

%preun
%systemd_preun samba.service

%postun
%systemd_postun

%changelog
* Wed Sep 28 2022 Davide Principi <davide.principi@nethesis.it> - 4.16.5-1
- Bump version 4.16.5

* Fri Apr 17 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 4.11.7-1
- Bump version 4.11.7

* Tue Feb  4 2020 Davide Principi <davide.principi@nethesis.it> - 4.9.18-1
- Bump version 4.9.18

* Thu Sep 19 2019 Davide Principi <davide.principi@nethesis.it> - 4.9.13-1
- Bump version 4.9.13

* Wed May 15 2019 Davide Principi <davide.principi@nethesis.it> - 4.8.12-1
- Bump version 4.8.12

* Mon Feb 18 2019 Davide Principi <davide.principi@nethesis.it> - 4.8.9-1
- Bump version 4.8.9

* Fri Feb  1 2019 Davide Principi <davide.principi@nethesis.it> - 4.8.8-1
- Bump version 4.8.8

* Mon Nov 12 2018 Davide Principi <davide.principi@nethesis.it> - 4.8.6-1
- Bump version 4.8.6

* Mon Sep  3 2018 Davide Principi <davide.principi@nethesis.it> - 4.7.10-1
- Bump version 4.7.10

* Mon Sep  3 2018 Davide Principi <davide.principi@nethesis.it> - 4.7.9-1
- Bump version 4.7.9

* Tue Jun 26 2018 Davide Principi <davide.principi@nethesis.it> - 4.7.8-1
- Bump version 4.7.8

* Thu Apr 26 2018 Davide Principi <davide.principi@nethesis.it> - 4.7.7-1
- Bump version 4.7.7

* Mon Apr 16 2018 Davide Principi <davide.principi@nethesis.it> - 4.7.6-1
- Bump version 4.7.6

* Thu Mar 15 2018 Davide Principi <davide.principi@nethesis.it> - 4.6.14-1
- Bump version 4.6.14

* Mon Jan 15 2018  Davide Principi <davide.principi@nethesis.it> - 4.6.12-1
- Bump version 4.6.12

* Fri Dec 01 2017 Davide Principi <davide.principi@nethesis.it> - 4.6.11-1
- Bump version 4.6.11

* Fri Oct 13 2017 Davide Principi <davide.principi@nethesis.it> - 4.6.8-1
- Bump version 4.6.8

* Fri Oct 06 2017 Davide Principi <davide.principi@nethesis.it> - 4.7.0-1
- Bump version 4.7.0
 
* Mon Jun 26 2017 Davide Principi <davide.principi@nethesis.it> - 4.6.5-1
- Bump version 4.6.5

* Wed May 24 2017 Davide Principi <davide.principi@nethesis.it> - 4.6.4-1
- Bump version 4.6.4

* Wed May 03 2017 Davide Principi <davide.principi@nethesis.it> - 4.6.3-1
- Bump version 4.6.3

* Mon Apr 10 2017 Davide Principi <davide.principi@nethesis.it> - 4.6.2-1
- Bump version 4.6.2

* Fri Mar 24 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 4.6.0-1
- Bump version 4.6.0

* Mon Dec 12 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Bump version 4.5.2

* Thu Jul 07 2016 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1
- Bump version 4.4.5

* Tue May 17 2016 Davide Principi <davide.principi@nethesis.it>
- Bump Samba 4.4.3

* Mon Apr 11 2016 Davide Principi <davide.principi@nethesis.it>
- Bump Samba 4.3.6

* Wed Jan 27 2016 Davide Principi <davide.principi@nethesis.it>
- Initial build
