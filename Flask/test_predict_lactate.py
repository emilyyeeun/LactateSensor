import requests

def run_test():
    print(requests.post(
        'http://0.0.0.0:9000/predict_lactate', 
        json={
            'age': 21,
            'gender': 'male', 
            'height': 1.5,
            'glucose': .1,
            'weight': 70,
            'sp02': .3,
            'heart_rate': 70}).text)

if __name__ == '__main__':
    run_test()