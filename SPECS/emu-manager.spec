Name:           xcp-emu-manager
Version:        0.0.2
Release:        1
Summary:        Tool used for managing xenguest
License:        LGPL
URL:            https://github.com/xcp-ng/xcp-emu-manager
Source0:        https://github.com/xcp-ng/xcp-emu-manager/archive/v%{version}/%{name}-%{version}.tar.gz
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
* Mon Jul 23 2018 John Else <john.else@gmail.com> - 0.0.2-1
- Initial package
