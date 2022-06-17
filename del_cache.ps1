#foldiers_for_delete
$cache_files = @(
"C:\Users\*\AppData\Local\Microsoft\Windows\INetCache",
"C:\Users\*\AppData\Local\Mozilla\Firefox\Profiles\*\cache2\entries",
"C:\Users\*\AppData\Local\Slimjet\User Data\Default\Cache",
"C:\Users\*\AppData\Local\Slimjet\User Data\Default\Media Cache",
"C:\users\*\AppData\local\slimjet\User Data\Default\Code Cache"
)

#print_files_for_delete
#foreach ($item in $cache_files){
#    gci -force $item -ErrorAction SilentlyContinue | ? { $_ -is [io.directoryinfo] } | % {
#    $len = 0
#    gci -recurse -force $_.fullname -ErrorAction SilentlyContinue | % { $len += $_.length }
#    $_.fullname, '{0:N2} GB' -f ($len / 1Gb)
#    }
#}

#delete_all_cache
foreach ($del in $cache_files){
    Remove-item $del
}
