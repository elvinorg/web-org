dnl ########################################################################
dnl
dnl              elvin.org web
dnl
dnl File:        $Source: /Users/d/work/elvin/CVS/web-org/org.m4,v $
dnl Version:     $RCSfile: org.m4,v $ $Revision: 1.3 $
dnl Copyright:   (C) 2002-2005 webmaster@elvin.org
dnl
dnl This program is free software; you can redistribute it and/or modify
dnl it under the terms of the GNU General Public License as published by
dnl the Free Software Foundation; either version 2 of the License, or
dnl (at your option) any later version.
dnl
dnl This program is distributed in the hope that it will be useful,
dnl but WITHOUT ANY WARRANTY; without even the implied warranty of
dnl MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
dnl GNU General Public License for more details.
dnl
dnl You should have received a copy of the GNU General Public License
dnl along with this program; if not, write to the Free Software
dnl Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
dnl
dnl ########################################################################*
dnl
dnl  macros for relative bits of the Elvin web
dnl
dnl  these are designed to allow portability of the web source, with
dnl  each site supplying the required basic parameters on the m4 command
dnl  line from the Makefile.
dnl
dnl    URL for home page, on this server
define(ELVIN_HOME,PUBLIC_SERVER`'PUBLIC_ROOT)dnl
dnl
dnl    URL for viewcvs page, on the CGI server
define(ELVIN_VIEWCVS_URL,ELVIN_CGI_HOME`'/viewcvs.cgi)dnl
dnl
dnl
dnl ########################################################################*
dnl
dnl  macros for external URLs
dnl
define(BREEZE_HOME,`http://www.dstc.edu.au/Research/Projects/KrowWolf/breeze.html')dnl
define(COSNS_HOME,`http://www.dstc.edu.au/Software/CosNotification.html')dnl
define(DSTC_HOME,`http://www.dstc.edu.au/')dnl
define(EDDIE_HOME,`http://www.codefx.com.au/eddie/')dnl
define(JRE_DOWNLOAD,`http://java.sun.com/products/jdk/1.1/jre/index.html')dnl
define(ORBIT_HOME,`http://www.dstc.edu.au/Research/Projects/Worlds/Prototypes/OrbitGold.html')dnl
define(TICKER_HOME,ELVIN_HOME/apps/tickertape)dnl
define(WORLDS_HOME,`http://www.dstc.edu.au/Research/Projects/Worlds')dnl
define(CORRELATION_HOME,ELVIN_HOME/correlation)dnl
dnl
dnl
dnl ########################################################################*
dnl
dnl  mail aliases
dnl
dnl    just the email address
define(ELVIN_MAIL,`elvin@dstc.edu.au')dnl
dnl
dnl    complete mailto link
define(ELVIN_MAILTO,`<a href="mailto:ELVIN_MAIL">ifelse($1, `', `<tt>ELVIN_MAIL</tt>', $1)</a>')dnl
define(MAILTO_ELVIN,ELVIN_MAILTO)dnl  this is deprecated!
dnl
dnl    downloads list
define(ELVIN_DOWNLOADS,`elvin-downloads@dstc.edu.au')dnl
dnl
dnl    ticker list
define(TICKER_MAIL,`elvin@dstc.edu.au')dnl
dnl
dnl    ticker mailto link
define(TICKER_MAILTO,`<a href="mailto:TICKER_MAIL">ifelse($1, `', `<tt>TICKER_MAIL</tt>', $1)</a>')dnl
define(JTICKER_DOWNLOADS,`jticker-downloads@dstc.edu.au')dnl
define(XTICKER_DOWNLOADS,`xticker-downloads@dstc.edu.au')dnl
dnl
dnl    licensing
define(LICENSE_MAIL,`elvin-licensing@dstc.edu.au')
define(LICENSE_MAILTO,`<a href="mailto:LICENSE_MAIL">ifelse($1, `', `<tt>LICENSE_MAIL</tt>', $1)</a>')dnl
dnl
dnl
changecom(/*,*/)dnl
define(m4_format,builtin(`format'))dnl
undefine(`format')dnl

dnl ########################################################################*
dnl ########################################################################*
dnl
dnl    darker red which has less "glare" (logo red is e2322c)
dnl
define(ELVIN_RED, `#aB1000')
dnl
dnl    lighter pink-y red
dnl
define(ELVIN_LIGHT_RED,`#ffeeee')
dnl
dnl    dark blue
dnl
define(ELVIN_BLUE, `#3366cc')
dnl
dnl
dnl    e4_heading(any text) -- inverse colour heading
dnl
define(e4_heading, `<table cellpadding="2" bgcolor="ELVIN_RED" width="100%">
<tr><td><font color="#ffffff"><b>$*</b></font></td></tr>
</table>
')dnl
dnl
dnl    e4_project(proj_dir, proj_title)
dnl
define(e4_project, `ifelse($2, `', <a href="ELVIN_HOME/projects/$1/index.html">$1</a>, <a href="ELVIN_HOME/projects/$1/index.html">$2</a>)')dnl
dnl
dnl    e4_text_url(text[, url]) - if url is there, create a link
dnl
define(e4_text_url, `ifelse($2, `', $1, <a href="$2">$1</a>)')dnl
dnl
dnl    e4_url_url(url) - make an URL with itself as text
dnl
define(e4_url_url, `<a href="$1">$1</a>')dnl
dnl
dnl
dnl FIXME - put some pretty tiny little icons here (and don't forget the
dnl         ALT tags :-)
define(E4_UPDATED_ICON, `<font color="#0000FF" size="-2">[UPDATED]</font>')dnl
define(E4_NEW_ICON, `<font color="#0000FF" size="-2">[NEW]</font>')dnl
dnl
dnl
dnl define(sb_section, `<b>text_url($1, $2)</b><br>')dnl
dnl define(sb_subsection, `&nbsp; text_url($1, $2)<br>')dnl
dnl define(sb_subsubsection, `&nbsp; &nbsp; text_url($1, $2)<br>')dnl
dnl define(sb_comment, `<small>$1</small><br>')dnl
dnl define(sb_subcomment, `&nbsp; &nbsp; <small>$1</small><br>')dnl
dnl
dnl
define(e4_mailurl, <a href="mailto:$1">$1</a>)
dnl
dnl
define(e4_nav_begin, `<!-- nav bar begin -->
<table width="100%" border="0" cellpadding="10" cellspacing="0">
  <tr>
    <td valign="top">
      <table border="0"  cellpadding="0" cellspacing="0">
        <tr>
          <td nowrap valign="bottom">
            <code>
')dnl
dnl
dnl
define(e4_nav_switch, `<!-- nav bar switch -->
            </code>
          </td>
          <td valign="bottom">
            <code>|</code>
          </td>
        </tr>
        <tr>
          <td>&nbsp;</td>
          <td align="left" valign="top">
            <code>
')dnl
dnl
dnl
define(e4_nav_end, `<!-- nav bar end -->
            </code>
          </td>
        </tr>
      </table>
    </td>
    <td valign="top" align="right">
      <form method="get" action="http://www.google.com/search">
	<input type="text" name="q" size="11" maxlength="255">
	<input type="hidden" name="domains" value="elvin.dstc.edu.au">
	<input type="hidden" name="sitesearch" value="elvin.dstc.edu.au">
      </form>
    </td>
  </tr>
</table>
<hr noshade size="2">
')dnl
dnl
dnl    e4_nav_item(title, url)
dnl
define(e4_nav_item,  ` |&nbsp;e4_text_url($1, $2)')dnl
dnl
dnl  nav_project(proj_name, ???, rel_proj_root)
dnl
dnl  i don't yet know where the second arg form is used.  the
dnl  third arg form is used in the download script, and the
dnl  rel_proj_root param is a path to the projects directory
dnl  from where the m4 is run.
dnl
define(e4_nav_project, `e4_nav_begin()dnl
ifelse($3, `', dnl
ifelse($2, `', dnl
dnl -- project name only supplied
e4_nav_item(elvin, ../../index.html)dnl
e4_nav_item(projects, ../index.html)dnl
, dnl
dnl -- project name and parent directory name (?) supplied
e4_nav_item(elvin, ../../../index.html)dnl
e4_nav_item(projects, ../../index.html)dnl
e4_nav_item($2, ../index.html)dnl
)dnl
e4_nav_item($1, ../$1/index.html)dnl
,dnl
dnl -- this is the case with the relative root supplied also
e4_nav_item(elvin, $3/../index.html)dnl
e4_nav_item(projects,$3/index.html)dnl
e4_nav_item($1,$3/$1/index.html)dnl
)dnl
dnl
e4_nav_switch()dnl
e4_nav_item(cvs, ELVIN_VIEWCVS_URL/$1/)dnl
e4_nav_item(bugzilla, ELVIN_BUGZILLA_URL/buglist.cgi?product=$1)dnl
e4_nav_end()')dnl
dnl
dnl
dnl
define(e4_nav_lang, `e4_nav_begin()dnl
e4_nav_item(elvin, ../../index.html)dnl
e4_nav_item(projects, ../index.html)dnl
e4_nav_item($1, index.html)dnl
e4_nav_switch()dnl
e4_nav_item(api, api/index.html)dnl
e4_nav_item(cvs, ELVIN_VIEWCVS_URL/$1/)dnl
e4_nav_item(bugzilla, ELVIN_BUGZILLA_URL/buglist.cgi?product=$1)dnl
e4_nav_end()')dnl
dnl ########################################################################
dnl ########################################################################
dnl
dnl    download macro for Aquatik (lawless)
dnl
define(e4_aquatik_download,`<a href="ELVIN_PKG_REQ?$1%20$2+$1.+CGI_PUBLIC_ROOT/download/GPL.txt+FTP_DOWNLOAD+HTTP_DOWNLOAD+lawley@dstc.edu.au">$3</a>')dnl
dnl
dnl
dnl
define(e3_download,`<a href="ELVIN_PKG_REQ?$1%20$2+$1.+CGI_PUBLIC_ROOT/download/licence.txt+FTP_DOWNLOAD+HTTP_DOWNLOAD+ELVIN_DOWNLOADS">$3</a>')dnl
dnl
dnl
define(e3_sticker_download,`<a href="ELVIN_PKG_REQ?$1%20$2+$1.+CGI_PUBLIC_ROOT/download/GPL.txt+FTP_DOWNLOAD+HTTP_DOWNLOAD+elvin-sticker@dstc.edu.au">$3</a>')dnl
dnl
define(ew_rpm_download,`<a href="CGI_HOME/rpm?.i386.rpm">$1</a>')dnl
dnl
define(rpm_link,`<a href="install/$1-$2.i386.rpm">$1</a>')dnl
dnl local files
define(ew_files_download,`<a href="files/$1">$1</a>')dnl
dnl
define(ew_filesrpm_download, `<a href="files/$1-$2.i386.rpm">$1</a>')dnl
define(ew_filesrpmno_download, `<a href="files/$1-$2.noarch.rpm">$1</a>')dnl
dnl
dnl    e4_download(name-verion, text_string)
dnl
define(e4_download, `<a href="CGI_HOME/download?$1">$2</a>')dnl
dnl
dnl    e4_licence()  --  licensing line
dnl
define(e4_licence, `
Elvin is <a href="PUBLIC_URL_ROOT/download/licence.txt">licensed</a>
but free for research and academic use. Enquiries can be sent to <a
href="mailto:elvin-licensing@dstc.edu.au">elvin-licensing@dstc.edu.au</a>
')dnl
dnl
dnl
define(e4_print_header,`
<!-- Copyright (C) elvin.org 1997-2002 -->

<html>
 <head>
  <title>ifelse($1, `', `Elvin', $1)</title>
 </head>
 <body bgcolor="#ffffff">
')dnl
dnl
dnl
define(e4_print_trailer,`
 <p>
 <center>&copy; 2002 Distributed Systems Technology Centre</center>
 </body>
</html>
')dnl
dnl
dnl    e4_example ( code segment, etc ) 
dnl
define(e4_example, `
<table width="100%" cellpadding="3"><tr><td bgcolor="EEEEEE">
<dl><dd>
<pre>$*</pre>
</dl>
</td></tr></table>
<p>
')dnl
dnl
dnl    e4_wide_example ( code segment, etc ) 
dnl
define(e4_wide_example, `
<table width="100%" cellpadding="3"><tr><td bgcolor="EEEEEE">
<pre>$*</pre>
</td></tr></table>
<p>
')dnl
dnl
dnl
dnl
dnl
dnl
dnl
dnl
dnl
dnl ########################################################################
dnl
dnl
define(ORG_REGISTRY_EMAIL,`registrar@elvin.org')dnl
define(ORG_REGISTRY_MAILTO,`<a href="mailto:ORG_REGISTRY_EMAIL">ORG_REGISTRY_EMAIL</a>')dnl
dnl
dnl
dnl
define(org_reverse_bg, `#888888')dnl
define(org_reverse_fg, `white')dnl
define(org_font_face, `helvetica,arial')dnl
dnl
dnl    org_header()  --  page header
dnl
define(org_header, `<html>
<head>
  <title>elvin.org</title>
</head>

<body bgcolor="white">

<table cellpadding="15" width="100%" border="0">

  <tr bgcolor="org_reverse_bg">
    <td colspan="2">
      <font color="org_reverse_fg" size="+6" face="org_font_face">
        <i><b>elvin.org</b></i>
      </font>
    </td>
  </tr>')dnl
dnl
dnl    org_footer() --  no arguments.
dnl
define(org_footer, `  <tr bgcolor="org_reverse_bg">
    <td colspan="2">
      <font color="org_reverse_fg" size="-2" face="org_font_face">
        Copyright &copy; 2002-2005&nbsp;&nbsp;&nbsp; 
	<a href="mailto:webmaster@elvin.org">webmaster@elvin.org</a>&nbsp;&nbsp;&nbsp;
	 Last updated: UPDATE
      </font>
    </td>
  </tr>

</table>

</body>
</html>')dnl
dnl
dnl
dnl
define(org_home_para,`  <tr>
    <td colspan="2">
      <font face="org_font_face">
$1<p>
      </font>
    </td>
  </tr>
')dnl
dnl
dnl
dnl
define(org_home_item,`  <tr>
    <td valign="top"><font size="+2" face="org_font_face">$1</font></td>
    <td>
      <font face="helvetica,arial">
$2
      </font>
    </td>
  </tr>
')dnl
dnl
dnl
dnl
dnl ########################################################################
