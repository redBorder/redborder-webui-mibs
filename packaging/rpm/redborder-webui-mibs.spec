%global debug_package %{nil}

Name:    redborder-webui-mibs
Version: %{__version}
Release: %{__release}%{?dist}
Summary: redborder-webui mibs Package

License: MIT
URL:     https://github.com/redBorder/redborder-webui-mibs/
Source0: %{name}-%{version}.tar.gz

Requires: bash libsmi
AutoReqProv: no

%description
This RPM package bundles all necessary MIB files required by redborder-webui
and installs them into the system MIBs directory.

%prep
%setup -qn %{name}-%{version}

%build
# No compilation is required

%install
# Create the destination directory in the buildroot (Standard path for custom MIBs)
mkdir -p %{buildroot}/usr/share/mibs/webui

# Copy the entire contents of your ‘resources/mibs/’ folder to the destination
cp -r resources/mibs/* %{buildroot}/usr/share/mibs/webui/

%clean
rm -rf %{buildroot}

%files
# We set the default permissions for MIB files (read access for everyone, execute not required)
%defattr(0644,root,root,0755)
/usr/share/mibs/webui/

%changelog
* Wed Jul 08 2026 Vicnete Mesa <vimesa@redborder.com>
- first spec version
