import os
import cv2
from lxml import etree
import xml.etree.cElementTree as ET

def write_xml(folder, img, objects, tl, br, savedir):
    if not os.path.isdir(savedir):
        os.mkdir(savedir)

    image = cv2.imread(img.path)
    height, width, depth = image.shape

    annotation = ET.Element('annotation')
    ET.SubElement(annotation, 'folder').text = folder
    ET.SubElement(annotation, 'filename').text = img.name
    ET.SubElement(annotation, 'segmented').text = '0'
    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = str(depth)
    for obj, topl, botr in zip(objects, tl, br):
        ob = ET.SubElement(annotation, 'object')
        ET.SubElement(ob, 'name').text = obj
        ET.SubElement(ob, 'pose').text = 'Unspecified'
        ET.SubElement(ob, 'truncated').text = '0'
        ET.SubElement(ob, 'difficult').text = '0'
        bbox = ET.SubElement(ob, 'bndbox')
        ET.SubElement(bbox, 'xmin').text = str(topl[0])
        ET.SubElement(bbox, 'ymin').text = str(topl[1])
        ET.SubElement(bbox, 'xmax').text = str(botr[0])
        ET.SubElement(bbox, 'ymax').text = str(botr[1])

    xml_str = ET.tostring(annotation)
    root = etree.fromstring(xml_str)
    xml_str = etree.tostring(root, pretty_print=True)
    save_path = os.path.join(savedir, img.name.replace('jpg', 'xml'))
    with open(save_path, 'wb') as temp_xml:
        temp_xml.write(xml_str)


if __name__ == '__main__':
    """
    for testing
    """
    """
    label_dict = {
    "bulk_carrier": 0, "container_vessel": 1, "fishing_vessel": 2, "military": 3, "small_boat": 4,
    "passenger_vessel": 5, "patrol_vessel": 6, "RORO": 7, "sailing_vessel": 8, "tanker": 9, "tug": 10, "tugboat": 11
}
    """

    folder = '../BBox-Label-Tool/images/11'
    label_folder = '../BBox-Label-Tool/Labels_true/11'
    object_name = 'tugboat'
    # img = [im for im in os.scandir(folder) if '102195' in im.name][0]

    # import json
    # name_array = []
    # with open('image_names.json', 'r') as readfile:
    #     name_array = json.load(readfile)
    #
    # name_array = eval(name_array)
    # print(name_array)
    # print(len(name_array))

    for im in os.scandir(folder):
        file_name_array = im.name.split('.')
        file_name = file_name_array[0]
        # print(file_name)
        # if file_name in name_array:
        #     print(file_name)
        #     new_file_name = file_name + '400000'
        #     new_file_name_image = new_file_name + '.jpg'
        #     new_file_name_label = new_file_name + '.txt'
        #     print(new_file_name_image)
        #     print(new_file_name_label)
        #     os.rename(os.path.join('../BBox-Label-Tool/images/11', (file_name + '.jpg')),
        #               os.path.join('../BBox-Label-Tool/images/11', new_file_name_image))
        #     os.rename(os.path.join('../BBox-Label-Tool/Labels_true/11', (file_name+'.txt')),
        #               os.path.join('../BBox-Label-Tool/Labels_true/11', new_file_name_label))
        #     file_name = new_file_name
        # name_array.append(file_name)
        img = [im][0]
        label_file_name = file_name + '.txt'
        label_file_path = os.path.join(label_folder, label_file_name)
        f = open(label_file_path, "r")
        fileContent = f.read()
        splitFileContent = fileContent.split("\n")
        numOfBox = splitFileContent[0]
        coordinate = splitFileContent[1].split(" ")
        objects = []
        tl = []
        br = []
        image = cv2.imread(img.path)
        height, width, depth = image.shape

        for i in range(int(numOfBox)):
            coordinate = splitFileContent[i+1].split(" ")
            if int(coordinate[0]) < 0:
                coordinate[0] = '0'
            if int(coordinate[1]) < 0:
                coordinate[1] = '0'
            if int(coordinate[2]) > width:
                coordinate[2] = str(width)
            if int(coordinate[3]) > height:
                coordinate[3] = str(height)
            tl_tuple = (int(coordinate[0]), int(coordinate[1]))
            br_tuple = (int(coordinate[2]), int(coordinate[3]))
            tl.append(tl_tuple)
            br.append(br_tuple)
            objects.append(object_name)

        savedir = 'annotations'
        write_xml(folder, img, objects, tl, br, savedir)
    # print(len(name_array))
    # # print(str(name_array))
    # with open('image_names.json', 'w') as outfile:
    #     json.dump(str(name_array), outfile)
    # tl = [(10, 10)]
    # br = [(100, 100)]

