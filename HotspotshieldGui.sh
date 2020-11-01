option=`kdialog --combobox "<h1>Welcome to KinuxShield</h1><h4>KinuxShield is an unofficial KDE GUI for Hotspotshield</h4><center><img src='KinuxShield.png'></center><p>Made by kiraitachi. For any issue: <br>https://github.com/kiraitachi/KinuxShield</p><p>Select an option:</p>" "hotspotshield account signin" "hotspotshield account signout" "hotspotshield start" "hotspotshield stop" "hotspotshield connect" "hotspotshield account status" "VPN Locations" "VPN Client Status" "Disconnect VPN" "What's my public IP?"`

answer="$?"
if [ "$answer" = 0 ] && [ "$option" = "hotspotshield account signin" ]; then
	kdialog --msgbox "`$option`"

elif [ "$answer" = 0 ] && [ "$option" = "hotspotshield account signout" ]; then
    kdialog --msgbox "`$option`"

elif [ "$answer" = 0 ] && [ "$option" = "hotspotshield start" ]; then
    kdialog --msgbox "`$option`"

elif [ "$answer" = 0 ] && [ "$option" = "hotspotshield stop" ]; then
    kdialog --msgbox "`$option`"

elif [ "$answer" = 0 ] && [ "$option" = "hotspotshield connect" ]; then
    kdialog --msgbox "`$option`"

elif [ "$answer" = 0 ] && [ "$option" = "hotspotshield account status" ]; then
    kdialog --msgbox "`$option`"

elif [ "$answer" = 0 ] && [ "$option" = "VPN Locations" ]; then
    kdialog --combobox "Select the Location to connect:" "`hotspotshield locations`"

elif [ "$answer" = 0 ] && [ "$option" = "VPN Client Status" ]; then
    kdialog --msgbox "`hotspotshield status`"

elif [ "$answer" = 0 ] && [ "$option" = "Disconnect VPN" ]; then
    kdialog --title "KinuxShield `hotspotshield disconnect`" --passivepopup \ "VPN Disconnected" 10

elif [ "$answer" = 0 ] && [ "$option" = "What's my public IP?" ]; then
    kdialog --msgbox "`curl ipinfo.io`"

else
	kdialog --error "Thanks for using KinuxShield by kiraitachi"
fi;
