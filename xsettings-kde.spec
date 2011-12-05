
Summary: XSettings Daemon for KDE
Name:    xsettings-kde
Version: 0.11
Release: 1%{?dist}	
License: GPLv2+
Group:   User Interface/Desktops 
# upstream is a svn
Source0:  %{name}-%{version}-20090829svn.tar.bz2
Source1:  xsettings-kde-%{version}-svn_checkout.sh
URL: http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/theme/xsettings-kde/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# fedora doesn't use ~/.kde4 like mandriva
Patch1: xsettings-kde-0.9-kde4.patch

Source10: xsettings-kde.desktop

BuildRequires: glib2-devel
BuildRequires: libX11-devel

%description
This package provides a XSettings daemon for KDE Desktop Environment.
It allows XSettings aware applications (all GTK+ 2 and GNOME 2 applications)
to be informed instantly of changes in KDE configuration, such as theme name,
default font and so on.


%prep
%setup -q

%patch1 -p1 -b .kde4


%build

make %{?_smp_mflags} CFLAGS="%{optflags}" lib=%{_lib}


%install
rm -rf %{buildroot}

install -p -m755 -D  xsettings-kde %{buildroot}%{_bindir}/xsettings-kde

install -p -m644 -D %{SOURCE10} \
  %{buildroot}%{_datadir}/autostart/xsettings-kde.desktop


%clean
rm -rf %{buildroot}


%files 
%defattr(-,root,root,-)
%doc ChangeLog README COPYING
%{_bindir}/*
%{_datadir}/autostart/*


%changelog
* Sat Aug 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.11-1
- xsettings-0.11

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.10-1
- xsettings-0.10

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 30 2008 Rex Dieter <rdieter@fedoraproject.org> 0.9-1
- resurrect latest kde4-enabled version, yay.

* Sun Jan 27 2008 Manuel Wolfshant <wolfy@fedoraproject.org> 0.6-3
- small fixes

* Sun Dec 30 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.6-2
- fedora-ize

* Wed Sep 26 2007 Frederic Crozat <fcrozat@mandriva.com> 0.6-1mdv2008.0
+ Revision: 93073
- Release 0.6 :
 -failover correctly when some configuration files aren't present

* Fri Sep 21 2007 Frederic Crozat <fcrozat@mandriva.com> 0.5-1mdv2008.0
+ Revision: 91946
- Release 0.5
 - handle multiple kde profiles specified as prefixes

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.com> 0.4-2mdv2008.0
+ Revision: 76611
- rebuild for 2008
- don't package COPYING
- Import xsettings-kde

* Wed Sep 13 2006 Frederic Crozat <fcrozat@mandriva.com> 0.4-1mdv2007.0
- Release 0.4 :
 * change theme according to color scheme for Ia Ora (Mdv bug #25574)
 * fix theme detection
 * support kde profile
 * don't change theme if ~/.gtkrc-2.0 exists

* Mon Mar 06 2006 Frederic Crozat <fcrozat@mandriva.com> 0.3-1mdk
- Release 0.3 :
 - support Net/FallbackIconTheme, fix Mdk bug #19441)

* Thu Aug 25 2005 Frederic Crozat <fcrozat@mandriva.com> 0.2-1mdk 
- Release 0.2 :
 - force gnome-vfs gtk2 file selector backend

* Wed Jul 27 2005 Frederic Crozat <fcrozat@mandriva.com> 0.1-1mdk 
- Initial package
