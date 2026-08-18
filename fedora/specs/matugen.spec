%global debug_package %{nil}

Name:               matugen
Version:        4.2.0
Release:        202608180031%{?dist}
Summary:            A cross-platform material you and base16 color generation tool

License:            GPL-2.0
URL:                https://github.com/InioX/matugen
Source0:            %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  rust-packaging
BuildRequires:  cargo
BuildRequires:  gcc

%description
A cross-platform material you and base16 color generation tool

%prep
%autosetup -n %{name}-%{version} -p1

%build
cargo build --release

%install
install -Dm0755 target/release/matugen %{buildroot}%{_bindir}/matugen

%files
%license LICENSE
%doc README.md
%{_bindir}/matugen

%changelog
%autochangelog
