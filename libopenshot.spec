%define _disable_ld_no_undefined 1
%define major	33
%define oldlibname %mklibname openshot 25
%define libname	%mklibname openshot
%define devname	%mklibname openshot -d

%define with_ruby	1

Name:		libopenshot
Version:	1.1.0
Release:	1
Summary:	Library for creating and editing videos
License:	LGPLv3+
Group:		System/Libraries
URL:		https://www.openshot.org/
Source0:	https://github.com/OpenShot/libopenshot/archive/v%{version}/%{name}-%{version}.tar.gz
# Local helpers named lerp() clash with std::lerp once libstdc++ math.h
# imports it. Cooker builds this tree as C++20.
Patch0:		libopenshot-1.1.0-lerp.patch

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	doxygen
BuildRequires:	pkgconfig(babl-0.1) >= 0.1.100
BuildRequires:	pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(opencv5)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:	swig
BuildRequires:	ffmpeg-devel
%if %{with_ruby}
BuildRequires:	pkgconfig(ruby)
%endif
BuildRequires:	openshot-audio-devel >= 1.0.2
# OpenShotAudioConfig.cmake calls find_dependency(ALSA).
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(python3)
BuildRequires:  python%{pyver}dist(setuptools)
#BuildRequires:	pkgconfig(UnitTest++)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(libpipewire-0.3)
BuildRequires:	pkgconfig(libspa-0.2)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
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
%rename		%{oldlibname}

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
%cmake \
	-DENABLE_MAGICK=OFF \
	-DENABLE_TESTS=OFF \
	-DUSE_QT6=ON \
	-G Ninja

%build
export LD_LIBRARY_PATH=$(pwd)/build/src:$LD_LIBRARY_PATH
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libopenshot.so.%{major}
%{_libdir}/libopenshot.so.%{version}
%{_libdir}/libopenshot-wayland-capture.so
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
