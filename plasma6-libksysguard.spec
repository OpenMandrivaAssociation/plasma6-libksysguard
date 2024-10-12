%define devname %mklibname KF6Libksysguard -d
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

%define ksgrd_major 10
%define libksgrd %mklibname KSysGuardSystemStats
%define processcore_major 10
%define libprocesscore %mklibname processcore
%define formatter_major 2
%define libformatter %mklibname KSysGuardFormatter
%define sensorfaces_major 2
%define libsensorfaces %mklibname KSysGuardSensorFaces
%define sensors_major 2
%define libsensors %mklibname KSysGuardSensors
# Removed in 6.0
%define oldlibksgrd %mklibname ksgrd
%define libksignalplotter %mklibname ksignalplotter
%define liblsofui %mklibname lsofui
%define libprocessui %mklibname processui
%define desname %mklibname KF6Libksysguard-designer -d

Name: plasma6-libksysguard
Version:	6.2.0
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/libksysguard/-/archive/%{gitbranch}/libksysguard-%{gitbranchd}.tar.bz2#/libksysguard-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/libksysguard-%{version}.tar.xz
%endif
Summary: KDE Frameworks 6 system monitoring framework
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6WebEngineCore)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(zlib)
BuildRequires: cmake(Qt6Designer)
BuildRequires: cmake(Qt6Sensors)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Plasma) >= 5.90.0
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(libpcap)
BuildRequires: pkgconfig(libcap)
BuildRequires: lm_sensors-devel
BuildRequires: gettext

Requires: kf6-kquickcharts
Requires: %{libksgrd} = %{EVRD}
Requires: %{libprocesscore} = %{EVRD}
Requires: %{libformatter} = %{EVRD}
Requires: %{libsensorfaces} = %{EVRD}
Requires: %{libsensors} = %{EVRD}
Obsoletes: %{libksignalplotter} < %{EVRD}
Obsoletes: %{liblsofui} < %{EVRD}
Obsoletes: %{libprocessui} < %{EVRD}

%description
KDE Frameworks 6 system monitoring framework.

%files -f ksgrd.lang
%{_datadir}/qlogging-categories6/libksysguard.categories
%{_datadir}/dbus-1/interfaces/org.kde.ksystemstats1.xml
%{_libdir}/libexec/kf6/kauth/ksysguardprocesslist_helper
%dir %{_libdir}/libexec/ksysguard
%caps(cap_net_raw+ep) %{_libdir}/libexec/ksysguard/ksgrd_network_helper
%{_datadir}/dbus-1/system.d/org.kde.ksysguard.processlisthelper.conf
%{_datadir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
%{_qtdir}/qml/org/kde/ksysguard
%{_qtdir}/plugins/kf6/packagestructure/ksysguard_sensorface.so
%{_datadir}/knsrcfiles/systemmonitor-faces.knsrc
%{_datadir}/knsrcfiles/systemmonitor-presets.knsrc
%{_datadir}/ksysguard/sensorfaces
%{_datadir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy
%dir %{_qtdir}/plugins/ksysguard
%dir %{_qtdir}/plugins/ksysguard/process
%{_qtdir}/plugins/ksysguard/process/ksysguard_plugin_network.so
%{_qtdir}/plugins/ksysguard/process/ksysguard_plugin_nvidia.so

#----------------------------------------------------------------------------

%package -n %{libksgrd}
Summary: Plasma 6 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}
%rename %{oldlibksgrd}

%description -n %{libksgrd}
Plasma 6 KDE System Guard shared library.

%files -n %{libksgrd}
%{_libdir}/libKSysGuardSystemStats.so.2
%{_libdir}/libKSysGuardSystemStats.so.6*

#----------------------------------------------------------------------------

%package -n %{libprocesscore}
Summary: Plasma 6 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libprocesscore}
Plasma 6 KDE System Guard shared library.

%files -n %{libprocesscore}
%{_libdir}/libprocesscore.so.%{processcore_major}
%{_libdir}/libprocesscore.so.6*

#----------------------------------------------------------------------------

%package -n %{libformatter}
Summary: Plasma 6 KDE System Guard formatting library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libformatter}
Plasma 6 KDE System Guard formatting shared library.

%files -n %{libformatter}
%{_libdir}/libKSysGuardFormatter.so.%{formatter_major}
%{_libdir}/libKSysGuardFormatter.so.6*

#----------------------------------------------------------------------------

%package -n %{libsensorfaces}
Summary: Plasma 6 KDE System Guard sensor faces shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libsensorfaces}
Plasma 6 KDE System Guard sensor faces shared library.

%files -n %{libsensorfaces}
%{_libdir}/libKSysGuardSensorFaces.so.%{sensorfaces_major}
%{_libdir}/libKSysGuardSensorFaces.so.6*

#----------------------------------------------------------------------------

%package -n %{libsensors}
Summary: Plasma 6 KDE System Guard sensors shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libsensors}
Plasma 6 KDE System Guard sensors shared library.

%files -n %{libsensors}
%{_libdir}/libKSysGuardSensors.so.%{sensors_major}
%{_libdir}/libKSysGuardSensors.so.6*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary: Development files for the KDE Frameworks 6 system monitoring library
Group: Development/KDE and Qt
Requires: %{libksgrd} = %{EVRD}
Requires: %{libprocesscore} = %{EVRD}
Requires: %{libformatter} = %{EVRD}
Requires: %{libsensorfaces} = %{EVRD}
Requires: %{libsensors} = %{EVRD}
Obsoletes: %{desname} < %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 6 system monitoring library.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KSysGuard

%prep
%autosetup -p1 -n libksysguard-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang ksgrd --all-name --with-html
