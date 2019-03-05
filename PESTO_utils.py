"""
This script contains utilities which are used when debugging the pipeline. They allow the user to look into the headers
of the image files (.fits) which are used to see quantities such as exposures, the filters used during observations, the 
size of the image in pixels, etc.
"""

import PESTO_lib
import sys
import os
from subprocess import run
from astropy.io import fits
import numpy as np
import time

           
def files_with_zero(self):
    """
    Input: None
    Return: None
    Checks for files with IMAGETYP == 'zero'. Prints any files which do.
    """
    for l in self.loc:
        files = os.listdir(l)
        for f in files:
            if '.fits' in f:
                hdr_temp = fits.open(l+'/'+f, mode = 'update')
                hdu = hdr_temp[self.hdr_ind[l]] # Modified: was 0
                if 'zero' in hdu.header['IMAGETYP']:
                    print(f)

def print_filters(self):
    """
    Input: None
    Return: None
    Prints the filters used for all .fits files in the directories in use.
    """
    for l in self.loc:
        files = os.listdir(l)
        print("\nLooking for filters in "+l+":")
        for f in files:
            if '.fits' in f:
                hdr_temp = fits.open(l+'/'+f)
                hdu = hdr_temp[self.hdr_ind[l]] # Modified: was 0
                if 'r' in hdu.header['filtre']:
                    print('r filter: '+f)
                if 'g' in hdu.header['filtre']:
                    print('g filter: '+f)
                if 'i' in hdu.header['filtre']:
                    print('i filter: '+f)
                if 'z' in hdu.header['filtre']:
                    print('z filter: '+f)
                if 'Ha' in hdu.header['filtre']:
                    print('Ha filter: '+f)
                if 'N/A' in hdu.header['filtre']:
                        print('N/A filter: '+f)
    
def print_NAXES(self):
    """
    Input: None
    Return: None
    Prints the values of NAXIS1 & NAXIS2 used for all .fits files in the directories in use.
    """
    for l in self.loc:
        files = os.listdir(l)
        print("\nLooking for NAXIS1 & NAXIS2 in "+l+":")
        for f in files:
            if '.fits' in f:
                hdr_temp = fits.open(l+'/'+f)
                hdu = hdr_temp[self.hdr_ind[l]] # Modified: was 0
                print(f+': NAXIS1='+str(hdu.header['NAXIS1'])+', NAXIS2='+str(hdu.header['NAXIS2']))

def print_WCS_headers(self):
    """
    Input: None
    Return: None
    Prints the values of RA and DEC headers used for all .fits files in the directories in use.
    """
    for l in self.loc:
        files = os.listdir(l)
        print("\nLooking for RA & DEC in "+l+":")
        time.sleep(10)
        for f in files:
            if '.fits' in f:
               hdr_temp = fits.open(l+'/'+f)
               hdu = hdr_temp[self.hdr_ind[l]] # Modified: was 0
               print(f+': RA='+str(hdu.header['RA'])+', DEC='+str(hdu.header['DEC']))

def print_objects(self):
    """
    Input: None
    Return: None
    Prints the values of OBJECT headers used for all .fits files in the directories in use.
    """
    for l in self.loc:
        files = os.listdir(l)
        print("\nLooking for OBJECTs in "+l+":")
        for f in files:
            if '.fits' in f:
                hdr_temp = fits.open(l+'/'+f)
                hdu = hdr_temp[self.hdr_ind[l]] # Modified: was 0
                print(f+': OBJECT='+hdu.header['OBJECT'])

def print_exposures(self):
    """
    Input:None
    Return: None
    Prints the values of OBJECT headers used for all .fits files in the directories in use.
    """
    for l in self.loc:
        files = os.listdir(l)
        print("\nLooking for EXPOSUREs in "+l+":")
        for f in files:
            if '.fits' in f:
                hdr_temp = fits.open(l+'/'+f)
                hdu = hdr_temp[self.hdr_ind[l]] # Modified: was 0
                print(f+': EXPOSURE= '+str(hdu.header['EXPOSURE']))
