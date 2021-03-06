Summary:        Program for modifying or creating files
Name:           patch
Version:        2.7.6
Release:        4%{?dist}
License:        GPLv3+
URL:            http://www.gnu.org/software/%{name}
Source0:        ftp://ftp.gnu.org/gnu/patch/%{name}-%{version}.tar.gz
%define sha1 patch=0ed8f3e49d84964f27e27c712fc8780e291dfa60
Patch0:		CVE-2018-6951.patch
Patch1:		CVE-2018-1000156.patch
Patch2:		CVE-2018-6952.patch
patch3:         CVE-2019-13636.patch
Patch4:         CVE-2019-13638.patch
Group:          Development/Tools
Vendor:         VMware, Inc.
Distribution:   Photon
Conflicts:      toybox

%description
Program for modifying or creating files by applying a patch
file typically created by the diff program.

%prep
%setup -q
%patch0	-p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure --disable-silent-rules
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%check
sed -i "s/ulimit -n 32/ulimit -n 1024/g" tests/deep-directories
make  %{?_smp_mflags} check

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*/*

%changelog
*   Thu Aug 08 2019 Shreenidhi Shedi <sshedi@vmware.com> 2.7.6-4
-   Apply patch for CVE-2019-13636, CVE-2019-13638
*   Mon Nov 19 2018 Siju Maliakkal <smaliakkal@vmware.com> 2.7.6-3
-   Add patches for CVE-2018-6951,CVE-2018-1000156,CVE-2018-6952
*   Tue Oct 2 2018 Michelle Wang <michellew@vmware.com> 2.7.6-2
-   Add conflicts toybox.
*   Tue Sep 11 2018 Him Kalyan Bordoloi <bordoloih@vmware.com> 2.7.6-1
-   Upgrade to 2.7.6.
*   Fri Apr 28 2017 Divya Thaluru <dthaluru@vmware.com> 2.7.5-4
-   Fixed ulimit in test script.
*   Fri Oct 07 2016 ChangLee <changlee@vmware.com> 2.7.5-3
-   Modified %check.
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.7.5-2
-   GA - Bump release of all rpms.
*   Tue Aug 11 2015 Divya Thaluru <dthaluru@vmware.com> 2.7.5-1
-   Updating to 2.7.5 version.
*   Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 2.7.1-1
-   Initial build First version.
