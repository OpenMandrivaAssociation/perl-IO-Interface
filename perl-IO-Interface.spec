%define real_name IO-Interface

Summary:	IO::Interface - Perl extension for access to network card configuration information
Name:		perl-%{real_name}
Version:	1.05
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/L/LD/LDS/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
IO::Interface adds methods to IO::Socket objects that allows them to
be used to retrieve and change information about the network
interfaces on your system.  In addition to the object-oriented access
methods, you can use a function-oriented style.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/*/auto/IO/Interface
%{perl_vendorlib}/*/auto/IO/Interface/*
%{perl_vendorlib}/*/IO/*
%{_mandir}/*/*

