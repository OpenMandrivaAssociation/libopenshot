%define major	16
%define libname	%mklibname openshot %{major}
%define devname	%mklibname openshot -d

%define with_ruby	0

Name:		libopenshot
Version:	0.2.2
Release:	2
Summary:	Library for creating and editing videos
License:	LGPLv3+
Group:		System/Libraries
URL:		http://www.openshot.org/
Source0:	https://github.com/OpenShot/libopenshot/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		libopenshot-0.2.2-fix-build-with-imagemagick7.patch

BuildRequires:	cmake
BuildRequires:  qmake5
BuildRequires:	cppzmq-devel
BuildRequires:  pkgconfig(libzmq)
BuildRequires:	doxygen
BuildRequires:	swig
BuildRequires:	ffmpeg-devel
%if %{with_ruby}
BuildRequires:	pkgconfig(ruby)
%endif
BuildRequires:	libopenshot-audio-devel >= 0.1.4
BuildRequires:	pkgconfig(ImageMagick) >= 7.0
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(UnitTest++)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5MultimediaWidgets)

%description
OpenShot Library (libopenshot) is an open-source project
dedicated to delivering high quality video editing, animation,
and playback solutions to the world. For more information
visit <http://www.openshot.org/>.

#----------------------------------------------------

%package -n	%{libname}
Summary:	OpenShot Library
Group:		System/Libraries

%description -n	%{libname}
OpenShot Library (libopenshot) is an open-source project
dedicated to delivering high quality video editing, animation,
and playback solutions to the world. For more information
visit <http://www.openshot.org/>.
This package contains library files for %{name}.

#----------------------------------------------------

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	openshot-devel = %{version}-%{release}

%description -n	%{devname}
The %{devname} package contains libraries and header files for
developing applications that use %{name}.

#----------------------------------------------------

%package -n	python-%{name}
Summary:	Python 3 bindings for %{name}
Group:		Development/Python

%description -n	python-%{name}
The python-%{name} package contains python 3 bindings for
applications that use %{name}.

#----------------------------------------------------
%if %{with_ruby}
%package -n	ruby-%{name}
Summary:	Ruby bindings for %{name}
Group:		Development/Ruby

%description -n	ruby-%{name}
The ruby-%{name} package contains ruby bindings for
applications that use %{name}.
%endif
#----------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files -n %{libname}
%{_libdir}/libopenshot.so.%{major}
%{_libdir}/libopenshot.so.%{version}

%files -n %{devname}
%doc AUTHORS COPYING README
%{_includedir}/%{name}/
%{_libdir}/libopenshot.so

%files -n python-%{name}
%doc AUTHORS COPYING README
%{python3_sitearch}/*

%if %{with_ruby}
%files -n ruby-%{name}
%{ruby_vendorarchdir}/*
%endif
