import numpy as np  
from open3d import *

if __name__ == "__main__":
    print("Load a ply point cloud, print it, and reader it")

    pcd = read_point_cloud("./open3d_toturials/TestData/tt.pcd")
    print(pcd)
    print(np.asarray(pcd.points))
    draw_geometries([pcd])

    print("Downsample the point cloud with a voxel of 0.05")
    downpcd = voxel_down_sample(pcd, voxel_size=0.05)
    draw_geometries([downpcd])











































