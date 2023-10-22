%define devname %mklibname KF6Libksysguard -d
%define desname %mklibname KF6Libksysguard-designer -d
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define git 20231023

%define ksgrd_major 10
%define libksgrd %mklibname ksgrd
%define ksignalplotter_major 10
%define libksignalplotter %mklibname ksignalplotter
%define lsofui_major 10
%define liblsofui %mklibname lsofui
%define processcore_major 10
%define libprocesscore %mklibname processcore
%define processui_major 10
%define libprocessui %mklibname processui
%define formatter_major 2
%define libformatter %mklibname KSysGuardFormatter
%define sensorfaces_major 2
%define libsensorfaces %mklibname KSysGuardSensorFaces
%define sensors_major 2
%define libsensors %mklibname KSysGuardSensors

Name: plasma6-libksysguard
Version:	5.240.0
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/libksysguard/-/archive/master/libksysguard-master.tar.bz2#/libksysguard-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
%endif
Patch0:	libksysguard-bump-sonames.patch
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
BuildRequires: cmake(KF6Plasma)
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
# Prevent pulling in Plasma 5
BuildRequires: plasma6-xdg-desktop-portal-kde

Requires: kf6-kquickcharts
Requires: %{libksgrd} = %{EVRD}
Requires: %{libksignalplotter} = %{EVRD}
Requires: %{liblsofui} = %{EVRD}
Requires: %{libprocesscore} = %{EVRD}
Requires: %{libprocessui} = %{EVRD}
Requires: %{libformatter} = %{EVRD}
Requires: %{libsensorfaces} = %{EVRD}
Requires: %{libsensors} = %{EVRD}

%description
KDE Frameworks 6 system monitoring framework.

%files -f ksgrd.lang
%{_datadir}/qlogging-categories6/libksysguard.categories
%{_datadir}/ksysguard/scripts
%{_libdir}/libexec/kf6/kauth/ksysguardprocesslist_helper
%dir %{_libdir}/libexec/ksysguard
%caps(cap_net_raw+ep) %{_libdir}/libexec/ksysguard/ksgrd_network_helper
%{_datadir}/dbus-1/system.d/org.kde.ksysguard.processlisthelper.conf
%{_datadir}/dbus-1/interfaces/org.kde.ksystemstats.xml
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

%description -n %{libksgrd}
Plasma 6 KDE System Guard shared library.

%files -n %{libksgrd}
%{_libdir}/libksgrd.so.%{ksgrd_major}
%{_libdir}/libksgrd.so.5*
%{_libdir}/libKSysGuardSystemStats.so.2
%{_libdir}/libKSysGuardSystemStats.so.5*

#----------------------------------------------------------------------------

%package -n %{libksignalplotter}
Summary: Plasma 6 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libksignalplotter}
Plasma 6 KDE System Guard shared library.

%files -n %{libksignalplotter}
%{_libdir}/libksignalplotter.so.%{ksignalplotter_major}
%{_libdir}/libksignalplotter.so.5*

#----------------------------------------------------------------------------

%package -n %{liblsofui}
Summary: Plasma 6 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{liblsofui}
Plasma 6 KDE System Guard shared library.

%files -n %{liblsofui}
%{_libdir}/liblsofui.so.%{lsofui_major}
%{_libdir}/liblsofui.so.5*

#----------------------------------------------------------------------------

%package -n %{libprocesscore}
Summary: Plasma 6 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libprocesscore}
Plasma 6 KDE System Guard shared library.

%files -n %{libprocesscore}
%{_libdir}/libprocesscore.so.%{processcore_major}
%{_libdir}/libprocesscore.so.5*

#----------------------------------------------------------------------------

%package -n %{libprocessui}
Summary: Plasma 6 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libprocessui}
Plasma 6 KDE System Guard shared library.

%files -n %{libprocessui}
%{_libdir}/libprocessui.so.%{processui_major}
%{_libdir}/libprocessui.so.5*

#----------------------------------------------------------------------------

%package -n %{libformatter}
Summary: Plasma 6 KDE System Guard formatting library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libformatter}
Plasma 6 KDE System Guard formatting shared library.

%files -n %{libformatter}
%{_libdir}/libKSysGuardFormatter.so.%{formatter_major}
%{_libdir}/libKSysGuardFormatter.so.5*

#----------------------------------------------------------------------------

%package -n %{libsensorfaces}
Summary: Plasma 6 KDE System Guard sensor faces shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libsensorfaces}
Plasma 6 KDE System Guard sensor faces shared library.

%files -n %{libsensorfaces}
%{_libdir}/libKSysGuardSensorFaces.so.%{sensorfaces_major}
%{_libdir}/libKSysGuardSensorFaces.so.5*

#----------------------------------------------------------------------------

%package -n %{libsensors}
Summary: Plasma 6 KDE System Guard sensors shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libsensors}
Plasma 6 KDE System Guard sensors shared library.

%files -n %{libsensors}
%{_libdir}/libKSysGuardSensors.so.%{sensors_major}
%{_libdir}/libKSysGuardSensors.so.5*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary: Development files for the KDE Frameworks 6 system monitoring library
Group: Development/KDE and Qt
Requires: %{libksgrd} = %{EVRD}
Requires: %{libksignalplotter} = %{EVRD}
Requires: %{liblsofui} = %{EVRD}
Requires: %{libprocesscore} = %{EVRD}
Requires: %{libprocessui} = %{EVRD}
Requires: %{libformatter} = %{EVRD}
Requires: %{libsensorfaces} = %{EVRD}
Requires: %{libsensors} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 6 system monitoring library.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KSysGuard

%package -n %{desname}
Summary: Qt Designer plugin integrating KSysguard widgets
Group: Development/KDE and Qt
Requires: %{devname} = %{EVRD}

%description -n %{desname}
Qt Designer plugin integrating KSysguard widgets.

%files -n %{desname}
%{_libdir}/qt6/plugins/designer/ksignalplotter5widgets.so
%{_libdir}/qt6/plugins/designer/ksysguard5widgets.so
%{_libdir}/qt6/plugins/designer/ksysguardlsof5widgets.so

%prep
%autosetup -p1 -n libksysguard-%{?git:master}%{!?git:%{version}}
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
