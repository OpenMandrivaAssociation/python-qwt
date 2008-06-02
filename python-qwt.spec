
%define module PyQwt
%define version 5.1.0
%define release 1

%define sipfiles /usr/share/sip

Name:         python-qwt
Version:      %{version}
Release:      %mkrel %release
Url:	      http://pyqwt.sourceforge.net/
License:      GPLv2+
Group:        Development/Python
Summary:      Python bindings for Qwt (Qt Widgets for Technical applications)
Source0:      http://belnet.dl.sourceforge.net/sourceforge/pyqwt/%{module}-%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Provides:     PyQwt = %{version}-%{release}
Requires:     python
Requires:     PyQt
Requires:     sip
Requires:     python-numeric
Requires:     python-numarray
BuildRequires: python-devel
BuildRequires: libqwt-devel
BuildRequires: python-numeric-devel
BuildRequires: python-numarray-devel
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
python configure.py -I %{qt4include}/qwt
%make

%install
rm -rf $RPM_BUILD_ROOT

(
cd configure
make install DESTDIR=$RPM_BUILD_ROOT
)
# install PyCute
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp examples/PyCute $RPM_BUILD_ROOT/%{_bindir}

# will create dangling symlinks
unlink examples/iqt
unlink examples/qwt

%if "%{_lib}" == "lib64"
mv $RPM_BUILD_ROOT/%{_prefix}/lib $RPM_BUILD_ROOT/%{_libdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{py_platsitedir}/*
%sipfiles
%doc ANN* AUTHORS COPYING* DIFFER INSTALL MANIFEST* PATCHER README* REGIS* THANKS examples Doc/html

