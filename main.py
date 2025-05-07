import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO



# The URL for the ballot page
url = 'https://apps.chu.cam.ac.uk/internal/roomsballot/popularity.php'

# Replace with the cookie name and value you found in Safari
cookies = {
    'cookie_name': 'cookie_value',
    '_ga': 'GA1.1.1608816565.1745508459',
    '_ga_46G99DQTK9': 'GS2.1.s1746621853$o13$g0$t1746621853$j0$l0$h0',
    '_ga_F78J36YEFH': 'GS1.1.1745606663.1.1.1745606679.0.0.0',
    '_ga_G092NPEZFS': 'GS1.1.1745580291.1.0.1745580298.0.0.0',
    '_ga_JQWB2RPL5M': 'GS1.1.1745943898.1.0.1745943902.0.0.0',
    '_ga_LHPMVBPN4R': 'GS2.1.s1746554749$o14$g0$t1746554749$j0$l0$h0',
    '_ga_P8Q1QT5W4K': 'GS1.1.1745943898.2.1.1745944002.0.0.0',
    '_ga_QHQ86LCL1W': 'GS1.1.1745580291.1.0.1745580298.0.0.0',
    '_ga_T36YS7H4YC': 'GS1.1.1745944001.1.0.1745944002.0.0.0',
    '_ga_XM5ZBR66W0': 'GS1.1.1745606634.1.1.1745606663.0.0.0',
    '_gid': 'GA1.3.1059963680.1746526096',
    'csprod-PORTAL-PSJSESSIONID': 'pq1Z70sbj0aOW3Bxgej_o3yZWWBvYtUd!-420345374',
    'ExpirePage': 'https://camsis.cam.ac.uk/psc/ravenprod/',
    'mod_auth_openidc_session': '418fae92-b5b2-4e8d-bf20-77fa0cff3946',
    'PHPSESSID': 'o7rv1dqhf5a5ci1tuo60vi66s1',
    'PS_LASTSITE': 'https://camsis.cam.ac.uk/psc/ravenprod/',
    'PS_LOGINLIST': 'https://camsis.cam.ac.uk/ravenprod',
    'ps_theme': 'node:SA portal:EMPLOYEE theme_id:UC_860_FLUID_THEME_STUDENT css:PT_BRAND_CLASSIC_TEMPLATE_860 css_f:UC_PT_BRAND_FLUID_TEMPLATE_860 accessibility:N macroset:UC_MACROSET_860 formfactor:3 piamode:2',
    'PS_TOKEN': 'pQAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4Aawg4AC4AMQAwABQgkYn2Uj/NaS8+FtHNW6GaO14CBGUAAAAFAFNkYXRhWXicLYxLDkBAFATLJxYWbmLCGL8D+KxEsJdYCVd0OB3xkq5K9+LdQBj4nic/Pt/FFwcnjoaoY2IgmVnp2dgZWXCWDEtJKjvRkv80WluxkI0e1F8qdV5mjgtY',
    'PS_TOKENEXPIRE': '21_Apr_2025_19',
    'PS_TokenSite': 'https://camsis.cam.ac.uk/psc/ravenprod/?csprod-PORTAL-PSJSESSIONID'
}

# Start a session to maintain the logged-in state
session = requests.Session()

# Set the cookies for the session
session.cookies.update(cookies)

# Fetch the page containing the ballot table
response = session.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Page fetched successfully.")
    
    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the outer table
    outer_table = soup.find('table')  # This will find the first table on the page (outer table)

    # Find the inner table inside the outer table (you can adjust based on structure)
    inner_table = outer_table.find_all('table')[0]  # The inner table is the second table in this case

    # Convert the inner table to a DataFrame
    df = pd.read_html(str(inner_table))[0]

    print(df.head())  # Print the first few rows of the inner table to check
    df.to_csv('ballot_data.csv', index=False)  # Export to CSV


else:
    print(f"Failed to fetch the page, status code: {response.status_code}")
