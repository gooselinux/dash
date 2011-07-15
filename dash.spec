Name:           dash
Version:        0.5.5.1
Release:        3.1%{?dist}
Summary:        Small and fast POSIX-compliant shell

Group:          System Environment/Shells
License:        BSD
URL:            http://gondor.apana.org.au/~herbert/dash/
Source0:        http://gondor.apana.org.au/~herbert/dash/files/dash-%{version}.tar.gz
Patch0:         dash-do-not-close-stderr.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
DASH is a POSIX-compliant implementation of /bin/sh that aims to be as small as
possible. It does this without sacrificing speed where possible. In fact, it is
significantly faster than bash (the GNU Bourne-Again SHell) for most tasks.

%prep
%setup -q
%patch0 -p 1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin
mv $RPM_BUILD_ROOT%{_bindir}/dash $RPM_BUILD_ROOT/bin/
rm -rf $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
/bin/dash
%{_datadir}/man/man1/dash.1.gz

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.5.5.1-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Andreas Thienemann <andreas@bawue.net> - 0.5.5.1-2
- Added patch from upstream git to not close stdout on err. This improves
  initramfs use of dash.

* Mon Apr 13 2009 Warren Togami <wtogami@redhat.com> - 0.5.5.1-1
- 0.5.5.1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 08 2008 Warren Togami <wtogami@redhat.com> 0.5.4-3
- rebuild for gcc-4.3

* Wed Nov 07 2007 Warren Togami <wtogami@redhat.com> 0.5.4-2
- move to /bin/dash
- BSD license tag

* Fri Nov 02 2007 Warren Togami <wtogami@redhat.com> 0.5.4-1
- initial package


