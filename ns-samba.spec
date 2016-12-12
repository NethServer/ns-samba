%define sambaver 4.5.2

Name:           ns-samba
Version: 1.0.1
Release: 1%{?dist}
Summary:        Samba vanilla build

License: GPLv3+
URL: %{url_prefix}/%{name}
Source0: %{name}-%{version}.tar.gz
Source1: https://download.samba.org/pub/samba/stable/samba-%{sambaver}.tar.gz  

BuildRequires: nethserver-devtools
BuildRequires: python-devel
BuildRequires: systemd-devel
BuildRequires: gnutls-devel
BuildRequires: docbook-xsl
BuildRequires: libacl-devel
BuildRequires: openldap-devel

BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
This is is a vanilla samba-%{sambaver} build for NethServer 7

%prep
%setup 
%setup -D -T -b 1

%build
cd %{_builddir}/samba-%{sambaver} 
%configure --with-systemd --enable-fhs 
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

(cd root ; find . -depth -print | cpio -dump %{buildroot})

pushd %{_builddir}/samba-%{sambaver}
%make_install
popd

%{genfilelist} %{buildroot} > %{name}-%{version}.filelist

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

