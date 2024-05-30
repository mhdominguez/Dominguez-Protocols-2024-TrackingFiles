# Dominguez-Protocols-2024-TrackingFiles
Configuration and other files for handling example data with LSFMProcessing, F-TGMM, SVF, and MaMuT.  To be published with "4-dimension light sheet imaging and cell tracking in mouse embryos" in ___ (2024).
<br>

## intermediate-data
#### Source data containing intermediate steps of the computational cell tracking workflow using F-TGMM and SVF.
See below for files in this directory.
<br>

## luts
#### Fiji-compatible lookup tables for pseudocoloring projection images for presentation.
Can be used with MIP->AVI macros in [LSFMProcessing](https://github.com/mhdominguez/LSFMProcessing).
<br>

## SVF
#### Configuration files for converting [raw TGMM data]([raw/main/intermediate-data/](https://github.com/mhdominguez/Dominguez-Protocols-2024-TrackingFiles/raw/main/intermediate-data/TGMM_result.tar.gz) to MaMuT via SVF. 
For the `tissue-bw-prop.py` step when using included [raw TGMM data]([intermediate-data](https://github.com/mhdominguez/Dominguez-Protocols-2024-TrackingFiles/raw/main/intermediate-data/TGMM_result.tar.gz), you will need [t00004-6tissue.tif](https://github.com/mhdominguez/Dominguez-Protocols-2024-TrackingFiles/raw/main/intermediate-data/t00004-6tissue.tif) to label the tissue types. Available in [intermediate-data](intermediate-data) are [SVF result](https://github.com/mhdominguez/Dominguez-Protocols-2024-TrackingFiles/raw/main/intermediate-data/SVF_to_MaMuT_output.xml.gz) and [MaMuTLibrary](https://github.com/mhdominguez/MaMuTLibrary)-processed [single tissue .xml datasets](https://github.com/mhdominguez/Dominguez-Protocols-2024-TrackingFiles/raw/main/intermediate-data/SVF_4tissue_datasets.tar.gz), the latter of which can be analyzed with the included SVFdata_vlnplot.py.
<br>

## TGMM
#### Configuration files and shell scripts for running F-TGMM and post-handling of raw .xml data. 
You will need a raw .klb (or .tif) dataset to run TGMM. Available in [intermediate-data](intermediate-data) are a [raw TGMM solution](https://github.com/mhdominguez/Dominguez-Protocols-2024-TrackingFiles/raw/main/intermediate-data/TGMM_result.tar.gz) from our example dataset.
<br>

## References
1.	Dominguez, M.H., Krup, A.L., Muncie, J.M., and Bruneau, B.G. (2023). Graded mesoderm assembly governs cell fate and morphogenesis of the early mammalian heart. Cell 186, 479-496.e23. 10.1016/j.cell.2023.01.001.
<br><br>
2.	McDole, K., Guignard, L., Amat, F., Berger, A., Malandain, G., Royer, L.A., Turaga, S.C., Branson, K., and Keller, P.J. (2018). In Toto Imaging and Reconstruction of Post-Implantation Mouse Development at the Single-Cell Level. Cell 175, 859-876.e33. 10.1016/j.cell.2018.09.031.
<br><br>
3.	Amat, F., Lemon, W., Mossing, D.P., McDole, K., Wan, Y., Branson, K., Myers, E.W., and Keller, P.J. (2014). Fast, accurate reconstruction of cell lineages from large-scale fluorescence microscopy data. Nat Methods 11, 951–958. 10.1038/nmeth.3036.
<br><br>
4.	Saga, Y., Miyagawa-Tomita, S., Takagi, A., Kitajima, S., Miyazaki, J. i, and Inoue, T. (1999). MesP1 is expressed in the heart precursor cells and required for the formation of a single heart tube. Development 126, 3437–3447.
<br><br>
5.	Devine, W.P., Wythe, J.D., George, M., Koshiba-Takeuchi, K., and Bruneau, B.G. (2014). Early patterning and specification of cardiac progenitors in gastrulating mesoderm. Elife 3. 10.7554/eLife.03848.
<br><br>
6.	Dodou, E., Verzi, M.P., Anderson, J.P., Xu, S.-M., and Black, B.L. (2004). Mef2c is a direct transcriptional target of ISL1 and GATA factors in the anterior heart field during mouse embryonic development. Development 131, 3931–3942. 10.1242/dev.01256.
<br><br>
7.	Cai, C.-L., Liang, X., Shi, Y., Chu, P.-H., Pfaff, S.L., Chen, J., and Evans, S. (2003). Isl1 Identifies a Cardiac Progenitor Population that Proliferates Prior to Differentiation and Contributes a Majority of Cells to the Heart. Dev Cell 5, 877–889.
<br><br>
8.	Schindelin, J., Arganda-Carreras, I., Frise, E., Kaynig, V., Longair, M., Pietzsch, T., Preibisch, S., Rueden, C., Saalfeld, S., Schmid, B., et al. (2012). Fiji: an open-source platform for biological-image analysis. Nat Methods 9, 676–682. 10.1038/nmeth.2019.
<br><br>
9.	Hörl, D., Rojas Rusak, F., Preusser, F., Tillberg, P., Randel, N., Chhetri, R.K., Cardona, A., Keller, P.J., Harz, H., Leonhardt, H., et al. (2019). BigStitcher: reconstructing high-resolution image datasets of cleared and expanded samples. Nature Methods 16, 870–874. 10.1038/s41592-019-0501-0.
<br><br>
10.	Wolff, C., Tinevez, J.-Y., Pietzsch, T., Stamataki, E., Harich, B., Guignard, L., Preibisch, S., Shorte, S., Keller, P.J., Tomancak, P., et al. (2018). Multi-view light-sheet imaging and tracking with the MaMuT software reveals the cell lineage of a direct developing arthropod limb. Elife 7. 10.7554/eLife.34410.
<br><br>
11.	Bedzhov, I., and Zernicka-Goetz, M. (2014). Self-Organizing Properties of Mouse Pluripotent Cells Initiate Morphogenesis upon Implantation. Cell 156, 1032–1044. 10.1016/j.cell.2014.01.023.
<br><br>
12.	Harrison, S.E., Sozen, B., Christodoulou, N., Kyprianou, C., and Zernicka-Goetz, M. (2017). Assembly of embryonic and extraembryonic stem cells to mimic embryogenesis in vitro. Science 356. 10.1126/science.aal1810.
<br><br>
13.	Glanville-Jones, H.C., Woo, N., and Arkell, R.M. (2013). Successful whole embryo culture with commercially available reagents. Int. J. Dev. Biol. 57, 61–67. 10.1387/ijdb.120098ra.
<br><br>
14.	Tyser, R.C., Miranda, A.M., Chen, C.-M., Davidson, S.M., Srinivas, S., and Riley, P.R. (2016). Calcium handling precedes cardiac differentiation to initiate the first heartbeat. Elife 5. 10.7554/eLife.17113.
<br><br>
15.	Shea, K., and Geijsen, N. (2007). Dissection of 6.5 dpc mouse embryos. J Vis Exp, 160. 10.3791/160.
<br><br>
16.	Pryor, S.E., Massa, V., Savery, D., Greene, N.D.E., and Copp, A.J. (2012). Convergent extension analysis in mouse whole embryo culture. Methods Mol Biol 839, 133–146. 10.1007/978-1-61779-510-7_11.
<br><br>
17.	Preibisch, S., Amat, F., Stamataki, E., Sarov, M., Singer, R.H., Myers, E., and Tomancak, P. (2014). Efficient Bayesian-based multiview deconvolution. Nat Methods 11, 645–648. 10.1038/nmeth.2929.
<br><br>
18.	Malin-Mayor, C., Hirsch, P., Guignard, L., McDole, K., Wan, Y., Lemon, W.C., Kainmueller, D., Keller, P.J., Preibisch, S., and Funke, J. (2023). Automated reconstruction of whole-embryo cell lineages by learning from sparse annotations. Nat Biotechnol 41, 44–49. 10.1038/s41587-022-01427-7.
