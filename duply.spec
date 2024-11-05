Summary:	Wrapper for duplicity
Name:		duply
Version:	2.5.3
Release:	1
License:	GPLv2
URL:		https://duply.net/
Source0:	https://downloads.sourceforge.net/ftplicity/%{name}_%{version}.tgz

BuildRequires:	txt2man >= 1.5.6

Requires:	duplicity

BuildArch:	noarch

%description
duply is a frontend for the mighty duplicity magic. It simplifies
running duplicity with cron or on command line by:

- keeping recurring settings in profiles per backup job
- automated import/export of keys between profile and keyring
- enabling batch operations e.g. backup_verify_purge
- executing pre/post scripts
- precondition checking for flawless duplicity operation

Since version 1.5.0 all duplicity backends are supported. Hence the
name changed from ftplicity to duply.

%files
%license gpl-2.0.txt
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}_%{version}

# fix shebang
sed -i "1c#!/bin/bash" %{name}

%build
# manpgage
sh %{name} txt2man > %{name}.1

%install
# binary
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

# manpage
install -Dpm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# root's profiles will be stored there
install -dm 0755 %{buildroot}%{_sysconfdir}/%{name}

