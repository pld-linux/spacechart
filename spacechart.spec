Summary:	SpaceChart - a 3d map of the stars
Summary(pl):	SpaceChart - tr�jwymiarowa mapa nieba
Name:		spacechart
Version:	0.9.2
Release:	4
License:	GPL
Group:		X11/Applications/Science
Group(de):	X11/Applikationen/Wissenschaft
Group(pl):	X11/Aplikacje/Nauka
Source0:	http://zipi.fi.upm.es/~e970095/spacechart/download/%{name}-0_9_2.tgz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://zipi.fi.upm.es/~e970095/spacechart/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
SpaceChart is a program for displaying maps of the stars in 3D and
rotate them. It is capable of showing only a subset of the stars in a
given data file, and only those within a given distance of the center
of the display. Also, it shows lines between stars that are closer
than a given distance.

Included with the program is the file gliese.dat, which is based on
the Gliese Catalogue of Nearby Stars, 3rd version, which includes all
known stars within 25 parsecs of the Sun.

%description -l pl
SpaceChart jest programem, kt�ry wy�wietla map� nieba w trzech
wymiarach oraz umo�liwia jej obracanie wok� gwiazd. Za jego pomoc�
mo�na ograniczy� ogl�dany zbi�r gwiazd wzgl�dem ich w�asno�ci, a tak�e
odleg�o�ci od centrum okna podgl�du.

Z programem jest do��czany plik gliese.dat, kt�ry zosta� utworzony na
podstawie katalogu Gliese Catalogue of Nearby Stars (trzecia wersja),
kt�ry zawiera wszystkie znane gwiazdy w odleg�o�ci do 25 parsek�w od
S�o�ca.

%prep
%setup -q

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Scientific,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}/*
%{_applnkdir}/Scientific/%{name}.desktop
%{_pixmapsdir}/*
