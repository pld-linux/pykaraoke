Summary:	Python Powered Karaoke
Summary(pl):	Karaoke w Pythonie
Name:		pykaraoke
Version:	0.5
Release:	1
License:	LGPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/pykaraoke/%{name}-%{version}.zip
# Source0-md5:	1e05f284c7c6a8fac4024cddf77a5b63
Patch0:		%{name}-mid_charset.patch
URL:		http://www.kibosh.org/pykaraoke/
BuildRequires:	SDL-devel
BuildRequires:	python-pygame-devel
Requires:	python-pygame
Requires:	python-wxPython
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyKaraoke is a free karaoke player for Linux, FreeBSD, Windows and
GP2X.

You can use this program to play your collection of CDG, MIDI and MPEG
karaoke songs. No songs are provided, you must obtain these from
elsewhere.

PyKaraoke Features:
 - CDG (MP3+G, OGG+G) playback - Play standard CDG karaoke files
 - MIDI (.MID/.KAR) playback - Play MIDI format karaoke files
 - MPEG playback - Play karaoke songs and movies in MPEG format
 - Playlist - Queue up songs, sit back and enjoy
 - Searchable song database - Easily find your songs from the main
   screen
 - Search inside ZIP files - Play MP3+G/MIDI files wrapped in ZIP files
 - Cross-platform - Runs on Windows, Linux, FreeBSD and GP2X

%description -l pl
PyKaraoke to wolnodostêpny odtwarzacz karaoke dla Linuksa, FreeBSD,
Windows i GP2X.

Tego programu mo¿na u¿ywaæ do odtwarzania w³asnego zbioru piosenek
karaoke w formacie CDG, MIDI i MPEG. Nie zawiera ¿adnych piosenek,
trzeba je zdobyæ z innych ¼róde³.

Mo¿liwo¶ci PyKaraoke:
 - odtwarzanie standardowych plików karaoke CDG (MP3+G, OGG+G)
 - odtwarzanie plików karaoke w formacie MIDI (.MID/.KAR)
 - odtwarzanie piosenek i filmów w formacie MPEG
 - playlista - kolejkowanie piosenek
 - baza danych piosenek z wyszukiwaniem dostêpnym z g³ównego ekranu
 - szukanie wewn±trz plików ZIP, odtwarzanie plików MP3+G/MIDI z
   plików ZIP
 - wieloplatformowo¶æ - dzia³a pod Windows, Linuksem, FreeBSD i GP2X

%prep
%setup -q
%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{py_sitedir} -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*
%{_desktopdir}/*.desktop
%{_datadir}/%{name}
