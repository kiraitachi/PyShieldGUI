option=`kdialog --combobox "Select an option for Hotspotshield:" "hotspotshield account status" "hotspotshield locations" "hotspotshield status" "hotspotshield disconnect" "curl ipinfo.io"`
kdialog --msgbox "`$option`"
