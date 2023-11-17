import requests
from bs4 import BeautifulSoup

def scrape_specific_division(url, class_name1, class_name2,  det, over1, over2):
    try:
        response = requests.get(url)


        if response.status_code ==200:

 
            soup = BeautifulSoup(response.text, 'html.parser')
        
            countries = soup.find_all(class_=class_name1)

            first_country = countries[0].text
            second_country = countries[1].text


            if first_country and second_country:
            
                matching = f'{first_country} VS {second_country}'
            else:
                matching = 'No matches at the moment'

            over_counttt = soup.find_all(class_=over1)


            over_count2 = over_counttt[0].text
            over_count1 = over_counttt[1].text

            if over_count1 :
                prog1 = f'{first_country} - {over_count1}'

            else :
                prog1 = ""


            if over_count2:
                prog2 = f'{second_country} - {over_count2}'

            else :
                prog2 = ""

 
            details = soup.find_all(class_ = det)

            detail = details[0].text

            if detail :
                ved = str(detail)

            else:
                print(' ')

        
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return "Failed to fetch data."

    except Exception as e:
        print(f"Error while scraping: {e}")
    
    
    
    return "\n".join([matching, prog1, prog2, ved])
    print(matching)
    print(prog1)
    print(prog2)
    print(ved)



