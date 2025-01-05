import subprocess

# Boilerplate function - include this in every test below!
def prepare_and_assert(input_array, output_array):
    # Prepare Variables
    expected_output = '\n'.join(output_array)

    # Get Actual Output 
    output_data = subprocess.run(['node', 'index.js'] + input_array, stdout=subprocess.PIPE)
    output_bytes = output_data.stdout.strip()
    output_string = output_bytes.decode("utf-8")

    # Test if Expected Output is found in Actual Output
    assert expected_output in output_string

# Test 1
def test_task_one():
    # Inputs
    input_array = [
        '1'
    ]

    # Outputs
    output_array = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12',
        '13',
        '14',
        '15',
        '16',
        '17',
        '18',
        '19',
        '20',
        '21',
        '22',
        '23',
        '24',
        '25',
        '26',
        '27',
        '28',
        '29',
        '30',
        '31',
        '32',
        '33',
        '34',
        '35',
        '36',
        '37',
        '38',
        '39',
        '40',
        '41',
        '42',
        '43',
        '44',
        '45',
        '46',
        '47',
        '48',
        '49',
        '50',
        '51',
        '52',
        '53',
        '54',
        '55',
        '56',
        '57',
        '58',
        '59',
        '60',
        '61',
        '62',
        '63',
        '64',
        '65',
        '66',
        '67',
        '68',
        '69',
        '70',
        '71',
        '72',
        '73',
        '74',
        '75',
        '76',
        '77',
        '78',
        '79',
        '80',
        '81',
        '82',
        '83',
        '84',
        '85',
        '86',
        '87',
        '88',
        '89',
        '90',
        '91',
        '92',
        '93',
        '94',
        '95',
        '96',
        '97',
        '98',
        '99',
        '100',
        '101',
        '102',
        '103',
        '104',
        '105'
    ]

    prepare_and_assert(input_array, output_array)

# Test 2
def test_task_two():
    # Inputs
    input_array = [
        '2'
    ]

    # Outputs
    output_array = [
        '1',
        '2',
        'Fizz',
        '4',
        '5',
        'Fizz',
        '7',
        '8',
        'Fizz',
        '10',
        '11',
        'Fizz',
        '13',
        '14',
        'Fizz',
        '16',
        '17',
        'Fizz',
        '19',
        '20',
        'Fizz',
        '22',
        '23',
        'Fizz',
        '25',
        '26',
        'Fizz',
        '28',
        '29',
        'Fizz',
        '31',
        '32',
        'Fizz',
        '34',
        '35',
        'Fizz',
        '37',
        '38',
        'Fizz',
        '40',
        '41',
        'Fizz',
        '43',
        '44',
        'Fizz',
        '46',
        '47',
        'Fizz',
        '49',
        '50',
        'Fizz',
        '52',
        '53',
        'Fizz',
        '55',
        '56',
        'Fizz',
        '58',
        '59',
        'Fizz',
        '61',
        '62',
        'Fizz',
        '64',
        '65',
        'Fizz',
        '67',
        '68',
        'Fizz',
        '70',
        '71',
        'Fizz',
        '73',
        '74',
        'Fizz',
        '76',
        '77',
        'Fizz',
        '79',
        '80',
        'Fizz',
        '82',
        '83',
        'Fizz',
        '85',
        '86',
        'Fizz',
        '88',
        '89',
        'Fizz',
        '91',
        '92',
        'Fizz',
        '94',
        '95',
        'Fizz',
        '97',
        '98',
        'Fizz',
        '100',
        '101',
        'Fizz',
        '103',
        '104',
        'Fizz'
    ]

    prepare_and_assert(input_array, output_array)

# Test 3
def test_task_three():
    # Inputs
    input_array = [
        '3'
    ]

    # Outputs
    output_array = [
        '1',
        '2',
        'Fizz',
        '4',
        'Buzz',
        'Fizz',
        '7',
        '8',
        'Fizz',
        'Buzz',
        '11',
        'Fizz',
        '13',
        '14',
        'FizzBuzz',
        '16',
        '17',
        'Fizz',
        '19',
        'Buzz',
        'Fizz',
        '22',
        '23',
        'Fizz',
        'Buzz',
        '26',
        'Fizz',
        '28',
        '29',
        'FizzBuzz',
        '31',
        '32',
        'Fizz',
        '34',
        'Buzz',
        'Fizz',
        '37',
        '38',
        'Fizz',
        'Buzz',
        '41',
        'Fizz',
        '43',
        '44',
        'FizzBuzz',
        '46',
        '47',
        'Fizz',
        '49',
        'Buzz',
        'Fizz',
        '52',
        '53',
        'Fizz',
        'Buzz',
        '56',
        'Fizz',
        '58',
        '59',
        'FizzBuzz',
        '61',
        '62',
        'Fizz',
        '64',
        'Buzz',
        'Fizz',
        '67',
        '68',
        'Fizz',
        'Buzz',
        '71',
        'Fizz',
        '73',
        '74',
        'FizzBuzz',
        '76',
        '77',
        'Fizz',
        '79',
        'Buzz',
        'Fizz',
        '82',
        '83',
        'Fizz',
        'Buzz',
        '86',
        'Fizz',
        '88',
        '89',
        'FizzBuzz',
        '91',
        '92',
        'Fizz',
        '94',
        'Buzz',
        'Fizz',
        '97',
        '98',
        'Fizz',
        'Buzz',
        '101',
        'Fizz',
        '103',
        '104',
        'FizzBuzz'
    ]

    prepare_and_assert(input_array, output_array)

# Test 4
def test_task_four():
    # Inputs
    input_array = [
        '4'
    ]

    # Outputs
    output_array = [
        '1',
        '2',
        'Fizz',
        '4',
        'Buzz',
        'Fizz',
        'Woof',
        '8',
        'Fizz',
        'Buzz',
        '11',
        'Fizz',
        '13',
        'Woof',
        'FizzBuzz',
        '16',
        '17',
        'Fizz',
        '19',
        'Buzz',
        'FizzWoof',
        '22',
        '23',
        'Fizz',
        'Buzz',
        '26',
        'Fizz',
        'Woof',
        '29',
        'FizzBuzz',
        '31',
        '32',
        'Fizz',
        '34',
        'BuzzWoof',
        'Fizz',
        '37',
        '38',
        'Fizz',
        'Buzz',
        '41',
        'FizzWoof',
        '43',
        '44',
        'FizzBuzz',
        '46',
        '47',
        'Fizz',
        'Woof',
        'Buzz',
        'Fizz',
        '52',
        '53',
        'Fizz',
        'Buzz',
        'Woof',
        'Fizz',
        '58',
        '59',
        'FizzBuzz',
        '61',
        '62',
        'FizzWoof',
        '64',
        'Buzz',
        'Fizz',
        '67',
        '68',
        'Fizz',
        'BuzzWoof',
        '71',
        'Fizz',
        '73',
        '74',
        'FizzBuzz',
        '76',
        'Woof',
        'Fizz',
        '79',
        'Buzz',
        'Fizz',
        '82',
        '83',
        'FizzWoof',
        'Buzz',
        '86',
        'Fizz',
        '88',
        '89',
        'FizzBuzz',
        'Woof',
        '92',
        'Fizz',
        '94',
        'Buzz',
        'Fizz',
        '97',
        'Woof',
        'Fizz',
        'Buzz',
        '101',
        'Fizz',
        '103',
        '104',
        'FizzBuzzWoof'
    ]

    prepare_and_assert(input_array, output_array)