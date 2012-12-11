%define	pkgname io
%define name	octave-%{pkgname}
%define version 1.0.14

Summary:	Octave toolkit for I/O in external formats
Name:		%{name}
Version:	%{version}
Release:        2
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/io/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.2.0
BuildRequires:  octave-devel >= 3.2.0
BuildRequires:  mesagl-devel
BuildRequires:  mesaglu-devel
BuildRequires:	texinfo
BuildArch:	noarch

%description
Octave toolkit for I/O in external formats.

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}/COPYING .
mv %{pkgname}/DESCRIPTION .

%clean

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}


%changelog
* Tue Jun 28 2011 Lev Givon <lev@mandriva.org> 1.0.14-1mdv2011.0
+ Revision: 688037
- import octave-io


