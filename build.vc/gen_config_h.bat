@echo off
rem %1 = directory holding config data (in cdata)

echo creating config.h from %1

if not exist cfg.h (call :seterr & echo   config.h couldn't be built because cfg.h is missing & exit /b %errorlevel%)

echo /* generated by gen_config_h.bat */ >tmp.h
for /f  %%a in (%1cfg.h) do (if "%%a" NEQ "" (echo #define HAVE_NATIVE_%%a 1 >>tmp.h))

type cfg.h >>tmp.h
call out_copy_rename tmp.h ..\ config.h
del tmp.h

exit /b 0

:seterr
exit /b 1