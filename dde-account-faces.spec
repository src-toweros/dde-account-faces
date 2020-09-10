Name:           dde-account-faces
Version:        1.0.11
Release:        1
Summary:        Account faces for Linux Deepin
License:        GPLv2+
URL:            https://github.com/linuxdeepin/dde-account-faces
Source0:        https://github.com/linuxdeepin/dde-account-faces/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:  	accountsservice
Conflicts: 	deepin-system-settings-module-account

%description
Account faces for Linux Deepin

%prep
%setup -q -n %{name}-%{version}

%build

%install
%make_install

%files
%{_sharedstatedir}/AccountsService/icons/*

%changelog
* Thu Sep 10 2020 chenbo pan <panchenbo@uniontech.com> - 1.0.11-1
- Initial package build
