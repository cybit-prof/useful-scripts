<#Basic PowerShell port scan script to scan URL or IP address using one port or a range of port numbers
#>
Write-Host "Today's date is $(Get-Date)"
$target = Read-Host -Prompt "Enter the URL or IP address"
$portsInput = Read-Host -Prompt "Enter the ports to scan (comma-separated, e.g. 21,23,25,80,443)"
$ports = $portsInput -split "," | ForEach-Object { $_.Trim() }

foreach ($port in $ports) {
    $check=Test-NetConnection $target -Port $port -WarningAction SilentlyContinue
	If ($check.tcpTestSucceeded -eq $true)
		{Write-Host "$target TCP port $port is open" -ForegroundColor Green}
	Else
		{Write-Host "$target TCP port $port is closed" -ForegroundColor Red}
}
