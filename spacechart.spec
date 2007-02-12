Summary:	SpaceChart - a 3d map of the stars
Summary(pl.UTF-8):   SpaceChart - trójwymiarowa mapa nieba
Name:		spacechart
Version:	0.9.5
Release:	2
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.gnu.org/pub/gnu/spacechart/%{name}-%{version}.tar.gz
# Source0-md5:	5d23778a92b3c4a1e843efc114d69f83
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.gnu.org/software/spacechart/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SpaceChart is a program for displaying maps of the stars in 3D and
rotate them. It is capable of showing only a subset of the stars in a
given data file, and only those within a given distance of the center
of the display. Also, it shows lines between stars that are closer
than a given distance.

Included with the program is the file gliese.dat, which is based on
the Gliese Catalogue of Nearby Stars, 3rd version, which includes all
known stars within 25 parsecs of the Sun.

%description -l pl.UTF-8
SpaceChart jest programem, który wyświetla mapę nieba w trzech
wymiarach oraz umożliwia jej obracanie wokół gwiazd. Za jego pomocą
można ograniczyć oglądany zbiór gwiazd względem ich własności, a także
odległości od centrum okna podglądu.

Z programem jest dołączany plik gliese.dat, który został utworzony na
podstawie katalogu Gliese Catalogue of Nearby Stars (trzecia wersja),
który zawiera wszystkie znane gwiazdy w odległości do 25 parseków od
Słońca.

%prep
%setup -q

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
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README doc/coordinates.txt doc/sample-spacechartrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/spacechartrc
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*
