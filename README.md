# Atbash Cipher App

This is the atbash cipher app that read content from *original_data.txt* file and encrypt them, After encryption it will save encrypted content into another txt *encrypt_data.txt* file.

Here we have some sample inputs.
1. Hello world!
2. Christmas is the 25th December

## Encrypt Hello world!
To encrypt **Hello world!** into atbash cipher, you have to wrtite **Hello world!** into *original_data.txt* file and then you have to open command line on current folder and execute following command to see the output.

```python 
python atbash_cipher.py
```
When you run above command, you will get an output **Svool dliow!**.

## Encrypt "Christmas is the 25th December"

To encrypt _Christmas is the 25th December_** into atbash cipher, you have to wrtite _Christmas is the 25th December_** into *original_data.txt* file and then you have to open command line on current folder and execute following command to see the output.

```python 
python atbash_cipher.py
```

When you run above command, you will get an output _Xsirhgnzh rh gsv 25gs Wvxvnyvi_**.

# Unittesting using PyTest.
Here we have a file *test_atbash.py* that is used to test the *atbash_cipher.py file*. *test_* prefix is mandatory which indicate the test file name where PyTest's functions or classes are written.

Make sure PyTest already installed in you system,If PyTest not installed execute below command.

```python
pip install pytest
```

## In case of *Svool dliow!* output:
Add following code inside *test_atbash.py* file.
```python 

import atbash_cipher
import pytest

#read test from original_data.txt file.
with open(f"original_data.txt", "r") as f:
	data = atbash_cipher.atbash(f.read()).lower()



#Unit testing using PyTest module
def test_abtash_cipher():
	assert ' '.join(atbash_cipher.encrypt_data) == 'Svool dliow'

```

After adding above code, execute below command.

```python
pytest test_atbash.py 
```


## In case of *Xsirhgnzh rh gsv 25gs Wvxvnyvi* output:

Add following code inside *test_atbash.py* file.

```python 

import atbash_cipher
import pytest

#read test from original_data.txt file.
with open(f"original_data.txt", "r") as f:
	data = atbash_cipher.atbash(f.read()).lower()



#Unit testing using PyTest module
def test_abtash_cipher():
	assert ' '.join(atbash_cipher.encrypt_data) == 'Xsirhgnzh rh gsv 25gs Wvxvnyvi'

```


After adding above code, execute below command.


```python
pytest test_atbash.py 
```






