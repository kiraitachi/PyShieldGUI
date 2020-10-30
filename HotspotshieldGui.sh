option=`kdialog --combobox "<h1>Welcome to KinuxShield</h1><h4>KinuxShield is an unofficial KDE GUI for Hotspotshield</h4><center><img src='KinuxShield.png'></center><p>Made by kiraitachi. For any issue: <br>https://github.com/kiraitachi/KinuxShield</p><p>Select an option</p>" "hotspotshield account status" "hotspotshield locations" "hotspotshield status" "hotspotshield disconnect" "curl ipinfo.io"`

kdialog --msgbox "`$option`"
