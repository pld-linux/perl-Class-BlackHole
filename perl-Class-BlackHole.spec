#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	BlackHole
Summary:	Class::BlackHole - base class to treat unhandled method calls as no-ops
Summary(pl):	Class::BlackHole - bazowa klasa do ignorowania nie obs³ugiwanych metod
Name:		perl-Class-BlackHole
Version:	0.03
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	568ca5e8a9520d0ae2453c3ee9a49d5f
BuildRequires:	perl-devel >= 5.6
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
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
