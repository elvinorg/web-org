#! /opt/local/bin/python2.2
########################################################################
#
#              elvin.org web
#              notification format registry
#
# File:        $Source: /Users/d/work/elvin/CVS/web-org/cgi-bin/formats/fshow.py,v $
# Version:     $RCSfile: fshow.py,v $ $Revision: 1.3 $
# Copyright:   (C) 1998-2003 elvin.org
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

ORG_SERVER = "http://www.elvin.org"
ORG_ROOT = ""
ORG_CGI_HOME = "http://www.elvin.org/cgi-bin"
ORG_CGI_FORMAT_ROOT = "/formats"
ORG_REGISTRY = "/data/www/www.elvin.org/docs/regs/formats/registry"
#ORG_REGISTRY = "/home/d/work/web/web-org/regs/formats/registry"

########################################################################

import base64, cgi, os, pickle, sys, getopt, random, string, time, traceback, urllib


########################################################################

web_header = '''Content-type: text/html
Elvin-check: ok


<!-- Copyright (C) elvin.org 1998-2003 -->

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

'''


web_trailer = '''

        </td>
      </tr>

      <tr bgcolor="#888888">
        <td colspan="2">
          <font color="white" size="-2" face="helvetica,arial">
            Copyright &copy; 2002-2003&nbsp;&nbsp;&nbsp; 
            <a href="mailto:webmaster@elvin.org">webmaster@elvin.org</a>&nbsp;&nbsp;&nbsp;
             Last updated: $Date: 2003/11/07 13:12:27 $
          </font>
        </td>
      </tr>

    </table>
  </body>
</html>

'''


web_owner = """

<table width="100%%" border="0" cellpadding="4">
<tr>
<th valign="top" align="left" width="15%%">Name</th>
<td colspan="4" width="85%%">%s</td>
</tr>

<tr>
<th valign="top" align="left">Version</th>
<td colspan="4">%s</td>
</tr>

<tr>
<td valign="top" align="left" width="15%%"><b>Replaces</b></td>
<td valign="top" align="left" >%s</td>
<td valign="top" align="left" ><b>Replaced by</b></td>
<td valign="top" align="left" >%s</td>
<td valign="top" align="left" width="50%%">&nbsp;</td>
</tr>

<tr>
<th valign="top" align="left">Summary</th>
<td colspan="4">
<pre>%s</pre>
</td>
</tr>

<tr>
<th valign="top" align="left">URL</th>
<td colspan="4"><a href="%s">%s</a></td>
</tr>

<tr>
<th valign="top" align="left">Owner</th>
<td colspan="4"><a href="mailto:%s">%s</a></td>
</tr>
</table>

<br><br>

<table align="right" width="90%%" border="1" cellpadding="4">
<tr>
<th align="left" width="20%%">Name</th>
<th align="left" width="10%%">Type</th>
<th align="left" width="10%%">Opt/Mand</th>
<th align="left" width="60%%">Description</th>
</tr>

"""

web_field = """
<tr>
<td valign="top">%s</td>
<td valign="top">%s</td>
<td valign="top">%s</td>
<td valign="top">%s</td>
</tr>

"""

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
        form = cgi.FieldStorage()

        #-- check for cancel
        if form.has_key("action") and form["action"].value == "Cancel":
            print "Status: 302 Redirected"
            print "Location: " + form["referer"].value
            print
            sys.exit(0)

	#-- get format spec
	f_name = form["f_name"].value
	f_major = form["f_major"].value
	f_minor = form["f_minor"].value

	file_name = '%s-%s.%s' % (f_name, f_major, f_minor)
	url = "%s%s/regs/formats/registry/%s" % (ORG_SERVER, ORG_ROOT, file_name)

	#-- open format file
	try:
	    f = urllib.urlopen(url)

	#-- catch errors with web server
	except:
	    print web_header % ("Error", "error")
	    print "<pre>A problem occured loading the format definition.</pre>"
	    print web_trailer
	    sys.exit(0)

	#-- check document
	#if not f.info().has_key("Content-type") or f.info()["Content-type"] != "text/plain":
        if not f.info().has_key("Content-type"):
	    print web_header % ("Error", "error")
	    print "<pre>The loaded definition file appears to be missing or corrupt.</pre>"
	    print web_trailer
	    sys.exit(0)

	lines = f.readlines()
	f.close()

	#-- parse data
	summary = ""
	desc = ""
	fields = []
	flg_sum = 0
	flg_field = 0

	for line in lines[6:]:
	    if not flg_sum:
		if string.strip(line) != "%%":
		    summary = summary + line
		else:
		    flg_sum = 1

	    elif flg_field == 0:
		f_name = line
		flg_field = 1

	    elif flg_field == 1:
		f_type = line
		flg_field = 2

	    elif flg_field == 2:
		f_opt = line
		flg_field = 3

	    elif flg_field == 3:
		if string.strip(line) == "%%":
		    flg_field = 0
		    fields.append((f_name, f_type, f_opt, desc))
		    desc = ""

		else:
		    desc = desc + line

	#-- previous version
	if string.strip(lines[2]):
	    f_replaces = '<a href="%s?f_name=%s&f_major=%s&f_minor=%s">%s</a>' % \
			 ("%s%s/fshow.py" % (ORG_CGI_HOME, ORG_CGI_FORMAT_ROOT),
			  string.strip(lines[0]), 
			  string.split(string.strip(lines[2]), ".")[0],
			  string.split(string.strip(lines[2]), ".")[1],
			  string.strip(lines[2]))
	else:
	    f_replaces = "&nbsp;-&nbsp;"

	#-- newer version
	if string.strip(lines[3]):
	    f_replaced = '<a href="%s?f_name=%s&f_major=%s&f_minor=%s">%s</a>' % \
			 ("%s%s/fshow.py" % (ORG_CGI_HOME, ORG_CGI_FORMAT_ROOT),
			  string.strip(lines[0]), 
			  string.split(string.strip(lines[3]), ".")[0],
			  string.split(string.strip(lines[3]), ".")[1],
			  string.strip(lines[3]))
	else:
	    f_replaced = "&nbsp;-&nbsp;"

	#-- start writing HTML
	print web_header % (file_name)

	print web_owner % (lines[0], 
			   lines[1], 
			   f_replaces,
			   f_replaced,
			   summary, 
			   lines[4], lines[4], 
			   lines[5], lines[5])

	#-- write out fields
	for field in fields:
	    print web_field % field

	#-- complete page
	print "</table>"
	print web_trailer


    except SystemExit:
	pass

    except:
	print web_header % ("Error")
	print "<pre>"
        print "We had an exception ...\n"
        traceback.print_exc()
	print "</pre>"
	print web_trailer

    sys.exit(0)


########################################################################
