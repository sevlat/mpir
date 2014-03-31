/* Generated by tuneup.c, 2014-03-21, gcc 4.4 */

#define MUL_KARATSUBA_THRESHOLD          16
#define MUL_TOOM3_THRESHOLD             105
#define MUL_TOOM4_THRESHOLD             246
#define MUL_TOOM8H_THRESHOLD            303

#define SQR_BASECASE_THRESHOLD            0  /* always (native) */
#define SQR_KARATSUBA_THRESHOLD          26
#define SQR_TOOM3_THRESHOLD             162
#define SQR_TOOM4_THRESHOLD             268
#define SQR_TOOM8_THRESHOLD             348

#define POWM_THRESHOLD                  619

#define DIVREM_1_NORM_THRESHOLD       MP_SIZE_T_MAX  /* never */
#define DIVREM_1_UNNORM_THRESHOLD     MP_SIZE_T_MAX  /* never */
#define MOD_1_NORM_THRESHOLD              0  /* always */
#define MOD_1_UNNORM_THRESHOLD            0  /* always */
#define USE_PREINV_DIVREM_1               1  /* native */
#define USE_PREINV_MOD_1                  1
#define DIVEXACT_1_THRESHOLD              0  /* always */
#define MODEXACT_1_ODD_THRESHOLD          0  /* always (native) */
#define MOD_1_1_THRESHOLD                 6
#define MOD_1_2_THRESHOLD                 8
#define MOD_1_3_THRESHOLD                19
#define DIVREM_HENSEL_QR_1_THRESHOLD    996
#define RSH_DIVREM_HENSEL_QR_1_THRESHOLD      5
#define DIVREM_EUCLID_HENSEL_THRESHOLD      8

#define MUL_FFT_FULL_THRESHOLD         3904

#define SQR_FFT_FULL_THRESHOLD         2880

#define MULLOW_BASECASE_THRESHOLD         4
#define MULLOW_DC_THRESHOLD              27
#define MULLOW_MUL_THRESHOLD           5143

#define MULHIGH_BASECASE_THRESHOLD       10
#define MULHIGH_DC_THRESHOLD             27
#define MULHIGH_MUL_THRESHOLD          2966

#define MULMOD_2EXPM1_THRESHOLD          20

#define SB_DIVAPPR_Q_SMALL_THRESHOLD      0  /* always */
#define SB_DIV_QR_SMALL_THRESHOLD         0  /* always */
#define DC_DIV_QR_THRESHOLD              30
#define INV_DIV_QR_THRESHOLD           2089
#define INV_DIVAPPR_Q_N_THRESHOLD        30
#define DC_DIV_Q_THRESHOLD               44
#define INV_DIV_Q_THRESHOLD            1470
#define DC_DIVAPPR_Q_THRESHOLD           63
#define INV_DIVAPPR_Q_THRESHOLD       16039
#define DC_BDIV_QR_THRESHOLD             36
#define DC_BDIV_Q_THRESHOLD              44

#define ROOTREM_THRESHOLD                 6

#define MATRIX22_STRASSEN_THRESHOLD      21
#define HGCD_THRESHOLD                   75
#define HGCD_APPR_THRESHOLD              50
#define HGCD_REDUCE_THRESHOLD           772
#define GCD_DC_THRESHOLD                492
#define GCDEXT_DC_THRESHOLD             358
#define JACOBI_BASE_METHOD                2

#define GET_STR_DC_THRESHOLD             13
#define GET_STR_PRECOMPUTE_THRESHOLD     22
#define SET_STR_DC_THRESHOLD            890
#define SET_STR_PRECOMPUTE_THRESHOLD   2093

#define FAC_DSC_THRESHOLD               557
#define FAC_ODD_THRESHOLD                44

/* fft_tuning -- autogenerated by tune-fft */

#define FFT_TAB \
   { { 4, 3 }, { 3, 3 }, { 3, 2 }, { 2, 1 }, { 1, 0 } }

#define MULMOD_TAB \
   { 4, 3, 4, 4, 4, 3, 3, 3, 3, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1 }

#define FFT_N_NUM 19

#define FFT_MULMOD_2EXPP1_CUTOFF 128


/* Tuneup completed successfully, took 91 seconds */

