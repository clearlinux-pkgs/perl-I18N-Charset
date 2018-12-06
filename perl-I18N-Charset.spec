#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-I18N-Charset
Version  : 1.418
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/M/MT/MTHURN/I18N-Charset-1.418.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MT/MTHURN/I18N-Charset-1.418.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libi18n-charset-perl/libi18n-charset-perl_1.417-1.debian.tar.xz
Summary  : 'IANA Character Set Registry names and Unicode::MapUTF8 (et al.) conversion scheme names'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(IO::Capture::Stderr)

%description
I18N-Charset Distribution
This distribution contains a module I18N::Charset which maps Character
Set names to the names officially registered with IANA.  For example,
'Shift_JIS' is the official name of what is often referred to in HTML
headers as 'x-sjis'.

%package dev
Summary: dev components for the perl-I18N-Charset package.
Group: Development
Provides: perl-I18N-Charset-devel = %{version}-%{release}

%description dev
dev components for the perl-I18N-Charset package.


%prep
%setup -q -n I18N-Charset-1.418
cd ..
%setup -q -T -D -n I18N-Charset-1.418 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/I18N-Charset-1.418/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1I18N/Charset.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/I18N::Charset.3
