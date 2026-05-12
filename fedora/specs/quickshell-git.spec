# Original-Spec: https://copr-dist-git.fedorainfracloud.org/packages/errornointernet/quickshell/quickshell-git.git/plain/quickshell-git.spec?h=master
%global debug_package %{nil}
%bcond_with         asan

%global commit      7d1c9a9c6721606b129829134d6f614f015621e2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commits     818
%global snapdate    20260511
%global tag         0.3.0

Name:               quickshell-git
Version:            %{tag}^%{commits}.git%{shortcommit}
Release:            0%{?dist}
Summary:            Flexible QtQuick based desktop shell toolkit

License:            LGPL-3.0-only AND GPL-3.0-only
URL:                https://github.com/quickshell-mirror/quickshell
Source0:            %{url}/archive/%{commit}/quickshell-%{shortcommit}.tar.gz

Conflicts:          quickshell <= %{tag}


%if 0%{fedora} >= 43
BuildRequires:      breakpad-static
%endif
BuildRequires:      cmake
BuildRequires:      cmake(Qt6Core)
BuildRequires:      cmake(Qt6Qml)
BuildRequires:      cmake(Qt6ShaderTools)
BuildRequires:      cmake(Qt6WaylandClient)
BuildRequires:      gcc-c++
BuildRequires:      ninja-build
BuildRequires:      pkgconfig(breakpad)
BuildRequires:      pkgconfig(CLI11)
BuildRequires:      pkgconfig(gbm)
BuildRequires:      pkgconfig(glib-2.0)
BuildRequires:      pkgconfig(jemalloc)
BuildRequires:      pkgconfig(libdrm)
BuildRequires:      pkgconfig(libpipewire-0.3)
BuildRequires:      pkgconfig(pam)
BuildRequires:      pkgconfig(polkit-agent-1)
BuildRequires:      pkgconfig(wayland-client)
BuildRequires:      pkgconfig(wayland-protocols)
BuildRequires:      cpptrace
BuildRequires:      qt6-qtbase-private-devel
BuildRequires:      spirv-tools

Requires: qt6-qtdeclarative
Requires: qt6-qtbase
Requires: jemalloc
Requires: qt6-qtsvg
Requires: pipewire-libs
Requires: libxcb
Requires: wayland-devel
Requires: qt6-qtwayland
Requires: qt5-qtwayland
Requires: libdrm
Requires: breakpad
Requires: kf6-kirigami
Requires: libunwind-devel
Requires: qt6-qt5compat
Requires: qt6-qtimageformats
Requires: qt6-qtpositioning
Requires: qt6-qtquicktimeline
Requires: qt6-qtsensors
Requires: qt6-qttools
Requires: qt6-qttranslations
Requires: qt6-qtvirtualkeyboard
Requires: kdialog
Requires: kf6-syntax-highlighting

%if %{with asan}
BuildRequires:      libasan
%endif

Provides:           desktop-notification-daemon

%description
Flexible toolkit for making desktop shells with QtQuick, targeting
Wayland and X11.

%prep
%autosetup -n quickshell-%{commit} -p1

%build
%cmake  -GNinja \
%if %{with asan}
        -DASAN=ON \
%endif
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_BUILD_TYPE=Release \
        -DGIT_REVISION=%{commit} \
        -DINSTALL_QML_PREFIX=%{_lib}/qt6/qml
%cmake_build

%install
%cmake_install



%files
%license LICENSE
%license LICENSE-GPL
%doc BUILD.md
%doc CONTRIBUTING.md
%doc README.md
%doc changelog/v%{tag}.md
%{_bindir}/qs
%{_bindir}/quickshell


%{_datadir}/applications/org.quickshell.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.quickshell.svg
%{_libdir}/qt6/qml/Quickshell




%changelog
%autochangelog
