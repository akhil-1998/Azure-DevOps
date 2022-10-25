FROM mcr.microsoft.com/windows/servercore:ltsc2019

WORKDIR /azp

COPY azure-cli-2.41.0.msi .
RUN powershell -c Start-Process -Wait -FilePath '.\azure-cli-2.41.0.msi' -ArgumentList "/quiet"

COPY dotnet-sdk-6.0.402-win-x64.exe .
RUN powershell -c Start-Process -Wait -FilePath '.\dotnet-sdk-6.0.402-win-x64.exe' -ArgumentList "/quiet"

COPY start.ps1 .

CMD powershell .\start.ps1