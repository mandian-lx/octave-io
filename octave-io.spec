%define octpkg io

Summary:	Octave toolkit for I/O in external formats
Name:           octave-%{octpkg}
Version:	2.4.5
Release:        3
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+ and BSD
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/io/
BuildRequires:  octave-devel >= 3.8.0
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
Octave toolkit for I/O in external formats.

%prep
%setup -q -c %{octpkg}-%{version}
cp %SOURCE0 .

%build
%octave_pkg_build  -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkgdir}
%{octpkglibdir}
