import pandas as pd
import h5py
import numpy as np

csv_file = 'data.csv'
hdf_file = 'output.hdf5'

# CSV 파일 읽기
df = pd.read_csv(csv_file, delimiter=',')

# HDF5 파일 생성 및 데이터 저장
with h5py.File(hdf_file, 'w') as hdf:
    for i, col in enumerate(df.columns):
        key = ''
        if i == 0:
            key = 'joint1'
        elif i == 1:
            key = 'joint2'
        elif i == 2:
            key = 'joint3'
        elif i == 3:
            key = 'joint4'
        elif i == 4:
            key = 'joint5'
        elif i == 5:
            key = 'joint6'
        elif i == 6:
            key = 'velocity1'
        elif i == 7:
            key = 'velocity2'
        elif i == 8:
            key = 'velocity3'
        elif i == 9:
            key = 'velocity4'
        elif i == 10:
            key = 'velocity5'
        elif i == 11:
            key = 'velocity6'

        data = df[col].values.astype(np.float32)
        hdf.create_dataset(key, data=data, dtype='f')

print(f'CSV 파일이 HDF5 파일 {hdf_file}로 성공적으로 변환되었습니다.')
