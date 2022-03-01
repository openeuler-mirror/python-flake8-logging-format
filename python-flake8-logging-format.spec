%global _empty_manifest_terminate_build 0
Name:           python-flake8-logging-format
Version:        0.6.0
Release:        2
Summary:        Flake8 extension to validate (lack of) logging format strings
License:        Apache License 2.0
URL:            https://github.com/globality-corp/flake8-logging-format
Source0:        https://files.pythonhosted.org/packages/72/ad/4bf4d21330138e216c416e0195fa63a5b598100f17e49a284e8da2108b83/flake8-logging-format-0.6.0.tar.gz
BuildArch:      noarch
%description
Flake8 extension to validate (lack of) logging format strings


%package -n python3-flake8-logging-format
Summary:        Flake8 extension to validate (lack of) logging format strings
Provides:       python-flake8-logging-format
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
%description -n python3-flake8-logging-format
Flake8 extension to validate (lack of) logging format strings


%package help
Summary:        Flake8 extension to validate (lack of) logging format strings
Provides:       python3-flake8-logging-format-doc
%description help
Flake8 extension to validate (lack of) logging format strings


%prep
%autosetup -n flake8-logging-format-0.6.0

%build
%py3_build


%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
    find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
    find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-flake8-logging-format -f filelist.lst
%dir %{python3_sitelib}/*


%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri Feb 25 2022 huangtianhua <huangtianhua@huawei.com> - 0.6.0-2
- Remove python-nose due it is in recycle
  
* Mon Aug 09 2021 OpenStack_SIG <openstack@openeuler.org> - 0.6.0-1
- Package Spec generate
