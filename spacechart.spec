Summary:	SpaceChart - a 3d map of the stars
Summary(pl):	SpaceChart - trójwymiarowa mapa nieba
Name:		spacechart
Version:	0.9.2
Release:	8
License:	GPL
Group:		X11/Applications/Science
Source0:	http://zipi.fi.upm.es/~e970095/spacechart/download/%{name}-%(echo  %{version} | sed s/\\./_/g).tgz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-ac_fixes.patch
URL:		http://zipi.fi.upm.es/~e970095/spacechart/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
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
SpaceChart jest programem, który wy¶wietla mapê nieba w trzech
wymiarach oraz umo¿liwia jej obracanie wokó³ gwiazd. Za jego pomoc±
mo¿na ograniczyæ ogl±dany zbiór gwiazd wzglêdem ich w³asno¶ci, a tak¿e
odleg³o¶ci od centrum okna podgl±du.

Z programem jest do³±czany plik gliese.dat, który zosta³ utworzony na
podstawie katalogu Gliese Catalogue of Nearby Stars (trzecia wersja),
który zawiera wszystkie znane gwiazdy w odleg³o¶ci do 25 parseków od
S³oñca.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Scientific/Astronomy,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Astronomy
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_applnkdir}/Scientific/Astronomy/%{name}.desktop
%{_pixmapsdir}/*
