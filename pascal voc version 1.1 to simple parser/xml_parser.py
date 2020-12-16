# SWAMI KARUPPASWAMI THUNNAI

import os
import glob
from benedict import benedict as bdict


def parse_xml(xml_dir):
    xml_files = glob.glob(xml_dir+"*.xml")
    for i in xml_files:
        print(i)
        with open(i, "r") as xml_file:
            contents = xml_file.read()
            data = bdict.from_xml(contents)
            out_data = data["annotation.object"]
            result = []
            if type(out_data) != type(list()):
                out_data = out_data["bndbox"]
                result.append(out_data)
            else:
                for j in out_data:
                    result.append(j["bndbox"])
            for region in result:
                new_name = i[:-3] + "jpg"
                with open("out.txt", "a") as out:
                    xmin = int(float(region["xmin"]))
                    ymin = int(float(region["ymin"]))
                    xmax = int(float(region["xmax"]))
                    ymax = int(float(region["ymax"]))
                    out.write("{},{},{},{},{},sugarcane\n".format(new_name, xmin, ymin, xmax, ymax))



parse_xml("D:/sugarcane/tad_data/")
