################################################################
# 
# Project:  Elvin
# File:     $Source: /Users/d/work/elvin/CVS/web-org/Makefile,v $
#
################################################################
#
#  add more source files here
#
RAW_FILES := 
SRC_FILES := $(wildcard *.htmi)
SUB_DIRS  := papers regs specs cgi-bin
TARGET    := .

################################################################
#  anything after here shouldn't need to be changed (much!)
################################################################

INCLUDE := .
include $(INCLUDE)/Makefile.config

$(GEN_FILES): Makefile \
	$(INCLUDE)/Makefile.config \
	$(INCLUDE)/org.m4

################################################################

