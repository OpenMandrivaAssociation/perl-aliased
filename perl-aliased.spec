%define upstream_name    aliased
%define upstream_version 0.31

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Use shorter versions of class names
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//aliased-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel
BuildArch: noarch

Provides: perl(aliased)

%description
'aliased' is simple in concept but is a rather handy module. It loads the
class you specify and exports into your namespace a subroutine that returns
the class name. You can explicitly alias the class to another name or, if
you prefer, you can do so implicitly. In the latter case, the name of the
subroutine is the last part of the class name.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.300.0-2mdv2011.0
+ Revision: 658903
- rebuild for updated spec-helper

* Thu Aug 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.0
+ Revision: 410629
- update to 0.30

* Sun Nov 16 2008 Jérôme Quelin <jquelin@mandriva.org> 0.22-3mdv2009.1
+ Revision: 303674
- forcing provides: since all-lower case modules are automatically stripped

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.22-2mdv2009.0
+ Revision: 268890
- rebuild early 2009.0 package (before pixel changes)

* Thu Jun 12 2008 Jérôme Quelin <jquelin@mandriva.org> 0.22-1mdv2009.0
+ Revision: 218578
- fix summary & description
- import perl-aliased



