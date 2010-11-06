%define module PyQwt
%define version 5.2.0
%define rel 5

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
