Summary:	SpaceChart - a 3d map of the stars
Summary(pl):	SpaceChart - trójwymiarowa mapa nieba
Name:	spacechart
Version: 0.9.2
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source:	%{name}-0_9_2.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-libs-devel

%define		_prefix		/usr/X11R6

%description
SpaceChart is a program for displaying maps of the stars in 3D and rotate
them.  It is capable of showing only a subset of the stars in a given data
file, and only those within a given distance of the center of the display.
Also, it shows lines between stars that are closer than a given distance.

Included with the program is the file gliese.dat, which is based on the
Gliese Catalogue of Nearby Stars, 3rd version, which includes all known
stars within 25 parsecs of the Sun.

%description -l pl
SpaceChart jest programem, który wy¶wietla mapê nieba w trzech wymiarach
oraz umo¿liwia jej obracanie wokó³ gwiazd. Za jego pomoc± mo¿na
ogl±daæ tylko wybrany podzbiór gwiazd z danego pliku, a tak¿e ty

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}/*
