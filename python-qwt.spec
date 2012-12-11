%define module PyQwt
%define version 5.2.0
%define rel 6

Name:         python-qwt
Version:      %{version}
Release:      %mkrel %rel
Url:	      http://pyqwt.sourceforge.net/
License:      GPLv2+
Group:        Development/Python
Summary:      Python bindings for Qwt (Qt Widgets for Technical applications)
Source0:      http://belnet.dl.sourceforge.net/sourceforge/pyqwt/%{module}-%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Provides:     PyQwt = %{version}-%{release}
Requires:     python-qt4
Requires:     python-sip
Requires:     python-numeric
Requires:     python-numarray
Requires:     python-numpy
%py_requires -d
BuildRequires: libqwt-devel >= 5.2.0
BuildRequires: python-numeric-devel
BuildRequires: python-numarray-devel
BuildRequires: python-numpy-devel
BuildRequires: python-qt4
BuildRequires: python-sip

%description
Qwt is an extension to the Qt GUI library. The Qwt library contains
widgets and components which are primarily useful for technical and
scientifical purposes. It includes a 2-D plotting widget, different
kinds of sliders, and much more.

PyQwt has almost all functionality of the Qwt library implemented.

%prep
%setup -q -n %{module}-%{version}

%build
cd configure
python configure.py %_smp_mflags --extra-cflags="%{optflags}" --extra-cxxflags="%{optflags}" \
	--extra-lflags="%{?ldflags}" --extra-libs="python%{py_ver}"
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std -C configure

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ANN* qt4examples
%{py_platsitedir}/*
%_datadir/sip/PyQt4/Qwt5/*


%changelog
* Sat Dec 25 2010 Funda Wang <fwang@mandriva.org> 5.2.0-6mdv2011.0
+ Revision: 624725
- rebuild

* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 5.2.0-5mdv2011.0
+ Revision: 593995
- rebuild for py2.7

* Wed Sep 01 2010 Funda Wang <fwang@mandriva.org> 5.2.0-4mdv2011.0
+ Revision: 575042
- rebuild for new python-sip

* Thu Jul 15 2010 Funda Wang <fwang@mandriva.org> 5.2.0-3mdv2011.0
+ Revision: 553452
- rebuild for new python-sip

* Sun Jun 27 2010 Ahmad Samir <ahmadsamir@mandriva.org> 5.2.0-2mdv2010.1
+ Revision: 549214
- rebuild for new python-sip (mdv #59940)

* Wed Dec 23 2009 Funda Wang <fwang@mandriva.org> 5.2.0-1mdv2010.1
+ Revision: 481769
- new version 5.2.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 5.1.0-3mdv2009.1
+ Revision: 324117
- fix linkage

* Tue Jun 03 2008 Funda Wang <fwang@mandriva.org> 5.1.0-2mdv2009.0
+ Revision: 214469
- use optflags

* Mon Jun 02 2008 Funda Wang <fwang@mandriva.org> 5.1.0-1mdv2009.0
+ Revision: 214338
- really fix the file list
- fix spec file list
- New version 5.1.0

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Thu Aug 10 2006 glehmann
+ 08/10/06 19:39:22 (55496)
fix build on x!86_64

* Sun Jul 30 2006 glehmann
+ 07/30/06 10:27:03 (42702)
Import python-qwt

* Tue Jul 26 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 4.2-2mdk
- build on x86_64
- drop libqwt requirement
- spec cleanup
- buildrequires sip-devel

* Tue Mar 29 2005 Gaetan Lehmann <glehmann@n4.mandrakesoft.com> 4.2-1mdk
- initial contrib

