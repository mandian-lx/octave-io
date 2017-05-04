%define octpkg io

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	Input/Output in external formats
Name:		octave-%{octpkg}
Version:	2.4.7
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+ and BSD
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.8.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Input/Output in external formats.

This package is part of community Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

