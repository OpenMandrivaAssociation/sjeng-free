%define	version	11.2
%define release	%mkrel 3
%define pkgname Sjeng-Free

Summary:	Chess program that plays many variants
Name:		sjeng-free
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Boards
URL:		http://sjeng.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/sjeng/%{pkgname}-%{version}.tar.bz2
Source1:	sjeng.6.bz2
Source2:	sjeng-README.bz2
Patch0:		sjeng-11.2-cleanup.patch
Patch1:		sjeng-11.2-fhs.patch
BuildRequires:	automake1.9
BuildRequires:	gdbm-devel
# use version here, in case opening books need to be rebuilt
# due to binary imcompatibility from future gdbm(?)
# Nanar: this requires does not exists in the distro... ???
# Requires:	sjeng-book = 0.1
Provides:	chessengine

%description
Sjeng is a chess program that plays normal chess and many variants
like crazyhouse, bughouse, suicide (aka giveaway or anti-chess) and
losers. It can also play variants which have the same rules as normal
chess, but a different starting position. It uses the XBoard/WinBoard
interface by Tim Mann, so it can be used with xboard or eboard. It
is also capable of playing on internet chess servers.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1 -b .cleanup
%patch1 -p1 -b .fhs

FORCE_AUTOCONF_2_5=1 ACLOCAL=aclocal-1.9 AUTOMAKE=automake-1.9 autoreconf --force --install

bzip2 -dc %{SOURCE2} > README.debian

# (Abel) supress annoying rpmlint warning message
perl -pi -e 's/\r//g' [[:upper:]][[:upper:]]* ChangeLog

%build
%configure2_5x \
	--bindir=%{_gamesbindir} \
	--datadir=%{_gamesdatadir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man6
bzip2 -dc %{SOURCE1} > ${RPM_BUILD_ROOT}%{_mandir}/man6/sjeng.6

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog NEWS README README.debian
%{_gamesbindir}/*
%{_mandir}/man6/sjeng.6*


