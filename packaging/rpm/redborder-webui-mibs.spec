%global debug_package %{nil}

Name:    redborder-webui-mibs
Version: %{__version}
Release: %{__release}%{?dist}
Summary: redborder-webui mibs Package

License: MIT
URL:     https://github.com/redBorder/redborder-webui-mibs/
Source0: %{name}-%{version}.tar.gz

# Eliminamos las dependencias de node, npm, wget, etc.
Requires: bash libsmi
AutoReqProv: no

%description
This RPM package bundles all necessary MIB files required by redborder-webui
and installs them into the system MIBs directory.

%prep
%setup -qn %{name}-%{version}

%build
# No se requiere compilar nada ya que los MIBs son archivos de texto plano

%install
# 1. Crear el directorio de destino en el buildroot (Path estándar para MIBs personalizados)
mkdir -p %{buildroot}/usr/share/mibs/site

# 2. Copiar todo el contenido de tu carpeta 'resources/mibs/' al destino
# Asumiendo que en tu repositorio los mibs están en resources/mibs/
cp -r resources/mibs/* %{buildroot}/usr/share/mibs/site/

%clean
rm -rf %{buildroot}

%files
# Definimos los permisos por defecto para los archivos MIB (lectura para todos, ejecución no requerida)
%defattr(0644,root,root,0755)
/usr/share/mibs/site/

%changelog
* Wed Jul 08 2026 Vicnete Mesa <vimesa@redborder.com>
- first spec version
