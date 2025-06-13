from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def run_tests():
    # test_get_files_info()
    test_get_file_content()

def test_get_file_content():
    print("Test 1: get_file_content('calculator', 'lorem.txt')")
    print(get_file_content("calculator", "lorem.txt"))
    print("\n" + "="*60 + "\n")

    print("Test 2: get_file_content('calculator', 'main.py')")
    print(get_file_content("calculator", "main.py"))
    print("\n" + "="*60 + "\n")

    print("Test 3: get_file_content('calculator', 'pkg/calculator.py')")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("\n" + "="*60 + "\n")

    print("Test 4: get_file_content('calculator', '/bin/cat')")
    print(get_file_content("calculator", "/bin/cat"))
    print("\n" + "="*60 + "\n")

def test_get_files_info():
    print("Test 1: get_files_info('calculator', '.')")
    print(get_files_info("calculator", "."))
    print("\n" + "="*60 + "\n")

    print("Test 2: get_files_info('calculator', 'pkg')")
    print(get_files_info("calculator", "pkg"))
    print("\n" + "="*60 + "\n")

    print("Test 3: get_files_info('calculator', '/bin')  # should return error")
    print(get_files_info("calculator", "/bin"))
    print("\n" + "="*60 + "\n")

    print("Test 4: get_files_info('calculator', '../')  # should return error")
    print(get_files_info("calculator", "../"))
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    run_tests()
