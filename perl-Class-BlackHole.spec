#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	BlackHole
Summary:	Class::BlackHole - base class to treat unhandled method calls as no-ops
Summary(pl):	Class::BlackHole - bazowa klasa do ignorowania nie obs³ugiwanych metod
Name:		perl-Class-BlackHole
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a11985779f85aeece9f9f0df823c4dda
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Normally, if you try to call a method that there's no handler for,
you get an error: Can't locate object method "flork" via package "X".
But for classes that inherit from Class::BlackHole, unhandled methods
become just no-operations.

%description -l pl
Normalnie próba wywo³ania metody, która nie ma przypisanego kodu,
koñczy siê b³êdem: Can't locate object method "flork" via package "X".
Ale w przypadku klas dziedzicz±cych z Class::BlackHole, nie
obs³ugiwane metody s± po prostu pustymi operacjami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
