%define sambaver 4.3.4

Name:           ns-samba
Version:        0.0.0
Release:        1%{?dist}
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
* Wed Jan 27 2016 Davide Principi <davide.principi@nethesis.it>
- Initial build

