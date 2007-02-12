# TODO - BuildRequires/Requires
#
Summary:	e-Sofokles - Polish application to manage school divisions and students
Summary(pl.UTF-8):	e-Sofokles - polski program dla szkół do zarządzania listą klas, uczniów i ich danymi
Name:		esofokles
Version:	1.0
Release:	0.9
License:	GPL-v2
Group:		Applications
Source0:	http://www.esofokles.ab-com.pl/download/sources/%{name}-%{version}.tar.gz
# Source0-md5:	7624dbaa0cc15dcdb8edf996f8665a3a
URL:		http://www.esofokles.ab-com.pl/
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.5.91-2
BuildRequires:	gettext-devel
BuildRequires:	mono-csharp >= 1.1.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
e-Sofokles is a Polish application for schools. It's designed to
manage schoold division and student lists and their personal data,
marks and notes. It allows to generate reports for parents. The
application is multi-platform - it can work in different operating
systems, including Windows and Linux. It's easy to use with nice GUI.
The application includes network interface for parents, which allows
browsing students' marks, notes and attendance.

%description -l pl.UTF-8
e-Sofokles to polski program dla szkół. Pozwala na zarządzanie listą
klas, uczniów i ich danymi personalnymi, ocenami, uwagami. Umożliwia
także tworzenie raportów dla rodziców. Aplikacja jest
wieloplatformowa, co oznacza, że można ją uruchomić pod kontrolą
różnych systemów operacyjnych, m.in. Windows i Linuksa. Obsługa
programu jest prosta - ma łatwy w obsłudze graficzny interfejs
użytkownika. Ponadto aplikacja posiada interfejs sieciowy dla
rodziców, który umożliwia przeglądanie ocen, uwag i frekwencji
uczniów.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/esofokles
%{_libdir}/esofokles/MySql.Data.dll
%{_libdir}/esofokles/esofokles.exe
%{_desktopdir}/esofokles.desktop
%{_pixmapsdir}/esofokles.ico
%{_pixmapsdir}/esofokles.png
