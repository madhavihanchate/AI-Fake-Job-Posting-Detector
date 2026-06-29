import requests


def verify_company(company):

    result = {
        "website": None,
        "website_status": False,
        "careers": False,
    }

    try:
        url = f"https://www.google.com/search?q={company}+official+website"

        response = requests.get(
            url,
            timeout=5,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        if response.status_code == 200:

            result["website_status"] = True
            result["website"] = url

            careers = requests.get(
                f"https://www.google.com/search?q={company}+careers",
                timeout=5,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )

            if careers.status_code == 200:
                result["careers"] = True

    except Exception:
        pass

    return result