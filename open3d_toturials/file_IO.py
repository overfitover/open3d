from open3d import *
import open3d


if __name__ == '__main__':

    print("Testing IO for point cloud ...")
    pcd = open3d.read_point_cloud("./open3d_toturials/TestData/tt.pcd")
    print(pcd)
    write_point_cloud("copy_of_fragment.pcd", pcd)

    # print("Testing IO for meshs ...")
    # mesh = read_triangle_mesh("TestData/knot.ply")
    # print(mesh)
    # write_triangle_mesh("copy_of_knot.ply", mesh)

    print("Testing IO for images ...")
    img = read_image("/home/ovo/project/ovo_project/object_detection/hiddenLayer/open3d_toturials/TestData/timg.jpg")
    print(img)
    write_image("copy_of_lena_color.jpg", img)
























