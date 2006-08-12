Summary:	e-Sofokles
Summary(pl):	e-Sofokles to polski program dla szkó³. Pozwala na zarz±dzanie list± klas, uczniów i ich danymi.
Name:		esofokles
Version:	0.90.2
Release:	0.1
License:	GPL-v2
Group:		Applications
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.esofokles.ab-com.pl/
#BuildRequires:	mono
#Requires:	mono
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
e-Sofokles

%description -l pl
e-Sofokles to polski program dla szkó³. Pozwala na zarz±dzanie list±
klas, uczniów i ich danymi personalnymi, ocenami, uwagami. Umo¿liwia
tak¿e tworzenie raportów dla rodziców. Aplikacja jest
wieloplatformowa, co oznacza, ¿e mo¿emy j± uruchomiæ w ró¿nych
systemach operacyjnych, m. in. w Windowsie i Linuksie. Obs³uga
programu jest prosta - ma ³atwy w obs³udze graficzny interfejs
u¿ytkownika. Ponadto aplikacja posiada interfejs sieciowy dla
rodziców, który umo¿liwia przegl±danie ocen, uwag i frekwencji
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
