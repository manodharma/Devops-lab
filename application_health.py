import requests

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Application is UP")
        else:
            print(f"Application is DOWN, status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Application is DOWN, error: {e}")

# The application is tested locally using Kind (Kubernetes IN Docker) and Ingress.
check_application_status("https://wisecow.local")
