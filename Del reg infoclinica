::main_delete
reg delete HKCU\SOFTWARE\SDS /f
reg delete HKCU\SOFTWARE\MiCh /f
reg delete HKCU\SOFTWARE\SDS /f
reg delete HKCU\Infodent /f
reg delete HKCU\Infoclinica /f
reg delete HKCU\Software\Infodent2 /f
reg delete HKCU\Software\Infoclinica /f
reg delete HKCU\Software\software\mich /f

::hku_target_del
setlocal ENABLEDELAYEDEXPANSION
for /F %%r in ('reg query hku') do (
    set key=%%r
    if "!key:~11,8!"=="S-1-5-21" if NOT "!key:~-8!"=="_Classes" (
        reg delete "!key!\SOFTWARE\MiCh" /f
        reg delete "!key!\SOFTWARE\SDS" /f
        reg delete "!key!\SOFTWARE\Infodent2" /f
        reg delete "!key!\SOFTWARE\Infoclinica" /f
	reg delete "!key!\SOFTWARE\software\mich" /f
	reg delete "!key!\Infodent" /f
	reg delete "!key!\Infoclinica" /f
	reg delete "!key!\Software\Infoclinica\software\mich" /f
	reg delete "!key!\Infoclinica" /f
    )
)
endlocal
