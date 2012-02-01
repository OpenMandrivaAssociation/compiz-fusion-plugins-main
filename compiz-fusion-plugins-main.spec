%define name compiz-fusion-plugins-main
%define newname compiz-plugins-main
%define version 0.8.6
%define rel 3
%define git 0

%if %{git}
%define srcname plugins-main-%{git}.tar.lzma
%define distname plugins-main
%define release %mkrel 0.%{git}.%{rel}
%else
%define srcname %{newname}-%{version}.tar.bz2
%define distname %{newname}-%{version}
%define release %mkrel %{rel}
%endif


Summary: Compiz Fusion Main Plugin Set for compiz
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{srcname}
Patch1:  0001-Use-appropriate-animation-for-screenlets.patch
Patch2:  0002-Use-a-more-Mandriva-y-blue-for-expo.patch
License: GPL
Group: System/X11
URL: http://www.compiz-fusion.org/
BuildRoot: %{_tmppath}/%{newname}-%{version}-%{release}-buildroot
BuildRequires: dbus-devel
BuildRequires: compiz-devel >= %{version}
BuildRequires: gettext-devel
BuildRequires: intltool
BuildRequires: compiz-bcop
BuildRequires: libGConf2-devel
BuildRequires: MesaGLU-devel
BuildRequires: jpeg-devel
BuildRequires: pango-devel
Requires: compiz

Obsoletes: compiz-extra
Obsoletes: beryl-plugins
#Obsoletes: compiz-fusion-plugins-main
#Provides: compiz-fusion-plugins-main

%description
This is the main plugin set from the Compiz Fusion community.

This is a combination of the Compiz Extras and Beryl communities

#----------------------------------------------------------------------------

%package devel
Summary: Development files for Compiz Fusion Main Plugin Set for compiz
Group: Development/X11
#Obsoletes: compiz-fusion-plugins-main-devel
#Provides: compiz-fusion-plugins-main-devel

%description devel
Development files for Compiz Fusion Main Plugin Set for compiz

#----------------------------------------------------------------------------

%prep
%setup -q -n %{distname}
%patch1 -p1
%patch2 -p1

%build
%if %{git}
  # This is a CVS snapshot, so we need to generate makefiles.
  sh autogen.sh -V
%endif
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name *.la -exec rm -f {} \;
%find_lang %{newname}

%clean
rm -rf %{buildroot}

#----------------------------------------------------------------------------

%files -f %{newname}.lang
%defattr(-,root,root)
%{_libdir}/compiz/lib*.a
%{_libdir}/compiz/lib*.so
%{_datadir}/compiz/*.xml
%dir %{_datadir}/compiz/filters
%{_datadir}/compiz/filters/*
%{_datadir}/compiz/*/*.png


%files devel
%{_includedir}/compiz/*.h
%{_libdir}/pkgconfig/*.pc





%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-3mdv2011.0
+ Revision: 663395
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-2mdv2011.0
+ Revision: 603847
- rebuild

* Sun May 02 2010 Colin Guthrie <cguthrie@mandriva.org> 0.8.6-1mdv2010.1
+ Revision: 541654
- New version: 0.8.6

* Sat Mar 13 2010 Colin Guthrie <cguthrie@mandriva.org> 0.8.4-2mdv2010.1
+ Revision: 518615
- Rebuild for new Compiz

* Thu Oct 15 2009 Colin Guthrie <cguthrie@mandriva.org> 0.8.4-1mdv2010.0
+ Revision: 457733
- New version: 0.8.4
- Harden buildrequires versions

* Wed Sep 09 2009 Colin Guthrie <cguthrie@mandriva.org> 0.8.2-4mdv2010.0
+ Revision: 434888
- Rebuild against updated compiz

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-3mdv2010.0
+ Revision: 416648
- rebuilt against libjpeg v7

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-2mdv2010.0
+ Revision: 413264
- rebuild

* Sun Mar 15 2009 Emmanuel Andry <eandry@mandriva.org> 0.8.2-1mdv2009.1
+ Revision: 355370
- keep the old name for the moment, needs a package renaming
- New version 0.8.2
- remove fusion from name

* Sun Feb 08 2009 Colin Guthrie <cguthrie@mandriva.org> 0.8.0-0.20090208.1mdv2009.1
+ Revision: 338487
- 0.8 pre-release snapshot

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 0.7.8-1mdv2009.1
+ Revision: 319153
- rediff animation-screenlets.patch as properly named animation_screenlets.patch
- 0.7.8 final

* Fri Sep 12 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.8-0.20080912.1mdv2009.0
+ Revision: 284297
- New snapshot
- Update animation/screenlets patch

* Sun Jul 13 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.7-0.20080713.1mdv2009.0
+ Revision: 234345
- New snapshot
- New version: 0.7.6

* Fri May 23 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.5-0.20080522.1mdv2009.0
+ Revision: 210159
- Update to git snapshot
- Drop upstream applied patch

* Fri May 02 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.4-2mdv2009.0
+ Revision: 200083
- Apply upstream patch to fix panels not appearing after login

* Tue Apr 08 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.4-1mdv2009.0
+ Revision: 192372
- New version 0.7.4

* Fri Mar 07 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.2-1mdv2008.1
+ Revision: 181136
- Fix the animation/screenlets patch to include the options too.
- New version 0.7.2

* Mon Feb 18 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6.99-0.20080218.1mdv2008.1
+ Revision: 172297
- Update to git master for new compiz

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 28 2007 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-2mdv2008.1
+ Revision: 102769
- Fix certain window types from being handled incorrectly (upstream diff).

* Sat Oct 20 2007 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 100721
- New upstream release: 0.6.0

* Fri Oct 19 2007 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-0.20071018.1mdv2008.1
+ Revision: 100099
- Update snapshot from 0.6.0 branch for compiz 0.6.2

* Mon Sep 17 2007 Colin Guthrie <cguthrie@mandriva.org> 0.5.2-4mdv2008.0
+ Revision: 88949
- Make reflections colours fit in better with default Mandriva theme.

* Sun Sep 16 2007 Colin Guthrie <cguthrie@mandriva.org> 0.5.2-3mdv2008.0
+ Revision: 88520
- Add default animations for Screenlets windows.

* Tue Sep 04 2007 Colin Guthrie <cguthrie@mandriva.org> 0.5.2-2mdv2008.0
+ Revision: 79534
- Rebuild for latest compiz (patch removal caused ABI change)

* Mon Aug 13 2007 Colin Guthrie <cguthrie@mandriva.org> 0.5.2-1mdv2008.0
+ Revision: 62614
- Official Release: 0.5.2

* Sun Aug 12 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.20070811.1mdv2008.0
+ Revision: 62121
- Update snapshot

* Wed Aug 01 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.20070801.1mdv2008.0
+ Revision: 57838
- Updated snapshot

* Wed Jul 25 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.20070725.1mdv2008.0
+ Revision: 55252
- Update Snapshot

* Sat Jul 14 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.20070714.1mdv2008.0
+ Revision: 52117
- Update snapshot

* Sun Jul 08 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.20070707.1mdv2008.0
+ Revision: 49609
- Require compiz
- Update Snapshot to 20070707
- Obsolete Beryl Plugins and Compiz Extra
- Import compiz-fusion-main

