

pip install -U py2app

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
cp ~/opt/miniconda3/envs/myenv-conda/lib/libmkl_core.1.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libmkl_intel_thread.1.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libmkl_intel_thread.1.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libmkl_intel_lp64.1.dylib .
cp ~/opt/miniconda3/envs/myenv-conda/lib/libmkl_avx2.1.dylib .
pushd

cd dist
zip -r PhysiCell_Studio.zip PhysiCell_Studio.app

(myenv-conda) M1P~/git/studio_bundle/scripts/dist$ ll *.zip
-rw-r--r--  1 heiland  staff  226147947 Jan  2 17:21 PhysiCell_Studio.zip

