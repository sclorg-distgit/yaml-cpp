%{?scl:%scl_package yaml-cpp}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}yaml-cpp
Version:        0.5.1
Release:        10%{?dist}
Summary:        A YAML parser and emitter for C++
Group:          Development/Libraries
License:        MIT 
URL:            http://code.google.com/p/yaml-cpp/
Source0:        http://yaml-cpp.googlecode.com/files/%{pkg_name}-%{version}.tar.gz
Patch0:         yaml-cpp-majorversion.patch

BuildRequires:  cmake
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
BuildRequires:  boost-devel
%else
BuildRequires:  %{?scl_prefix}boost-devel
%endif

%{?scl:Requires:%scl_runtime}

%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

%package        devel
Summary:        Development files for %{pkg_name}
Group:          Development/Libraries
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
Requires:       boost-devel
%else
Requires:       %{?scl_prefix}boost-devel
%endif

%description    devel
The %{pkg_name}-devel package contains libraries and header files for
developing applications that use %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q
%patch0 -p1 -b .majorversion
# Fix eol 
sed -i 's/\r//' license.txt

%build
%{?scl:scl enable %{scl} - << \EOF}
# ask cmake to not strip binaries
%cmake . -DYAML_CPP_BUILD_TOOLS=0 -DVERSION_MAJOR_PREFIX="%{?scl_prefix}"
make VERBOSE=1 %{?_smp_mflags}
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%make_install
%{?scl:EOF}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc license.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/yaml-cpp/
%{_libdir}/*.so
%{_libdir}/pkgconfig/

%changelog
* Thu Feb 11 2016 Marek Skalicky <mskalick@redhat.com> - 0.5.1-10
- Fixed pkgconfig directory ownership

* Thu Jan 22 2015 Marek Skalicky <mskalick@redhat.com> - 0.5.1-9
- Fixed devel requires (system boost libraries)

* Thu Jan 22 2015 Marek Skalicky <mskalick@redhat.com> - 0.5.1-8
- Use system boost libs in RHEL7 (same in rh-mongodb26-mongodb)

* Tue Jan 20 2015 Marek Skalicky <mskalick@redhat.com> - 0.5.1-7
- Fixed using boost from rh-mongodb26 SCL

* Sun Jan 18 2015 Honza Horak <hhorak@redhat.com> - 0.5.1-6
- Change major version for scl package

* Sat Jan 17 2015 Honza Horak <hhorak@redhat.com> - 0.5.1-5
- Convert to SCL

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.5.1-2
- Rebuild for boost 1.55.0

* Thu Nov 14 2013 Richard Shaw <hobbes1069@gmail.com> - 0.5.1-1
- Update to latest upstream release.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Richard Shaw <hobbes1069@gmail.com> - 0.3.0-1
- Update to latest release.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.7-1
- Update to 0.2.7
- Remove gcc 4.6 patch fixed upstream

* Mon May 09 2011 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.6-1
- Upstream 0.2.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 02 2010 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.5-1
- Upstream 0.2.5

* Fri Jan 15 2010 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.4-1
- Upstream 0.2.4

* Sat Oct 17 2009 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.2-2
- Remove duplicate file

* Wed Oct 14 2009 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.2-1
- Initial packaging 
