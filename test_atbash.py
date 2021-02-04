import atbash_cipher
import pytest

#read test from original_data.txt file.
with open(f"original_data.txt", "r") as f:
	data = atbash_cipher.atbash(f.read()).lower()



#Unit testing using PyTest module
def test_abtash_cipher():
	assert ' '.join(atbash_cipher.encrypt_data) == 'Xsirhgnzh rh gsv 25gs Wvxvnyvi'