# TODO:
# - initscript
Summary:	"Sticky" Honeypot and IDS
Summary(pl):	Przynêta dla hackerów i IDS
Name:		labrea
Version:	2.5
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/labrea/%{name}-%{version}-stable-1.tar.gz
# Source0-md5:	e76d506e82b60cc5477ccee1b3368cda
URL:		http://labrea.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdnet-devel
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LaBrea takes over unused IP addresses, and creates virtual servers
that are attractive to worms, hackers, and other denizens of the
Internet. The program answers connection attempts in such a way that
the machine at the other end gets "stuck", sometimes for a very long
time.

%description -l pl
LaBrea przejmuje niewykorzystane adresy IP, i tworzy wirtualne serwery
atrakcyjne dla robaków, hackerów i innych czarnych charakterów
internetu. Program odpowiada prób± po³±czenia, tak ¿e atakuj±cy
komputer mo¿e byæ zablokowany przez d³ugi okres czasu.

%prep
%setup -q -n %{name}-%{version}-stable-1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%{_mandir}/man?/*
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_sbindir}/labrea
