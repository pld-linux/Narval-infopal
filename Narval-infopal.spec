%define short_name infopal

Summary:	Information pal
Summary(pl):	Kompel informacyjny
Name:		Narval-%{short_name}
Version:	20011016
Release:	1
Source0:	ftp://ftp.logilab.org/pub/narval/applications/%{short_name}-%{version}.npm
License:	GPL
Group:		Applications
Group(de):	Applikationen
Group(pl):	Aplikacje
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	Narval
Url:		http://www.logilab.org/narval/app.html

%description
Infopal is an extension set for Narval

It let one set up an information pal that acts as a web proxy, builds
a daily newspaper, monitors websites for changes, classifies
bookmarks, etc.

%description -l pl
Infopal to zestaw rozszerzeñ dla Narval'a

Pozwala na skonfigurowanie osobistego informacyjnego kumpla, który
dzia³a jako proxy WWW, tworzy codzienn± gazetê, ¶ledzi zmiany stron
WWW, klasyfikuje zak³adki itp.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/narval/apps
install %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/narval/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/narval/apps/*
