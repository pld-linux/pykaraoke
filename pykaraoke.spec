Summary:	Python Powered Karaoke
Summary(pl.UTF-8):	Karaoke w Pythonie
Name:		pykaraoke
Version:	0.7.1
Release:	1
License:	LGPL v2.1+
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/pykaraoke/%{name}-%{version}.zip
# Source0-md5:	28c57afe676f324030a1706f706d7e93
Patch0:		%{name}-mid_charset.patch
URL:		http://www.kibosh.org/pykaraoke/
BuildRequires:	SDL-devel
BuildRequires:	python-pygame-devel
BuildRequires:	python-wxPython
BuildRequires:	unzip
Requires:	python-pygame
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

%description -l pl.UTF-8
PyKaraoke to wolnodostępny odtwarzacz karaoke dla Linuksa, FreeBSD,
Windows i GP2X.

Tego programu można używać do odtwarzania własnego zbioru piosenek
karaoke w formacie CDG, MIDI i MPEG. Nie zawiera żadnych piosenek,
trzeba je zdobyć z innych źródeł.

Możliwości PyKaraoke:
 - odtwarzanie standardowych plików karaoke CDG (MP3+G, OGG+G)
 - odtwarzanie plików karaoke w formacie MIDI (.MID/.KAR)
 - odtwarzanie piosenek i filmów w formacie MPEG
 - playlista - kolejkowanie piosenek
 - baza danych piosenek z wyszukiwaniem dostępnym z głównego ekranu
 - szukanie wewnątrz plików ZIP, odtwarzanie plików MP3+G/MIDI z
   plików ZIP
 - wieloplatformowość - działa pod Windows, Linuksem, FreeBSD i GP2X

%prep
%setup -q
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

#find $RPM_BUILD_ROOT%{py_sitedir} -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*.py[co]
%{_desktopdir}/*.desktop
%{_datadir}/%{name}
