# UnZip Password Protected File(s)
Unzip password protected files that use fixed password with the last 4 characters from file name as the full password.


For example, if you have a zipped file name "12345678.zip" is passowrd protected with "infected5678", you can use this script to unzip the file without manually supplying password. This script will be able to automatically use the last 4 characters plus a fixed password "infected", combined as the full password "infected5678" and use that to extract the file.


Usage: 
<pre><code>python unzip.py <zip file>
</code></pre>

Example: 
<pre><code>$bash> python unzip.py *.zip
[+] Extracting malware sample
[+] Malware sample c8ff0d60cf15eb398b9cff7433b12365 extracted, moving on to next one...

[+] Extracting malware sample
[+] Malware sample ec421a271b5dc4a4d68762d4d402d549 extracted, moving on to next one...

[+] All files extracted, good bye!
$bash>
</code></pre>
