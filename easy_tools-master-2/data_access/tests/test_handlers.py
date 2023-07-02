import os
import sys
from pathlib import Path
import pandas as pd

folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(folder)

from data_access._class_universal_handler import UniversalHandler


def test_local_access_link_recognition():
    work_dir = Path(os.path.abspath(os.path.dirname(__file__))) / 'work_dir'
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)
    assert os.path.exists(work_dir)

    # Check with workable link
    correct_file_name = 'aaaBBB.txt'
    full_link = work_dir / correct_file_name
    # Create the file
    with open(full_link, 'w') as file:
        file.write('it is a file for testing')
    handler = UniversalHandler(full_link, work_dir)

    # Check with not workable link
    not_correct_file_name = ''
    full_link = work_dir / not_correct_file_name
    handler = UniversalHandler(full_link, work_dir)


def test_local_feather_handler():
    work_dir = Path(os.path.abspath(os.path.dirname(__file__))) / 'work_dir'
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)
    assert os.path.exists(work_dir)

    file_name = 'empty_data_frame.feather'
    full_link = work_dir / file_name
    data_frame_to_file = pd.DataFrame()

    local_handler = UniversalHandler(full_link)
    local_handler.write_data(data_frame_to_file)
    assert os.path.isfile(full_link)

    del local_handler

    local_handler = UniversalHandler(full_link)
    data_frame_from_file = local_handler.read_data()

    assert data_frame_from_file.to_dict() == {'index': {}}

    os. remove(full_link)
    assert not os.path.isfile(full_link)


def test_local_json_handler():
    work_dir = Path(os.path.abspath(os.path.dirname(__file__))) / 'work_dir'
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)
    assert os.path.exists(work_dir)

    file_name = 'data.json'
    full_link = work_dir / file_name
    data_to_put_to_file = {
        'key_1': 'value_1',
        'key_2': 'value_2',
        'key_3': 'value_3',
        'key_4': ['value_1', 'value_2']
    }
    local_handler = UniversalHandler(full_link)
    local_handler.write_data(data_to_put_to_file)
    assert os.path.isfile(full_link)
    del local_handler

    local_handler = UniversalHandler(full_link)
    data_got_from_file = local_handler.read_data()
    assert data_to_put_to_file == data_got_from_file
    os.remove(full_link)
    assert not os.path.isfile(full_link)


def test_local_toml_handler():
    work_dir = Path(os.path.abspath(os.path.dirname(__file__))) / 'work_dir'
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)
    assert os.path.exists(work_dir)

    file_name = 'data.toml'
    full_link = work_dir / file_name
    data_to_put_to_file = {
        'key_1': ['value_1', 'value_2'],
        'key_2': 'value_2',
        'key_3': 'value_3',
    }
    local_handler = UniversalHandler(full_link)
    local_handler.write_data(data_to_put_to_file)
    assert os.path.isfile(full_link)
    del local_handler

    local_handler = UniversalHandler(full_link)
    data_got_from_file = local_handler.read_data()
    assert data_to_put_to_file == data_got_from_file
    os.remove(full_link)
    assert not os.path.isfile(full_link)


def test_local_unknown_file_extension():
    work_dir = Path(os.path.abspath(os.path.dirname(__file__))) / 'work_dir'
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)
    assert os.path.exists(work_dir)

    file_name = 'data.ext'
    full_link = work_dir / file_name
    data_to_put_to_file = 'Data'
    local_handler = UniversalHandler(full_link)
    local_handler.write_data(data_to_put_to_file)
    assert os.path.isfile(full_link)
    del local_handler

    local_handler = UniversalHandler(full_link)
    assert local_handler.handler_class.__name__ == 'Txt'
    data_got_from_file = local_handler.read_data()
    assert data_to_put_to_file == data_got_from_file
    os.remove(full_link)
    assert not os.path.isfile(full_link)










