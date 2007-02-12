Summary:	XShipWars sounds (Star Trek theme)
Summary(pl.UTF-8):	Dźwięki do XShipWars (motyw Star Trek)
Name:		xsw-stsounds
Version:	1.4
Release:	2
License:	GPL-like
Group:		Applications/Games
Source0:	ftp://gd.tuwien.ac.at/games/wolfpack/stsounds%{version}.tgz
# Source0-md5:	7a440c9f86c5a124912c6187d2943ef4
URL:		http://wolfpack.twu.net/ShipWars/XShipWars/
Provides:	xsw-sounds
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
XShipWars is a highly customizable and massivly multiplayer space
gamming system designed for play entirly over the Internet. This
package contains StarTrek sound theme for the game.

%description -l pl.UTF-8
XShipWars to wysoko konfigurowalny system gry w przestrzeni kosmicznej
dla wielu graczy, zaprojektowany do grania przez Internet. Ten pakiet
zawiera motyw dźwiękowy Star Trek dla tej gry.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xshipwars

cd $RPM_BUILD_ROOT%{_datadir}/xshipwars
tar xzf %{SOURCE0}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xshipwars/sounds/*
