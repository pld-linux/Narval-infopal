%define short_name infopal

Summary:	Information pal
Summary(pl.UTF-8):   Kumpel informacyjny
Name:		Narval-%{short_name}
Version:	20020927
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.logilab.org/pub/narval/applications/%{short_name}-%{version}.npm
# Source0-md5:	944d56d9d8e980646ca53a8e6af87f2d
URL:		http://www.logilab.org/narval/app.html
Requires:	Narval
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Infopal is an extension set for Narval. It let one set up an
information pal that acts as a web proxy, builds a daily newspaper,
monitors websites for changes, classifies bookmarks, etc.

%description -l pl.UTF-8
Infopal to zestaw rozszerzeń dla Narvala. Pozwala na skonfigurowanie
osobistego informacyjnego kumpla, który działa jako proxy WWW, tworzy
codzienną gazetę, śledzi zmiany stron WWW, klasyfikuje zakładki itp.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -D %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/narval/apps/%{short_name}-%{version}/npm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/narval/apps/*
