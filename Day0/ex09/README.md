# My first package creation


### How to install ft_package ?

#### Install dependencies if you do not have it

```sh

pip install wheel
```

#### At first : Clean old builds

```sh
rm -rf build dist ft_package.egg-info
```

#### Then create package file

```sh
python setup.py sdist bdist_wheel
```

#### Finally, install it
##### using :
```sh
pip install ./dist/ft_package-0.0.1.tar.gz
```

##### or using :
```sh
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

>[!info] info 
You can use 
**pip uninstall -y ft_package** and **pip install .**
to install package if you want, but it doesn't create the packages files so our command using pip install ./dist will not work

#### To ensure installation is correct, you can run our tester
##### tester is at root in the repo
```sh
python tester.py
```