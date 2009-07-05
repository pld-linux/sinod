
%define		rel 20090705
Summary:	Simple Notification Daemon
Summary(pl.UTF-8):	Prosty serwer powiadomień
Name:		sinod
Version:	0
Release:	0.%{rel}.1
License:	GPL v3
Group:		Applications/System
Source0:	http://xatka.net/~z/sinod/%{name}-%{rel}.tar.bz2
# Source0-md5:	53796e8a6c3e7b7f2222e8f59ae615ab
URL:		http://xatka.net/~z/sinod
BuildRequires:	rpm-pythonprov
Requires:	dbus >= 0.91
Provides:	dbus(org.freedesktop.Notifications)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sinod is very simple implementation of notification daemon concept.
This program registers DBUS org.freedesktop.Notifications service and
prints all incoming notifications on standard output.

Unlike other notification daemons sinod does not displays any pop-up
windows. It only prints notifications on standard output. Its output
can be easily used by other scripts or programs. It can also be used
in environment without X windows at all (hey, think about
notifications from your screened irc session on shell acount a few
thousands kilometers away!).

%description -l pl.UTF-8
sinod jest bardzo prostą implementacją serwera powiadomień. Program
ten rejestruję w magistrali DBUS usługę org.freedesktop.Notifications
a następnie wypisuje na standardowe wyjście wszystkie przychodzące
powiadomienia.

W odróżnieniu od innych serwerów powiadomień, sinod nie wyświetla
żadnych wyskakujących okienek. Jedyne co robi to wypisuje
powiadomienia na standardowe wyjście. Dzięki temu może być łatwo
wykorzystany w połączeniu ze skryptami lub innymi programami. Sinod
może również być używany w środowiskach bez systemu okein X (pomyśl
tylko o powiadomieniach z "zascreenowanej" sesji irc na twoim koncie
shellowym tysiące kilometrów stąd).

%prep
%setup -q -n %{name}-%{rel}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install sinod $RPM_BUILD_ROOT%{_bindir}/sinod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/sinod
