Summary:        Easily embed LaTeX math in web pages
Name:           mimetex
Version:        1.71
Release:        8
License:        GPLv3
Group:          System/Servers
URL:            http://www.forkosh.com/mimetex.html
Source0:        http://www.forkosh.com/%{name}.zip
Requires:       webserver

%description
MimeTeX lets you easily embed LaTeX math in your html pages. It parses a LaTeX
math expression and immediately emits the corresponding gif image, rather than
the usual TeX dvi. And mimeTeX is an entirely separate little program that
doesn't use TeX or its fonts in any way.

%prep
%setup -q -c

%build
%serverbuild

gcc $CFLAGS -DAA -DCACHEPATH=\"/var/cache/%{name}/\" mimetex.c gifsave.c -lm -o mimetex.cgi

%install
install -d %{buildroot}/var/www/cgi-bin
install -d %{buildroot}/var/www/html
install -d %{buildroot}/var/cache/%{name}

install -m0755 mimetex.cgi %{buildroot}/var/www/cgi-bin/%{name}.cgi
install -m0644 mimetex.html %{buildroot}/var/www/html/%{name}.html

install -d %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d

# apache config
cat > %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/%{name}.conf << EOF

<LocationMatch /cgi-bin/%{name}.cgi>
    Require all granted
</LocationMatch>
EOF


%clean

%files
%doc COPYING README
%config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/%{name}.conf
/var/www/cgi-bin/%{name}.cgi
/var/www/html/%{name}.html
%attr(0755,apache,apache) %dir /var/cache/%{name}


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.71-5mdv2011.0
+ Revision: 612867
- the mass rebuild of 2010.1 packages

* Sun Feb 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.71-4mdv2010.1
+ Revision: 509195
- rely on filetrigger for reloading apache configuration begining with 2010.1, rpm-helper macros otherwise

* Sun Dec 27 2009 Oden Eriksson <oeriksson@mandriva.com> 1.71-3mdv2010.1
+ Revision: 482814
- newer source, same version

* Mon Jun 22 2009 Oden Eriksson <oeriksson@mandriva.com> 1.71-2mdv2010.0
+ Revision: 387974
- newer code

* Wed May 27 2009 Oden Eriksson <oeriksson@mandriva.com> 1.71-1mdv2010.0
+ Revision: 380116
- 1.71

* Sun Sep 07 2008 Oden Eriksson <oeriksson@mandriva.com> 1.70-1mdv2009.0
+ Revision: 282156
- 1.70

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.64-2mdv2009.0
+ Revision: 239063
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Oden Eriksson <oeriksson@mandriva.com> 1.64-1mdv2008.0
+ Revision: 68452
- Import mimetex



* Tue Aug 21 2007 Oden Eriksson <oeriksson@mandriva.com> 1.64-1mdv2008.0
- initial Mandriva package

* Sun Sep 17 2006 Jorge Torres <jtorresh@gmail.com> 1.60-3
- Rebuild for Fedora Extras 6

* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.60-2
- Rebuild for Fedora Extras 5

* Sun Oct  9 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.60-1
- Initial RPM release
