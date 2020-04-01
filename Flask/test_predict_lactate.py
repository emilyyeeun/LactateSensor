import requests

def run_test():
    print(requests.post(
        'http://0.0.0.0:9000/predict_lactate', 
        json={
            'age': 22,
            'gender': 'Female', 
            'height': 65,
            'glucose': 90,
            'weight': 123.5,
            'sp02': 97,
            'heart_rate': 80}).text)

if __name__ == '__main__':
    run_test()