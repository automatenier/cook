$r = [System.Net.HttpWebRequest]::Create('http://localhost:3456/api/crm')
$r.Timeout = 5000
try {
    $resp = $r.GetResponse()
    $stream = $resp.GetResponseStream()
    $sr = New-Object System.IO.StreamReader($stream)
    $content = $sr.ReadToEnd()
    $sr.Close()
    $j = $content | ConvertFrom-Json
    Write-Host "Total records returned:" $j.Count
    Write-Host "First record name:" $j[0].name
    Write-Host "First record channel:" $j[0].channel
} catch {
    Write-Host "Error:" $_.Exception.Message
}
