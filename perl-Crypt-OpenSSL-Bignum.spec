#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenSSL-Bignum
Summary:	Crypt::OpenSSL::Bignum - OpenSSL's multiprecision integer arithmetic
Summary(pl.UTF-8):   Crypt::OpenSSL::Bignum - arytmetyka liczb całkowitych dużej precyzji z OpenSSL
Name:		perl-Crypt-OpenSSL-Bignum
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b526c1554b2f3bf7d94bf0c8c474fd2d
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::Bignum provides access to OpenSSL multiprecision
integer arithmetic libraries. Presently, many though not all of the
arithmetic operations that OpenSSL provides are exposed to Perl. In
addition, this module can be used to provide access to bignum values
produced by other OpenSSL modules, such as key parameters from
Crypt::OpenSSL::RSA.

%description -l pl.UTF-8
Crypt::OpenSSL::Bignum daje dostęp do bibliotek arytmetyki
liczb całkowitych dużej precyzji z OpenSSL. Aktualnie wiele, ale nie
wszystkie, operacje arytmetyczne udostępniane przez OpenSSL są
dostępne z Perla. Ponadto ten moduł może być używany do udostępnienia
dużych wartości produkowanych przez inne moduły OpenSSL, takie jak
parametry klucza z Crypt::OpenSSL::RSA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/OpenSSL/Bignum.pm
%{perl_vendorarch}/Crypt/OpenSSL/Bignum
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL/Bignum
%{perl_vendorarch}/auto/Crypt/OpenSSL/Bignum/Bignum.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/OpenSSL/Bignum/Bignum.so
%{_mandir}/man3/*
