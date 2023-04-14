
echo "Killing web_ui"
taskkill /fi "WindowTitle eq web_ui"
start cmd "/c title web_ui && activate maskrcnn && title web_ui && web_ui_run.bat && title web_ui && deactivate"