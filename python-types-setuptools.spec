%define module types_setuptools

Name:		python-types-setuptools
Version:	76.0.0.20250313
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/types-setuptools/%{module}-%{version}.tar.gz
Summary:	Typing stubs for setuptools
URL:		https://pypi.org/project/types-setuptools/
License:	Apache-2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
Requires:	python
Requires:	python-setuptools

%description
Typing stubs for setuptools

This is a PEP 561 type stub package for the setuptools package. It can be used
by type-checking tools like mypy, pyright, pytype, Pyre, PyCharm, etc. to check
code that uses setuptools.

This version of types-setuptools aims to provide accurate annotations
for setuptools~=76.0.0.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py3_install


%files
%{py_sitedir}/distutils-stubs/*
%{py_sitedir}/setuptools-stubs/*
%{py_sitedir}/%{module}-%{version}-*.*-info/*
%license LICENSE
%doc README.md
