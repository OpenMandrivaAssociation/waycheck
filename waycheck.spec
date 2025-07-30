%define	oname Waycheck

Summary:	Display information for Wayland compositors
Name:	waycheck
Version:	1.7.0
Release:	1 
License: Apache-2.0
Group: System/X11/Wayland
Url: https://gitlab.freedesktop.org/serebit/waycheck
Source0: https://gitlab.freedesktop.org/serebit/waycheck/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
#BuildRequires: qt6-tools
BuildRequires:	meson >= 0.59.0
BuildRequires:ninja
BuildRequires: pkgconfig(Qt6Core) >= 6.5
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6WaylandClient)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(wayland-client) >= 1.17

%description
Waycheck is a simple Qt6 application that displays all of the Wayland
protocols that your compositor supports, and all of the protocols that
it doesn't support.

%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/dev.serebit.%{oname}.desktop
%{_datadir}/icons/hicolor/*/apps/dev.serebit.%{oname}.svg
%{_datadir}/metainfo/dev.serebit.%{oname}.metainfo.xml

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-v%{version}


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


