Summary:	PMDK pool conversion tool
Summary(pl.UTF-8):	Narzędzie do konwersji puli PMDK
Name:		pmdk-convert
Version:	1.5
Release:	1
License:	BSD
Group:		Applications/System
#Source0Download: https://github.com/pmem/pmdk-convert/releases
Source0:	https://github.com/pmem/pmdk-convert/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0f3020110ff7fead87cc88fae4dce0c5
Source1:	https://github.com/pmem/pmdk/archive/1.0/pmdk-1.0.tar.gz
# Source1-md5:	ffd191d5e2d69ecfc622652867cdca01
Source2:	https://github.com/pmem/pmdk/archive/1.1/pmdk-1.1.tar.gz
# Source2-md5:	71204f835a1920dff0381e9fc32a0366
Source3:	https://github.com/pmem/pmdk/archive/1.2.3/pmdk-1.2.3.tar.gz
# Source3-md5:	5097b29ec3e37721f71a01f2b929b4d4
Source4:	https://github.com/pmem/pmdk/archive/1.3.1/pmdk-1.3.1.tar.gz
# Source4-md5:	96fcdbb6e7e77b5302ebd88603d32bcb
Source5:	https://github.com/pmem/pmdk/archive/1.4.2/pmdk-1.4.2.tar.gz
# Source5-md5:	bde73bca9ef5b90911deb0fdcfb15ccf
Source6:	https://github.com/pmem/pmdk/archive/1.5/pmdk-1.5.tar.gz
# Source6-md5:	32cf94f0c8f754c94e5b91fd41ea102c
URL:		http://pmem.io/pmdk/
BuildRequires:	cmake >= 3.3
BuildRequires:	gcc >= 5:3.2
BuildRequires:	rpmbuild(macros) >= 1.605
ExclusiveArch:	%{x8664} aarch64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PMDK pool conversion tool.

%description -l pl.UTF-8
Narzędzie do konwersji puli PMDK.

%prep
%setup -q -a1 -a2 -a3 -a4 -a5 -a6

# rename to names expected by CMakeLists.txt
%{__mv} pmdk-1.0 nvml-1.0
%{__mv} pmdk-1.1 nvml-1.1
%{__mv} pmdk-1.2.3 nvml-1.2
%{__mv} pmdk-1.3.1 nvml-1.3
%{__mv} pmdk-1.4.2 nvml-1.4
%{__mv} pmdk-1.5 nvml-1.5
# fake to avoid downloading
touch nvml-{1.0,1.1,1.2.3,1.3.1,1.4.2,1.5}.tar.gz

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.md
%attr(755,root,root) %{_bindir}/pmdk-convert
%dir %{_libdir}/pmdk-convert
%attr(755,root,root) %{_libdir}/pmdk-convert/libpmem-convert.so
%attr(755,root,root) %{_libdir}/pmdk-convert/pmemobj_convert_v*.so
%{_mandir}/man1/pmdk-convert.1*
