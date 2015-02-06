%define upstream_name    IO-Interface
%define upstream_version 1.07
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl extension for access to network card configuration information
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/L/LD/LDS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel

%description
IO::Interface adds methods to IO::Socket objects that allows them to
be used to retrieve and change information about the network
interfaces on your system.  In addition to the object-oriented access
methods, you can use a function-oriented style.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
