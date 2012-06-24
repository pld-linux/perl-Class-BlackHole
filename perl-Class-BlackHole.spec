#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	BlackHole
Summary:	Class::BlackHole - base class to treat unhandled method calls as no-ops
Summary(pl):	Class::BlackHole - bazowa klasa do ignorowania nie obs�ugiwanych metod
Name:		perl-Class-BlackHole
Version:	0.03
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Normally, if you try to call a method that there's no handler for,
you get an error: Can't locate object method "flork" via package "X".
But for classes that inherit from Class::BlackHole, unhandled methods
become just no-operations.

%description -l pl
Normalnie pr�ba wywo�ania metody, kt�ra nie ma przypisanego kodu,
ko�czy si� b��dem: Can't locate object method "flork" via package "X".
Ale w przypadku klas dziedzicz�cych z Class::BlackHole, nie
obs�ugiwane metody s� po prostu pustymi operacjami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
