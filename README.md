# py

The export_insights.py require python 3.x and requests, re (regular expression), 
exceptions, prettytable installed.

pip install requests re exceptions prettytable

Once packages are installed run script export_insights.py

The script will prompt for your host name in the appomni tenant url.  
Next it will prompt for the appomni tenant API key.

The script will pull all insights and look up any potential risks for each insight,
and output the information to the console and write it to a file named 
yourhostname_InsightsExport.txt file in the directory where the script was executed.
