SET NAME=BrightnessControl-v.2.0
SET ROOT=C:\Projects\Python\BrightnessControl-Desktop-
SET RELEASES=%ROOT%\Releases
SET RELEASE=%RELEASES%\%NAME%

mkdir %RELEASE%
copy %ROOT%\build\BrightnessControl.exe %RELEASE%\BrightnessControl.exe
Xcopy %ROOT%\assets %RELEASE%\assets /E /H /C /I
#7z a -tzip %NAME%.zip C:\Projects\Python\BrightnessControl-Desktop-\Releases\%NAME%
rmdir /s /q %RELEASE%