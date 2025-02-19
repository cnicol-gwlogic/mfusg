from __future__ import print_function
import os
import shutil
import config

def test_teardown():

    if config.retain:
        return

    if os.path.isdir(config.dir_release):
        print('Removing folder ' + config.dir_release)
        shutil.rmtree(config.dir_release)

    if os.path.isfile(config.target):
        print('Removing ' + config.target)
        os.remove(config.target)

    if os.path.isfile(config.target_release):
        print('Removing ' + config.target_release)
        os.remove(config.target_release)

    if os.path.isfile(config.zbudusg_target):
        print('Removing ' + config.zbudusg_target)
        os.remove(config.zbudusg_target)

    return

if __name__ == '__main__':
    test_teardown()
