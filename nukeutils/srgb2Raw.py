import os
import nuke

def convert2Raw(directory: str, color_space: str = 'sRGBlinear'):
    files = os.listdir(directory)
    read_node = nuke.createNode('Read')
    write_node = nuke.createNode('Write')
    write_node['file_type'].setValue('exr')
    write_node['datatype'].setValue('32 bit float')
    write_node['colorspace'].setValue('data')

    for file in files:
        if file.endswith('.exr') and color_space in file:
            read_node['file'].setValue(os.path.join(directory, file))
            read_node['colorspace'].setValue('Linear Rec.709 (sRGB)')
            output_file = file.replace('sRGBlinear', 'Raw')
            output_path = os.path.join(directory, output_file)
            write_node['file'].setValue(output_path)
            nuke.execute(write_node, 1, 1)

    nuke.delete(write_node)
    nuke.delete(read_node)

input_dir = '/Users/suhail/Library/CloudStorage/Dropbox/threeD/lib/hdri'
convert2Raw(input_dir)
