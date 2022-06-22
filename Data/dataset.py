#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from Data.synset import Synset

from Method.outputs import outputList

class Dataset(object):
    def __init__(self, root_path=None):
        self.root_path = None

        self.synset_id_list = []
        self.synset_dict = {}

        if root_path is not None:
            self.loadRootPath(root_path)
        return

    def reset(self):
        self.root_path = None

        self.synset_id_list = []
        self.synset_dict = {}
        return True

    def loadSynsetIdList(self):
        self.synset_id_list = []
        root_folder_name_list = os.listdir(self.root_path)
        for root_folder_name in root_folder_name_list:
            if not os.path.isdir(self.root_path + root_folder_name):
                continue
            self.synset_id_list.append(root_folder_name)
        return True

    def loadSynsetDict(self):
        for synset_id in self.synset_id_list:
            synset_root_path = self.root_path + synset_id + "/"
            synset = Synset(synset_root_path)
            self.synset_dict[synset_id] = synset
        return True

    def loadRootPath(self, root_path):
        self.reset()

        if not os.path.exists(root_path):
            print("[ERROR][Dataset::loadRootPath]")
            print("\t root_path not exist!")
            return False

        self.root_path = root_path
        if self.root_path[-1] != "/":
            self.root_path += "/"

        if not self.loadSynsetIdList():
            print("[ERROR][Synset::loadRootPath]")
            print("\t loadSynsetIdList failed!")
            return False

        if not self.loadSynsetDict():
            print("[ERROR][Synset::loadRootPath]")
            print("\t loadSynsetDict failed!")
            return False
        return True

    def outputInfo(self, info_level=0, print_cols=10):
        line_start = "\t" * info_level
        print(line_start + "[Dataset]")
        print(line_start + "\t root_path =", self.root_path)
        print(line_start + "\t synset_id_list =")
        outputList(self.synset_id_list, info_level + 2, print_cols)
        print(line_start + "\t synset size =", len(self.synset_id_list))
        return True

