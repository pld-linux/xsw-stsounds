Summary:	XShipWars sounds (Star Trek theme)
Summary(pl):	D¼wiêki do XShipWars (temat Star Trek)
Name:		xsw-stsounds
Version:	1.4
Release:	2
License:	GPL-like
Group:		Applications/Games
Source0:	ftp://gd.tuwien.ac.at/games/wolfpack/stsounds%{version}.tgz
URL:		http://wolfpack.twu.net/ShipWars/XShipWars/
Provides:	xsw-sounds
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
XShipWars is a highly customizable and massivly multiplayer space
gamming system designed for play entirly over the Internet. This
package contains StarTrek sound theme for the game.

%description -l pl
XShipWars to wysoko konfigurowalny system gry w przestrzeni kosmicznej
dla wielu graczy, zaprojektowany do grania przez Internet. Ten pakiet
zawiera temat d¼wiêkowy Star Trek dla tej gry.

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
