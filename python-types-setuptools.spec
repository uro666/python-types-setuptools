%define module types-setuptools
%define uname types_setuptools

Name:		python-types-setuptools
Version:	76.0.0.20250313
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/t/types-setuptools/%{uname}-%{version}.tar.gz
Summary:	Typing stubs for setuptools
URL:		https://pypi.org/project/types-setuptools/
License:	Apache-2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	python
Requires:	python%{pyver}dist(setuptools)
Provides:	python%{pyver}dist(%{module})

%description
Typing stubs for setuptools

This is a PEP 561 type stub package for the setuptools package. It can be used
by type-checking tools like mypy, pyright, pytype, Pyre, PyCharm, etc. to check
code that uses setuptools.

This version of types-setuptools aims to provide accurate annotations
for setuptools~=76.0.0.

%prep
%autosetup -p1 -n %{uname}-%{version}

%build
%py_build

%install
%py3_install


%files
%{py_sitedir}/distutils-stubs/*
%{py_sitedir}/setuptools-stubs/*
%{py_sitedir}/%{uname}-%{version}-*.*-info/*
%license LICENSE
%doc README.md
