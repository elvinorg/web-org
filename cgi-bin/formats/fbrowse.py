#! /usr/bin/python2.0
########################################################################
#
#              Elvin Web
#              notification format registry
#
# File:        $Source: /Users/d/work/elvin/CVS/web-org/cgi-bin/formats/fbrowse.py,v $
# Version:     $RCSfile: fbrowse.py,v $ $Revision: 1.1 $
# Copyright:   (C) 1998-2002 elvin.org
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
########################################################################
"""

Display a notification format, given the raw data file.


"""

########################################################################
#
# configuration
#

ORG_SERVER = "http://www.elvin.org"
ORG_ROOT = ""
ORG_CGI_HOME = "http://www.elvin.org/cgi-bin"
ORG_CGI_FORMAT_ROOT = "/formats"
ORG_REGISTRY = "/u1/www/www.elvin.org/regs/formats/registry"


########################################################################

import base64, cgi, os, pickle, sys, getopt, random, string, time, traceback, urllib


########################################################################

web_header = '''Content-type: text/html
Elvin-check: ok


<!-- Copyright (C) elvin.org 1998-2002 -->

<html>
  <head>
    <title>%s</title>
  </head>

  <body bgcolor="white">
    <table width="100%%" border="0" cellpadding="15">
      <tr bgcolor="#888888">
        <td colspan="2">
          <font color="white" size="+6" face="helvetica,arial">
            <i><b>elvin.org</b></i>
          </font>
        </td>
      </tr>

      <tr>
        <td colspan="2">
          <font face="helvetica,arial">

Notification formats are registered under a name, required to be
globally unique.  Normally, the name uses a DNS domain name (or at
least, the root of the domain name) owned by the organisation that
defines the format to ensure uniqueness.<p>

A particular format might have multiple versions defined as the
application evolves.  Increasing minor version numbers are used for
backward-compatible changes, while a change that is incompatible
requires a new major version number.<p>

In the following table, the version number is linked to the format
specification.<p>

          </font>
        </td>
      </tr>

      <tr>
        <td colspan="2" valign="top">

'''


web_trailer = '''

        </td>
      </tr>

      <tr bgcolor="#888888">
        <td colspan="2">
          <font color="white" size="-2" face="helvetica,arial">
            Copyright &copy; 2002&nbsp;&nbsp;&nbsp; 
            <a href="mailto:webmaster@elvin.org">webmaster@elvin.org</a>&nbsp;&nbsp;&nbsp;
             Last updated: $Date: 2002/03/29 07:35:15 $
          </font>
        </td>
      </tr>

    </table>
  </body>
</html>

'''

web_field = '''<tr>
  <td>%s</td>
  <td><a href="%s">v%s.%s</a></td>
</tr>

'''

########################################################################

def dumb():
    #-- write the defined fields
    for e in l_format:

	print "<tr>"
	print '<td valign="top"><input type="checkbox" name="del_%s" value="0"></td>'%e[0]
	print '<td valign="top">%s</td><td valign="top">%s</td><td valign="top">%s</td><td valign="top">%s</td>' % e
	print "</tr>"

    #-- default no-fields output
    if len(l_format) == 0:
	print default_fields

    #-- trailer
    print web_tail

    return


########################################################################

if __name__ == '__main__':

    #-- trap error output
    sys.stderr = sys.stdout
    
    try:
        res = ""
        
        #-- get list of all registered formats
        f_list = os.listdir(ORG_REGISTRY)
        f_list.sort()

        res += '<table cellpadding="8" border="1">'
        res += '<tr><th>Format</th><th>Version</th></tr>'
        
        for f_name in f_list:
            ver_idx = f_name.rfind(".")
            name_idx = f_name.rfind("-")

            format = f_name[:name_idx]
            major = f_name[name_idx+1:ver_idx]
            minor = f_name[ver_idx+1:]

            url = "%s%s/fshow.py?f_name=%s&f_major=%s&f_minor=%s" % \
                  (ORG_CGI_HOME,
                   ORG_CGI_FORMAT_ROOT,
                   format,
                   major,
                   minor)
            res += web_field % (format, url, major, minor)

        res += '</table>'

    except SystemExit:
	pass

    except:
	print web_header % ("Error", "error")
	print "<pre>"
        print "We had an exception ...\n"
        traceback.print_exc()
	print "</pre>"
	print web_trailer

    else:
        print web_header % ("elvin.org",)
        print res
        print web_trailer
        
    sys.exit(0)


########################################################################
