%define __noautoprov 'pkgconfig(.*)'
%define __noautoreq 'pkgconfig\\(compiz\\)'

%define oname compiz-plugins-main

Name:		compiz-fusion-plugins-main
Version:	0.8.8
Release:	2
Summary:	Compiz Fusion Main Plugin Set for compiz
License:	GPLv2
Group:		System/X11
URL:		http://www.compiz.org/
Source0:	http://releases.compiz.org/components/plugins-main/%{oname}-%{version}.tar.bz2
Patch1:		0001-Use-appropriate-animation-for-screenlets.patch
Patch2:		0002-Use-a-more-Mandriva-y-blue-for-expo.patch
# From Debian and Fedora
Patch3:		compiz-plugins-main_fix_edges.patch
BuildRequires:	intltool
BuildRequires:	compiz0.8-bcop
BuildRequires:	compiz0.8-devel
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(pango)
Requires:	compiz0.8
Conflicts:	compiz > 0.9

%description
This is the main plugin set from the Compiz Fusion community.

This is a combination of the Compiz Extras and Beryl communities

%files -f %{oname}.lang
%{_libdir}/compiz/lib*.so
%{_datadir}/compiz/*.xml
%dir %{_datadir}/compiz/filters
%{_datadir}/compiz/filters/*
%{_datadir}/compiz/*/*.png

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for Compiz Fusion Main Plugin Set for compiz
Group:		Development/X11
Requires:	compiz0.8-devel
Conflicts:	compiz-devel > 0.9

%description devel
Development files for Compiz Fusion Main Plugin Set for compiz

%files devel
%{_includedir}/compiz/*.h
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -fi
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%find_lang %{oname}

