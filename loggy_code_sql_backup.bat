@ECHO OFF

set TIMESTAMP=%DATE:~10,4%%DATE:~4,2%%DATE:~7,2%

REM Export all databases into file C:\path\backup\databases.[year][month][day].sql
"C:\wamp64\bin\mysql\mysql5.7.24\bin\mysqldump.exe" --all-databases --result-file="E:\IDS\Loggy\database_backups\databases.%TIMESTAMP%.sql" --user="root" --password="idsidsidsids"

REM Change working directory to the location of the DB dump file.
E:
CD \IDS\Loggy\database_backups\

REM Compress DB dump file into CAB file (use "EXPAND file.cab" to decompress).
MAKECAB "databases.%TIMESTAMP%.sql" "databases.%TIMESTAMP%.sql.cab"

REM Delete uncompressed DB dump file.
REM DEL /q /f "databases.%TIMESTAMP%.sql"