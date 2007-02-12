Summary:	Foosball is an open source foosball (Table Football) game
Summary(pl.UTF-8):   Foosball jest grą w piłkarzyki
Name:		foosball
Version:	0.92
Release:	3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.autismuk.freeserve.co.uk/%{name}-%{version}.tar.gz
# Source0-md5:	a7b1513216bf00b2c01e28c1621cac6f
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://freshmeat.net/projects/foosball/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Foosball is an open source foosball (Table Football) game that uses
SDL. It allows you to play against the computer, or to play against a
friend. Various formations and game speeds are available.

%description -l pl.UTF-8
Foosball jest grą w piłkarzyki używającą biblioteki SDL. Można grać z
komputerem lub z inną osobą. Dostępne są różne ustawienia i szybkości
gry.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
