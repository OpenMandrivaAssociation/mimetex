Summary:        Easily embed LaTeX math in web pages
Name:           mimetex
Version:        1.71
Release:        %mkrel 3
License:        GPLv3
Group:          System/Servers
URL:            http://www.forkosh.com/mimetex.html
Source0:        http://www.forkosh.com/%{name}.zip
BuildRequires:	apache-base >= 2.0.54
Requires(pre):	apache-mpm-prefork
Requires:	apache-mpm-prefork
Requires(post): rpm-helper
Requires(postun): rpm-helper
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf %{buildroot}

install -d %{buildroot}/var/www/cgi-bin
install -d %{buildroot}/var/www/html
install -d %{buildroot}/var/cache/%{name}

install -m0755 mimetex.cgi %{buildroot}/var/www/cgi-bin/%{name}.cgi
install -m0644 mimetex.html %{buildroot}/var/www/html/%{name}.html

install -d %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d

# apache config
cat > %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/%{name}.conf << EOF

<LocationMatch /cgi-bin/%{name}.cgi>
    Order Deny,Allow
    Deny from All
    Allow from 127.0.0.1
    ErrorDocument 403 "Access denied per %{_sysconfdir}/httpd/conf/webapps.d/%{name}.conf"
</LocationMatch>

EOF

%post
%_post_webapp

%postun
%_postun_webapp

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/%{name}.conf
/var/www/cgi-bin/%{name}.cgi
/var/www/html/%{name}.html
%attr(0755,apache,apache) %dir /var/cache/%{name}
