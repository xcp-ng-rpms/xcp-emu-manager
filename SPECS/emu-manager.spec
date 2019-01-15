Name:           xcp-emu-manager
Version:        0.0.3
Release:        1.4
Summary:        Tool used for managing xenguest
License:        LGPL
URL:            https://github.com/xcp-ng/xcp-emu-manager
Source0:        https://github.com/xcp-ng/xcp-emu-manager/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-ignore-progress-messages-from-xenguest-when-exp-a-resp.patch
Patch1:         0002-wait-for-xenguest-migr-compl-msg-in-slct-loop.patch
Patch2:         0003-end-live-migr-stage-at-end-of-first-iteration.patch
Patch3:         0004-Open-a-Debug-module.patch
Patch4:         0005-Add-logging.patch
Patch5:         0006-Log-failures.patch
Patch6:         0007-Rework-live-save-completion-loop.patch
Patch7:         0008-Log-a-completion-message-or-an-error-message-and-bac.patch
BuildRequires:  make
BuildRequires:  xs-opam-repo
BuildRequires:  ocaml-xcp-idl-devel

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
* Tue Jan 15 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 0.0.3-1.4
- More live migration fixes, backported from XCP-ng 7.6

* Mon Nov 19 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 0.0.3-1.3
- Live migration fixes

* Thu Nov 08 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 0.0.3-1.2
- Backport patch to improve migration of loaded VMs.
- In most cases migration will now resume when the VM's CPU and/or IO usage decreases.

* Mon Jul 23 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 0.0.3-1
- Update to 0.0.3 with migration support!

* Mon Jul 23 2018 John Else <john.else@gmail.com> - 0.0.2-1
- Initial package
