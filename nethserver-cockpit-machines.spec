Summary: nethserver-cockpit-machines  is to create VM with libvirt inside cockpit
%define name nethserver-cockpit-machines
Name: %{name}
%define version 0.1.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Requires: cockpit-machines
Requires: virt-install
Requires: qemu-kvm
Requires: libvirt
Requires: libvirt-daemon-kvm
Requires: libvirt-dbus
Requires: libvirt-glib
BuildRequires: nethserver-devtools
BuildArch: noarch

%description
Use Cockpit to create and manage virtual machines

%prep

%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
> %{name}-%{version}-%{release}-filelist

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING

%changelog
* Sun Jan 10 2021 stephane de Labrusse <stephdl@de-labrusse.fr>
- initial commit
