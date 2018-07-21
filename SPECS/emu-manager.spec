Name:           emu-manager
Version:        0.0.1
Release:        1%{?dist}
Summary:        Used for managing xenguest
License:        LGPL
URL:            https://github.com/xcp-ng/xcp-emu-manager
Source0:        https://github.com/xcp-ng/xcp-emu-manager/archive/v%{version}/emu-manager-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  xs-opam-repo

%{?systemd_requires}

%description
Simple host networking management service for the xapi toolstack.

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
* Fri Jul 20 2018 John Else <john.else@gmail.com> - 0.0.1-1
- Initial package
