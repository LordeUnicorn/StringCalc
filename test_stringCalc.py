from stringCalc import add_num
import pytest
def test_empty_string_returns_0():
	assert add_num("") == 0

def test_single_number_converts_to_number():
	assert add_num("1") == 1
	assert add_num("5") == 5

def test_two_numbers_get_added():
	assert add_num("1,2") == 3

#q2
def test_arbitrary_numbers_get_added():
	assert add_num("1,2,3") == 6

# q3
def test_newlines_also_separates_input():
	assert add_num("1\n2,3") == 6

# q4
def test_delimiter_prefix():
	assert add_num("//;\n1;2") == 3

# q5
def test_negative_number_throws():
	with pytest.raises(Exception) as ex:
		add_num("1,2,-5")

	assert '-5' in str(ex.value)

def test_negative_can_be_delimiter_without_exception():
	assert add_num("//-\n1-2") == 3

# q6
def test_numbers_above_1000_are_ignored():
	assert add_num("2,1001,1") == 3

# q7
def test_any_length_delimiter():
	assert add_num("//[***]\n1***2***3") == 6

# q8
def test_allow_multiple_delimiters():
	assert add_num("//[*][%]\n1*2%3") == 6