
rm -rf dist build
python setup.py py2app

* Apparently we need to manually copy over libs before trying to run the app:
pushd dist/PhysiCell_Studio.app/Contents/Frameworks
cp ~/opt/miniconda3/envs/myenv-conda/lib/libffi.7.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libiomp5.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libgfortran.5.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libquadmath.0.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libgcc_s.1.1.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libmkl_rt.1.dylib .
pushd
