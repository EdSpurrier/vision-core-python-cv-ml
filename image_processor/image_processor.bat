
echo "Killing image_processor"
taskkill /fi "WindowTitle eq image_processor"
start cmd "/c title image_processor && activate maskrcnn && title image_processor && image_processor_run.bat && title image_processor && deactivate && exit"
exit