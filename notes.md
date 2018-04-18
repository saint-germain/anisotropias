
https://arxiv.org/abs/1612.09263


TF FP are secondary (Tully et al 2016) http://iopscience.iop.org/article/10.3847/0004-6256/152/2/50/meta http://iopscience.iop.org/article/10.3847/0004-6256/152/2/50/pdf -> "There are both random and systematic uncertainties in the estimate of H 0 . The largest random uncertainty ( ± 0.079 in the modulus ) lies with the zero-point calibration to the TF relation based on 33 galaxies with Cepheid or TRGB distances. The SNI a zero point is directly established through 9 Cepheid distances and less directly established through over 100 group af fi liations and has an uncertainty of ± 0.046. Then there is an uncertainty of ± 0.030 for the fi t to the mean Hubble parameter in Figure 13 . Added in quadrature, the random error is ± 0.096, 4.5% in distance and affect on H 0 . Systematic effects are harder to quantify, but the components of concern and estimates of uncertainties are the Cepheid and TRGB zero points ( ± 0.05 ) ,possible variations in SNI a properties that manifest in distance ( Rigault  et  al. 2015 ; ± 0.05 ) ,  and  uncertainties  in  the cosmological model corrections ( ± 0.027 ) . Systematics crudely add in quadrature to 0.076, 3.5% in distance and H 0 . ->

The distance moduli, both for individual galaxies and again for groups, are weighted averages with individual weights w_i = 1/e_i^2 where the uncertainty in a modulus is e_i , giving total weights w_t=Sum w_i, and error on the averaged modulus e_mu = 1/w_t^1/2 (QUADRATURE, GCM). For groups with many distance measures this formal error is as small as 0.02 mag, three times smaller than reasonable expectations of systematic errors."

From NED paper "Err (mag) and Est. with Err (%) represent mean of errors published, given in  units of  magnitude (m - M) , and percentage of number of estimates in total for which error  is  available" in final page. 

From NED-D "Redshift: appears only in cases where the distance modulus is published as a "luminosity distance modulus", as provided mostly for Type Ia supernova (SNIa), showing the target redshift used to transform each "luminosity distance modulus" given to the corresponding "metric distance", via m-M(L) = [5 logD/(1+z)]/5."

"Many  T ype Ia and some  T ype II supernovae estimates for example, are based not on the  linear or proper motion  distance modulus, m - M = 5 logD - 5 ,  with D in  parsecs ( pc ) , but  rather on the luminosity distance modulus, m - M = 5logD - 5/(1+z), e.g., Lang (1980)"

Idea: Multi-method analysis?
Idea: Distance difference from reported D in object page -> "Mean distances and errors can also be found, where available, in each individual galaxy’s  data summary page. Mean distances for large numbers of galaxies can be retrieved via  the Build Data Ta ble service on NED’s main interface. Either the names or coordinates of  galaxies may be entered as input"

To do: Check candidate methods for no H or LMC bs. Do not go near Cepheids.
To do (JC): Read description of candidate methods in list:

TRGB, CMD, RR Lyrae, Eclipsing Binary, Red Clump, PNLF, SZ effect, Brightest Stars, Horizontal Branch


"To place estimates on a uniform scale, they must first be sorted by the Hubble constant  assumed, and estimates affected by differences from the default value must be  standardized .  Once placed on a unifo rm basis with the default value, mean distance (s) can be obtained. Further, once standardized to the default value, estimates can be adjusted  en masse  to obtain mean distance(s) based on any value of the Hubble constant."

Check for both those things, for TF shouldn't be a problem, but still...

"Tully -‐ Fisher: introduced by Tully & Fisher (1977), based on the absolute blue magnitudes of spiral galaxies, which depend on their apparent blue magnitude, m B , and their maximum r otational velocity, sigma: M B = - 7.0 log sigma -‐ 1.8 ( e.g. , Karachentsev et al. 2003). So, the galaxy NGC 0247 has an absolute blue magnitude of M B = -‐ 18.2, based on its rotational velocity, sigma = 222 km s -‐ 1 . With an apparent blue magnitude of m B = 9.86, NGC 0247 has a distance modulus of (m -‐ M) B = 28.1, f or a distance of 4.1 Mpc"

- Efforts to reduce the uncertainty in the estimate the Hubble constant are single-method such as SNIa \citet{hubsn2018}.
- Bayesian analysis of systematic uncertainties for cosmology when using SNIa-derived galactic parameters (heterogeneous errors) \citet{unity}. 
- Hubble constant MCMC estimation based on Cepheids distance determination for NGC 4258 \citet{hubngc}. 
- \citet{hub2010} is the important hubble paper, although the original hubble estimation from redshift independent distances is \citet{huborig}. 
- \citet{ridsn} estimates distances using SNIa but no redshifts. 
- \citet{riess} is the 2.4 percent determination of hubble constant. 
- Changes in Hubble constant estimation using TF relation without Cepheids \citet{noceph}.
- GW searches \citet{gwgallist}, we should improve redshift independent distance determination .
- Determining the spatial distribution of galaxies in order to study large-scale structure \citet{gallargescale} or local universe peculiar velocities \citet{localunipv}. Kinematics of nearby galaxies in void \citet{void}
- \citet{6df} attempt to predict redshift-derived distance errors within a Bayesian framework yields 26\%.
- Studies of anisotropy be it of morphological types \citet{morphanis} or density-velocity \citet{nongauss}
- Determining whether a galaxy belongs to a group by analyzing their common properties \citet{gg3500} with conclusions regarding the halo mass function
- Anisotropy hubble from HST data \citet{anishub} and from NED-D \citet{tecciencia}. 
- 10\% estimated uncertainty for photometrically derived distance scale ladder \citet{hubunc}.
- \citet{locunivcf} local universe structure reconstruction Cosmicflows-1
- \citet{precisetf} corrected the TF method for uncertainties in galaxy inclinations. \citet{tf07dist}
-   \citet{said} has used emcee for Tully-Fisher in the southern Zone of Avoidance.
- \citet{hyperleda} does not give a prescription for error estimation.

-  UNUSED - which also need to take into account instrument detection limits \citet{catmatch} and source identification \citet{baymatch}. Importance of distance and catalogs \citet{catetg,catspi} in: Exploration of prior discrepancy modeling in model estimation \citet{priordisc}
