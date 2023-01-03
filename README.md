# studio_bundle - create standalone installer bundles for PhysiCell Studio

## MacOS

* We will use `py2app` to create the bundle (https://py2app.readthedocs.io/en/latest/)
* Warning: if you have previously attempted to use pyinstaller (on MacOS), you should uninstall it.

* Install Miniconda3: https://docs.conda.io/en/latest/miniconda.html 

```
- May need to manually have miniconda be preferred in your shell:
M1P~/git/studio_bundle$ sh /Users/heiland/opt/miniconda3/etc/profile.d/conda.sh
M1P~/git/studio_bundle$ export PATH="/Users/heiland/opt/miniconda3/bin:$PATH"

- Create and work from within a Python venv:
(base) M1P~$ conda activate myenv-conda

(myenv-conda) M1P~/git/studio_bundle/scripts$ which python
/Users/heiland/opt/miniconda3/envs/myenv-conda/bin/python

(myenv-conda) M1P~/git/studio_bundle/scripts$ which pip
/Users/heiland/opt/miniconda3/envs/myenv-conda/bin/pip

(myenv-conda) M1P~/git/studio_bundle/scripts$ which conda
/Users/heiland/opt/miniconda3/condabin/conda
  hmmm, not sure:
M1P~/git/studio_bundle$ which conda
/Users/heiland/opt/miniconda3/bin/conda
```

- Install py2app:
```
pip install -U py2app
```

* Install the necessary Python modules in this venv that will be needed for the Studio

```
(myenv-conda) M1P~$ pip install PyQt5
then:
pip install matplotlib
pip install pandas  # used by the pyMCDS*.py module
pip install scipy   # seemed to be problematic; use conda to install instead
pip uninstall scipy
conda install scipy
```

Then from this repo:
```
(myenv-conda) M1P~/git/studio_bundle/scripts$ rm -rf dist build   # if these dirs exist from previous attempts
(myenv-conda) M1P~/git/studio_bundle/scripts$ python setup.py py2app
... spews out lots...
Done!
```

Then before successfully running the app, apparently we need to manually copy libs:
```
* Apparently we need to manually copy over libs before trying to run the app:
(myenv-conda) M1P~/git/studio_bundle/scripts$  pushd dist/PhysiCell_Studio.app/Contents/Frameworks

-  then just copy/paste these "cp" commands, copying from wherever your miniconda libs are:
cp ~/opt/miniconda3/envs/myenv-conda/lib/libffi.7.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libiomp5.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libgfortran.5.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libquadmath.0.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libgcc_s.1.1.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libmkl_rt.1.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libmkl_core.1.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libmkl_intel_thread.1.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libmkl_intel_thread.1.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libmkl_intel_lp64.1.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libmkl_avx2.1.dylib .

- copy whatever executable model(s) we want to distribute
pushd ../Resources/
cp ~/git/studio_bundle/template-macos-intel template

- try running the Studio app [and an executable model]:
(myenv-conda) M1P~/git/studio_bundle/scripts$  dist/PhysiCell_Studio.app/Contents/MacOS/PhysiCell_Studio 
```

If successful, zip up the bundle for distribution:
```
(myenv-conda) M1P~/git/studio_bundle/scripts$ cd dist
(myenv-conda) M1P~/git/studio_bundle/scripts/dist$ zip -r PhysiCell_Studio.zip PhysiCell_Studio.app
```

---

## Windows