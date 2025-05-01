Name:           borshevik-control-center
Version:        48.1
Release:        1%{?dist}.borshevik
Summary:        GNOME's main interface to configure various aspects of the desktop (Borshevik Edition)

License:        GPLv2+
URL:            https://gitlab.gnome.org/GNOME/gnome-control-center
Source0:        https://download.gnome.org/sources/gnome-control-center/48/gnome-control-center-%{version}.tar.xz

Patch0:         borshevik-logo.patch
Patch1:         enable-vrr-default.patch
Patch2:         enable-fractional-scaling-default.patch

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gtk4-devel
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  libgnomekbd-devel
BuildRequires:  libnma-devel
BuildRequires:  libwacom-devel
BuildRequires:  libsecret-devel
BuildRequires:  libgtop2-devel
BuildRequires:  accountsservice-devel
BuildRequires:  systemd-devel
BuildRequires:  libxml2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  itstool
BuildRequires:  libadwaita-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libpwquality-devel

Requires:       gsettings-desktop-schemas
Requires:       adwaita-icon-theme

Provides:       gnome-control-center = %{version}-%{release}
Conflicts:      gnome-control-center

%description
This is a patched version of GNOME Control Center customized for Borshevik OS branding.
Includes modified ID-to-logo mapping and distro-specific appearance patches.

%prep
%autosetup -p1
%patch 1 -p1
%patch 2 -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/gnome-control-center
%{_datadir}/applications/org.gnome.Settings.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/gnome-control-center.*
%{_datadir}/gnome-control-center/

%changelog
- Add branding patch to recognize ID=borshevik and load custom logo icon
- Enable VRR by default
- Enable fractional scaling by default
- Initial release for Borshevik OS
