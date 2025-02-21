@echo off
setlocal

for %%F in (*.swf) do (
  set "filename=%%~nF"
  if not exist "%%~nF" (
    mkdir "%%~nF"
  )
  move "%%F" "%%~nF\game.swf"
  echo Moved %%F to %%~nF\game.swf
)

endlocal