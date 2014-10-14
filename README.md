hyperspec_unmix
===============

This Repository contains python codes for hyperspectral image unmixing

==============
 Code Summary
==============
~~~~~~~~
 NMF.py
~~~~~~~~
--------------------------------------
NMF (Nonnegative Matrix Factorization)
mathematical model: Y - A * S         
where Y is known and A , S are unknown
--------------------------------------
Functions included:
LSMU() ( Lee Seung Multiplicative Update        )
HALS() ( Hierarchical Alternating Least Squares )
NNLS() ( Alternating Nonnegative Least Squares  )


~~~~~~~~
 DSP.py
~~~~~~~~
Functions included:
-------------------------------------------
SPA helps identified the purest spectral   
signitures from a given Hyperspectral image
if pure pixel assumption is ensured and    
the number of existing substance is known  
-------------------------------------------
SPA() (Successive Projection Algorithm)


STOP()         ( pause the system from running if a file 'stop' is detected                   )
READMATRIX()   ( read a general matrix from a text file                                       )
READUSGSDATA() ( read hyperspectral signature data provided by USGS Spectroscopy Lab. Library )
               ( link: http://speclab.cr.usgs.gov/spectral.lib06/ds231/datatable.html         )
PLOT()         ( a function similar to MATLAB(R) plot by using python library matplotlib.plot )


===================
 Theory Background
===================
Hyperspectral Image Unmixing using Nonnegative Matrix factorization

Hyperspectral unmixing (HU) has become a popular research topic in many applications.
The objective is to separate a spectrum into a sum of basic spectra.
The source of the spectral signal can be from satellite hyperspectral images.
For a spectral image pixel, solving the HU problem gives two information of this pixel, namely the basic spectra and the corresponding abundance.

Spectral images can be modelled as nonnegative matrices and thus HU can be carried out by non-negative matrix factorization (NMF)as for every pixel the spectra and their abundance always take non-negative values in nature.
