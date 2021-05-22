#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-I18N-Charset
Version  : 1.419
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/M/MT/MTHURN/I18N-Charset-1.419.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MT/MTHURN/I18N-Charset-1.419.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libi18n-charset-perl/libi18n-charset-perl_1.417-1.debian.tar.xz
Summary  : 'IANA Character Set Registry names and Unicode::MapUTF8 (et al.) conversion scheme names'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-I18N-Charset-license = %{version}-%{release}
Requires: perl-I18N-Charset-perl = %{version}-%{release}
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
Requires: perl-I18N-Charset = %{version}-%{release}

%description dev
dev components for the perl-I18N-Charset package.


%package license
Summary: license components for the perl-I18N-Charset package.
Group: Default

%description license
license components for the perl-I18N-Charset package.


%package perl
Summary: perl components for the perl-I18N-Charset package.
Group: Default
Requires: perl-I18N-Charset = %{version}-%{release}

%description perl
perl components for the perl-I18N-Charset package.


%prep
%setup -q -n I18N-Charset-1.419
cd %{_builddir}
tar xf %{_sourcedir}/libi18n-charset-perl_1.417-1.debian.tar.xz
cd %{_builddir}/I18N-Charset-1.419
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/I18N-Charset-1.419/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-I18N-Charset
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-I18N-Charset/786cd6afb452a127275fb4b51878c81cfffda8cb
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/I18N::Charset.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-I18N-Charset/786cd6afb452a127275fb4b51878c81cfffda8cb

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/I18N/Charset.pm
