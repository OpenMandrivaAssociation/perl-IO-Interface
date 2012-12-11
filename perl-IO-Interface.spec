%define upstream_name    IO-Interface
%define upstream_version 1.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	IO::Interface - Perl extension for access to network card configuration information
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/L/LD/LDS/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.50.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-2mdv2011.0
+ Revision: 555963
- rebuild for perl 5.12

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-1mdv2010.0
+ Revision: 402548
- update to 0.56

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.05-2mdv2009.0
+ Revision: 268529
- rebuild early 2009.0 package (before pixel changes)

* Sat Jun 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2009.0
+ Revision: 216584
- update to new version 1.05

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.04-2mdv2008.1
+ Revision: 152120
- rebuild

* Thu Dec 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2008.1
+ Revision: 138325
- update to new version 1.04
- update to new version 1.04

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.03-1mdv2008.0
+ Revision: 20200
- 1.03


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.98-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.98-1mdk
- initial Mandriva package

