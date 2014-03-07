# $Id$
# Authority: ip2location

%define real_name ip2location-c

Summary: IP2Location C Library
Name: ip2location-c
Version: 6.0.2
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.ip2location.com/developers/c

Source: http://ip2location.com/downloads/ip2location-c-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel
Obsoletes: IP2Location-C < %{version}-%{release}
Provides: IP2Location-C = %{version}-%{release}

%description
IP2Location C library enables the user to find the country, region, city, coordinates,
zip code, time zone, ISP, domain name, connection type, area code, weather, MCC, MNC,
mobile brand name, elevation and usage type that any IP address or hostname originates
from. It has been optimized for speed and memory utilization. Developers can use the
API to query all IP2Locatio(TM) binary databases for applications written in C or
supporting static/dynamic library. Commercial databases are available from
http://www.ip2location.com/

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: IP2Location-C-devel < %{version}-%{release}
Provides: IP2Location-C-devel = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README
%{_libdir}/libIP2Location.so
%exclude %{_includedir}/IP2Loc_DBInterface.h
%exclude %{_includedir}/IP2Location.h
%exclude %{_includedir}/imath.h
%exclude %{_libdir}/libIP2Location.a
%exclude %{_libdir}/libIP2Location.la

%changelog
* Fri Mar 07 2014 IP2Location <support@ip2location.com> - 6.0.2-1
- Initial package.
