Summary:	DFBPoint - a presentation viewer using DirectFB
Summary(pl):	DFBPoint - przegl�darka prezentacji u�ywaj�ca DirectFB
Name:		DFBPoint
Version:	0.7.2
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.directfb.org/download/DFBPoint/%{name}-%{version}.tar.gz
# Source0-md5:	a4552e47d9a3204c81e502c6358ec08e
URL:		http://www.directfb.org/index.php?path=Development/Projects/DFBPoint
BuildRequires:	DirectFB-devel >= 0.9.11
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc *.xml *.dtd *.ttf

%description
DFBPoint is a simple presentation viewer that uses the DirectFB
graphics library to draw to the Linux frame buffer.

%description -l pl
DFBPoint to prosta przegl�darka prezentacji u�ywaj�ca biblioteki
graficznej DirectFB do wy�wietlania na linuksowym framebufferze.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f examples/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README dfbpoint.dtd examples
%attr(755,root,root) %{_bindir}/*