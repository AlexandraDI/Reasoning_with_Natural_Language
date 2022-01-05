call npm run build
rmdir /s /q ..\code\src\web\dist
xcopy /E /I dist ..\code\src\web\dist