hyperspec_unmix
===============

This Repository contains python codes for hyperspectral image unmixing

Algorithm included:
NMF (Nonnegative Matrix Factorization)

- math model: Y = A*S
- method used:
- > Lee Seung Multiplicative Update (LSMU)
- > using Hierarchical Alternating Least Squares (HALS)
- > using Alternating Nonnegative Least Squares (NNLS)

SPA (Successive Projection Algorithm)

General Utilities


Background:
Hyperspectral Image Unmixing using Nonnegative Matrix factorization

Hyperspectral unmixing (HU) has become a popular research topic in many applications.
The objective is to separate a spectrum into a sum of basic spectra.
The source of the spectral signal can be from satellite hyperspectral images.
For a spectral image pixel, solving the HU problem gives two information of this pixel, namely the basic spectra and the corresponding abundance.

Spectral images can be modelled as nonnegative matrices and thus HU can be carried out by non-negative matrix factorization (NMF)as for every pixel the spectra and their abundance always take non-negative values in nature.
