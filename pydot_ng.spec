#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pydot_ng
Version  : 1.0.0
Release  : 19
URL      : http://pypi.debian.net/pydot_ng/pydot_ng-1.0.0.tar.gz
Source0  : http://pypi.debian.net/pydot_ng/pydot_ng-1.0.0.tar.gz
Summary  : Python interface to Graphviz's Dot
Group    : Development/Tools
License  : MIT
Requires: pydot_ng-python3
Requires: pydot_ng-python
Requires: graphviz
Requires: pyparsing
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyparsing
BuildRequires : pytest

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
---------------------------------------------------
        Ero Carrera (c) 2004-2007
        
        ero@dkbza.org
        
        This code is distributed under the MIT license.

%package python
Summary: python components for the pydot_ng package.
Group: Default
Requires: pydot_ng-python3

%description python
python components for the pydot_ng package.


%package python3
Summary: python3 components for the pydot_ng package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pydot_ng package.


%prep
%setup -q -n pydot_ng-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507169105
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
