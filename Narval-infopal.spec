%define short_name infopal

Summary:	Information pal
Summary(pl):	Kumpel informacyjny
Name:		Narval-%{short_name}
Version:	20011016
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.logilab.org/pub/narval/applications/%{short_name}-%{version}.npm
# Source0-md5:	46959c58db9d0a2da357370abf9f5328
URL:		http://www.logilab.org/narval/app.html
Requires:	Narval
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Infopal is an extension set for Narval. It let one set up an
information pal that acts as a web proxy, builds a daily newspaper,
monitors websites for changes, classifies bookmarks, etc.

%description -l pl
Infopal to zestaw rozszerzeñ dla Narvala. Pozwala na skonfigurowanie
osobistego informacyjnego kumpla, który dzia³a jako proxy WWW, tworzy
codzienn± gazetê, ¶ledzi zmiany stron WWW, klasyfikuje zak³adki itp.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/narval/apps
install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/narval/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/narval/apps/*
