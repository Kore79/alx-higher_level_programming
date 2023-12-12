#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def searchReplace_2(elem):
        return (elem if elem != search else replace)
    return list(map(searchReplace_2, my_list))
