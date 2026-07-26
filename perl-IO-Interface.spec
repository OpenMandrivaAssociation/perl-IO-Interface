%define upstream_name    IO-Interface
Name:		perl-%{upstream_name}
Version:	1.09
Release:	2

Summary:	Perl extension for access to network card configuration information
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/IO-Interface
Source0:	https://cpan.metacpan.org/authors/id/L/LD/LDS/IO-Interface-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel

%description
IO::Interface adds methods to IO::Socket objects that allows them to
be used to retrieve and change information about the network
interfaces on your system.  In addition to the object-oriented access
methods, you can use a function-oriented style.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%dir %{perl_vendorlib}/*/auto/IO/Interface
%{perl_vendorlib}/*/auto/IO/Interface/*
%{perl_vendorlib}/*/IO/*
%{_mandir}/*/*
