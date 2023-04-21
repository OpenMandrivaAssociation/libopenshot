%define _disable_ld_no_undefined 1
%define major	25
%define libname	%mklibname openshot %{major}
%define devname	%mklibname openshot -d

%define with_ruby	1

Name:		libopenshot
Version:	0.3.2
Release:	1
Summary:	Library for creating and editing videos
License:	LGPLv3+
Group:		System/Libraries
URL:		http://www.openshot.org/
Source0:	https://github.com/OpenShot/libopenshot/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		libopenshot-0.3.0-c++17.patch

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:  qmake5
BuildRequires:	cppzmq-devel
BuildRequires:	doxygen
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(babl-0.1) >= 0.1.100
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(opencv4)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:	swig
BuildRequires:	ffmpeg-devel
%if %{with_ruby}
BuildRequires:	pkgconfig(ruby)
%endif
BuildRequires:	openshot-audio-devel >= 0.3.0
BuildRequires:	pkgconfig(ImageMagick) >= 7.0
BuildRequires:	pkgconfig(python)
#BuildRequires:	pkgconfig(UnitTest++)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(zlib)

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
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	openshot-devel = %{EVRD}

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
%autosetup -p1
%cmake .. -DENABLE_TESTS=1 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libopenshot.so.%{major}
%{_libdir}/libopenshot.so.%{version}
#{_libdir}/libopenshot_protobuf.so.%{version}
#{_libdir}/libopenshot_protobuf.so.%{major}


%files -n %{devname}
%doc AUTHORS
%{_includedir}/%{name}/
%{_libdir}/libopenshot.so
#{_libdir}/libopenshot_protobuf.so

%files -n python-%{name}
%doc AUTHORS
%{python3_sitearch}/*

%if %{with_ruby}
%files -n ruby-%{name}
%{ruby_vendorarchdir}/*
%endif
