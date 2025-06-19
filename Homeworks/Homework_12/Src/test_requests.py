import requests

BASE_URL = 'http://127.0.0.1:5000'
RESULTS_FILE = 'results.txt'

def log_result(action, response):
    try:
        data = response.json()
    except ValueError:
        data = "<no content>"
    output = f'{action}: {response.status_code} {data}\n'
    print(output)
    with open('results.txt', 'a') as f:
        f.write(output)

def clear_results_file():
    with open(RESULTS_FILE, 'w') as f:
        f.write("Student API Test Results\n\n")


def test_get_all_students():
    response = requests.get(f'{BASE_URL}/students')
    log_result('GET /students', response)


def test_post_student(first_name, last_name, age):
    student = {'first_name': first_name, 'last_name': last_name, 'age': age}
    response = requests.post(f'{BASE_URL}/students', json=student)
    log_result('POST /students', response)
    return response.json().get('id')


def test_get_student(student_id):
    response = requests.get(f'{BASE_URL}/students/{student_id}')
    log_result(f'GET /students/{student_id}', response)


def test_patch_student_age(student_id, new_age):
    patch_data = {'age': new_age}
    response = requests.patch(f'{BASE_URL}/students/{student_id}', json=patch_data)
    log_result(f'PATCH /students/{student_id}', response)


def test_put_student(student_id, first_name, last_name, age):
    update_data = {'first_name': first_name, 'last_name': last_name, 'age': age}
    response = requests.put(f'{BASE_URL}/students/{student_id}', json=update_data)
    log_result(f'PUT /students/{student_id}', response)


def test_delete_student(student_id):
    response = requests.delete(f'{BASE_URL}/students/{student_id}')
    log_result(f'DELETE /students/{student_id}', response)


if __name__ == '__main__':
    clear_results_file()

    test_get_all_students()

    id1 = test_post_student('Monica', 'Smith', 21)
    id2 = test_post_student('Bob', 'Teddy', 22)
    id3 = test_post_student('Johan', 'Brown', 23)

    test_get_all_students()

    test_patch_student_age(id2, 25)

    test_get_student(id2)

    test_put_student(id3, 'Charles', 'Green', 26)

    test_get_student(id3)

    test_get_all_students()

    test_delete_student(id1)

    test_get_all_students()
