#! /usr/bin/python2.0
########################################################################
#
#              elvin.org web
#              notification format registry
#
# File:        $Source: /Users/d/work/elvin/CVS/web-org/cgi-bin/formats/freg.py,v $
# Version:     $RCSfile: freg.py,v $ $Revision: 1.1 $
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
""" """

########################################################################
#
#  configuration settings
#

ORG_HOME      = "http://www.elvin.org"
ORG_FREG_PY   = ORG_HOME + "/cgi-bin/formats/freg.py"
ORG_MAIL      = "mailto:webmaster@elvin.org"
ORG_COPYRIGHT = "1998-2002 elvin.org"
ORG_MAILHOST  = "mailhost.dstc.edu.au"
ORG_WEB_OWNER = "elvin@dstc.edu.au"
ORG_FREG_USER = "davida@pobox.com"


########################################################################

import base64, cgi, os, pickle, sys, getopt, random, smtplib, socket, string, time, traceback


########################################################################

web_head = '''Content-type: text/html


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

'''


web_defn = '''

Select the <b>Del</b> checkbox to remove an element or specify
additional elements below.
<p>

<form method="post" action="''' + ORG_FREG_PY + '''">
<input type="hidden" name="rqst" value="%s">

<table width="100%%" border="0" cellpadding="4" bgcolor="#dddddd">

<tr>
<td width="9%%" ><b>Del?</b></td>
<td width="17%%"><b>Name</b></td>
<td width="17%%"><b>Type</b></td>
<td width="17%%"><b>Opt/Mand</b></td>
<td width="40%%"><b>Description</b></td>
</tr>

'''


default_fields = '''
<tr>
<td colspan="5" align="center"><i>no elements defined</i></td>
</tr>
'''


web_error = '''
<h2>Error!</h2>

There was an error registering your request.  Please use the
"previous page" function of your browser to retry the registration.
<p>

If that fails, then you should <a
href="''' + ORG_MAIL + '''">email us</a> and we will try to sort out
the problem.
<p>
'''

web_ok = """
<h2>Completed!</h2>

Your request has been registered.  The specified format will be
checked and registered if there are no errors.  Any problems will be
resolved by email to the format owner's address.
<p>

Return to the <a href="%s">notification formats  page</a>.
<p>
"""


web_tail = '''
</table>

<h2>Add New Element</h2>

<table width="100%" border="0" cellpadding="4" bgcolor="#dddddd">
<tr>
<th align="left">Name</th>
<td colspan="5">
  <input type="text" name="name" size="42"><br>

  <font size="-1">
    Field name.  It is recommended that field names use both shift
    case and hyphens between words, similarly to the RFC-2822 email
    standard.  For example, <tt>The-Field-Name</tt>.
  </font>
</td>
</tr>

<tr>
<th align="left">Type</th>
<td><input type="radio" name="type" value="string" checked>&nbsp;String</td>
<td><input type="radio" name="type" value="int32">&nbsp;Int32</td>
<td><input type="radio" name="type" value="int64">&nbsp;Int64</td>
<td><input type="radio" name="type" value="float">&nbsp;Float</td>
<td><input type="radio" name="type" value="opaque">&nbsp;Opaque</td>
</tr>

<tr>
<th align="left">Mandatory?</th>
<td colspan="5">
  <input type="checkbox" name="mand" value="M"><br>
  <font size="-1">
    Is this field always required?  Fields that have inter-dependent
    requirements should have this explained in the description.
  </font>
</td>
</tr>

<tr>
<th align="left" valign="top">Description</th>
<td colspan="5">
  <textarea name="desc" rows="5" cols="40" wrap="hard"></textarea><br>
  <font size="-1">
    A short description of the purpose of the field, including any
    dependencies on other fields.
  </font>
</td>
</tr>

</table>

<p>

<table width="100%" border="0" cellpadding="4">
<tr>
<td align="center"><input type="submit" value="Done" name="action"></td>
<td align="center"><input type="submit" value="Apply" name="action"></td>
<td align="center"><input type="submit" value="Cancel" name="action"></td>
</tr>
</table>

</form>

'''


web_trailer = '''

        </td>
      </tr>

      <tr bgcolor="#888888">
        <td colspan="2">
          <font color="white" size="-2" face="helvetica,arial">
            Copyright &copy; 2002&nbsp;&nbsp;&nbsp; 
            <a href="mailto:webmaster@elvin.org">webmaster@elvin.org</a>&nbsp;&nbsp;&nbsp;
             Last updated: $Date: 2002/03/29 07:35:12 $
          </font>
        </td>
      </tr>

    </table>
  </body>
</html>

'''

########################################################################

def encode(obj_in):
    """ """
    
    str_tmp = pickle.dumps(obj_in)
    str_tmp = base64.encodestring(str_tmp)
    
    str_tmp = string.replace(str_tmp, '\012', r'\x0a')
    str_tmp = string.replace(str_tmp, '=',    r'\x3d')
    str_tmp = string.replace(str_tmp, '+',    r'\x2b')

    return str_tmp


def decode(str_in):
    """ """
    str_tmp = string.replace(str_in,  r'\x0a', '\012')
    str_tmp = string.replace(str_tmp, r'\x3d', '=')
    str_tmp = string.replace(str_tmp, r'\x2b', '+')

    str_tmp = base64.decodestring(str_tmp)

    return pickle.loads(str_tmp)


def print_elements(f_name, f_major, f_minor, f_url, f_mail, f_summary, l_format, referer):
    """ """

    #-- start writing the output
    print web_head
    print web_defn % encode(l_format)

    #-- hidden data
    print '<input type="hidden" name="f_name"    value="%s">' % f_name
    print '<input type="hidden" name="f_major"   value="%s">' % f_major
    print '<input type="hidden" name="f_minor"   value="%s">' % f_minor
    print '<input type="hidden" name="f_url"     value="%s">' % f_url
    print '<input type="hidden" name="f_mail"    value="%s">' % f_mail
    print '<input type="hidden" name="f_summary" value="%s">' % f_summary
    print '<input type="hidden" name="referer"   value="%s">' % referer

    #-- version and name
    print "<tr>"
    print '<td valign="top">&nbsp;</td>'
    print '<td valign="top">%s</td><td valign="top">%s</td><td valign="top">%s</td><td valign="top">%s %s<br><br></td>' % (f_name, "int32", "M", f_major, "- Major version number")
    print "</tr>"

    print "<tr>"
    print '<td valign="top">&nbsp;</td>'
    print '<td valign="top">%s</td><td valign="top">%s</td><td valign="top">%s</td><td valign="top">%s %s<br><br></td>' % ("minor", "int32", "M", f_minor, "- Minor version number")
    print "</tr>"

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
    print web_trailer
    
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

	f_name = form["f_name"].value
	f_major = form["f_major"].value
	f_minor = form["f_minor"].value
	f_url = form["f_url"].value
	f_mail = form["f_mail"].value
	f_summary = form["f_summary"].value
	referer = form["referer"].value

        #-- first or subsequent use?
        if form.has_key("rqst"):
            l_format = decode(form["rqst"].value)

	    #-- delete checked elements
	    for key in form.keys():
		if key[:4] == "del_":
		    for e in l_format:
			if e[0] == key[4:]:
			    l_format.remove(e)

	    #-- append new elements
	    if form.has_key("name"):
		e_name = form["name"].value
		e_type = form["type"].value
		e_mand = form.has_key("mand") and form["mand"].value or "O"
		e_desc = form["desc"].value

		#-- validate new field
                #fixme!
		pass

		l_format.append((e_name, e_type, e_mand, e_desc))

	    #-- check for done
	    if form.has_key("action") and form["action"].value == "Done":

		#-- create rego string
		s = "Subject: [elvin.org] notification format request\n\n"
		s = s + "%s\n" % f_name
		s = s + "%s.%s\n" % (f_major, f_minor)
		s = s + "\n\n"                          #FIXME: prev/next?
		s = s + "%s\n" % f_url
		s = s + "%s\n" % f_mail
		s = s + "%s\n" % f_summary
		s = s + "%%\n"

		for e in l_format:
		    s = s + "%s\n%s\n%s\n%s\n%%%%\n" % e

		#-- mail rego request
		try:
		    mailer = smtplib.SMTP(ORG_MAILHOST)
		    mailer.sendmail(ORG_FREG_USER, [ORG_FREG_USER], s)
		    mailer.quit()
				
		except:
		    print web_head
		    print web_error
		    print "<pre>"
		    traceback.print_exc()
		    print "</pre>"
		    print web_trailer

		else:
		    print web_head
		    print web_ok % form["referer"].value
		    print web_trailer

		#-- exit
		sys.exit(0)

	    else:
		print_elements(f_name, f_major, f_minor, f_url, f_mail, f_summary, l_format, referer)

        else:
            l_format = []
	    f_name = form["f_name"].value
	    f_major = form["f_major"].value
	    f_minor = form["f_minor"].value
	    f_url = form["f_url"].value
	    f_mail = form["f_mail"].value
	    f_summary = form["f_summary"].value

	    #-- write the defined fields
	    print_elements(f_name, f_major, f_minor, f_url, f_mail, f_summary, l_format, referer)


    except SystemExit:
	pass

    except:
        print "Content-type: text/plain\n\n"
        print "had an exception ...\n"

        traceback.print_exc()

        
    sys.exit(0)


########################################################################

