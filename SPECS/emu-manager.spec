Name:           xcp-emu-manager
Version:        0.0.3
Release:        1.3
Summary:        Tool used for managing xenguest
License:        LGPL
URL:            https://github.com/xcp-ng/xcp-emu-manager
Source0:        https://github.com/xcp-ng/xcp-emu-manager/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         xcp-emu-manager-0.0.3-fix-migrate-of-loaded-vms.XCP-ng.patch
Patch1:         xcp-emu-manager-0.0.3-wait-for-xenguest-migr-compl-msg-in-slct-loop.XCP-ng.patch
Patch2:         xcp-emu-manager-0.0.3-end-live-migr-stage-at-end-of-first-iteration.patch
BuildRequires:  make
BuildRequires:  xs-opam-repo

Provides:	emu-manager
Obsoletes:	emu-manager

%description
Simple host networking management service for the xapi toolstack.

Handles suspend, resume and migrate.

%prep
%autosetup -p1

%build
eval $(opam config env --root=/usr/lib/opamroot)
make

%install
make install DESTDIR=%{buildroot} BINDIR=%{_libdir}/xen/bin

%files
%{_libdir}/xen/bin/emu-manager

%changelog
* Mon Nov 19 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 0.0.3-1.3
- Live migration fixes

* Thu Nov 08 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 0.0.3-1.2
- Backport patch to improve migration of loaded VMs.
- In most cases migration will now resume when the VM's CPU and/or IO usage decreases.

* Thu Jul 23 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 0.0.3-1
- Update to 0.0.3 with migration support!

* Mon Jul 23 2018 John Else <john.else@gmail.com> - 0.0.2-1
- Initial package
