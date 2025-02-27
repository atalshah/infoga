import phonenumbers
import requests
import json
from phonenumbers import carrier, geocoder

def get_number_info(phone_number):
    """ فون نمبر سے ملک اور سروس پرووائیڈر نکالنے کا فنکشن """
    try:
        number = phonenumbers.parse(phone_number)
        country = geocoder.description_for_number(number, "en")
        service_provider = carrier.name_for_number(number, "en")
        return country, service_provider
    except:
        return "Invalid Number!", "Unknown"

def numverify_api(phone_number):
    """ NumVerify API سے نمبر کی معلومات حاصل کرنے کا فنکشن """
    api_key = "d9a49e6e89fe528912ace91ec66e625b"  # اپنی API Key یہاں ڈالیں
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("valid"):
            return data
        else:
            return {"error": "Invalid number or API limit reached!"}
    except:
        return {"error": "Failed to connect to API!"}

if __name__ == "__main__":
    phone = input("📲 Enter phone number with country code (+923001234567): ")
    
    # فون نمبر کی بنیادی معلومات حاصل کریں
    country, service = get_number_info(phone)
    
    print("\n📌 Basic Info:")
    print(f"📍 Country: {country}")
    print(f"📡 Service Provider: {service}")
    
    # API سے مزید تفصیلات حاصل کریں
    api_data = numverify_api(phone)
    
    print("\n🔍 API Data:")
    print(json.dumps(api_data, indent=4))  # JSON کو خوبصورت فارمیٹ میں دکھانے کے لیے