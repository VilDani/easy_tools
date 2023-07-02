import os
import sys
from pathlib import Path
import pandas as pd

folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(folder)

from data_access import universal_access


def test_local_access_link_txt_file():
    work_dir = Path(os.path.abspath(os.path.dirname(__file__))) / 'work_dir'
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)
    assert os.path.exists(work_dir)

    # Check with workable link
    correct_file_name = 'aaaBBB.txt'
    full_link = work_dir / correct_file_name
    data_to_file = 'data to file'
    # Delete file
    if full_link.is_file():
        full_link.unlink()
    assert not os.path.exists(full_link)

    error, data = universal_access.put_data(full_link, data_to_file, work_dir=work_dir)
    assert error is None
    assert data_to_file

    error, data_from_file = universal_access.read_data(full_link, work_dir=work_dir)
    assert error is None
    assert data_to_file == data_from_file

    # Delete file
    full_link.unlink()
    assert not os.path.exists(full_link)


def test_local_access_link_feather_file():
    work_dir = Path(os.path.abspath(os.path.dirname(__file__))) / 'work_dir'
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)
    assert os.path.exists(work_dir)

    # Check with workable link
    correct_file_name = 'aaaBBB.feather'
    full_link = work_dir / correct_file_name
    # Delete file
    if full_link.is_file():
        full_link.unlink()
    assert not os.path.exists(full_link)
    data_to_file = pd.DataFrame({
        'first_column': [1, 2],
        'second_column': [3, 4]
    })

    error, data = universal_access.put_data(full_link, data_to_file, work_dir=work_dir)
    assert error is None
    assert not data_to_file.empty

    error, data_from_file = universal_access.read_data(full_link, work_dir=work_dir)
    assert error is None
    assert data_to_file.__class__ == data_from_file.__class__
    del data_from_file['index']     # removing column 'index'
    assert data_to_file.to_dict() == data_to_file.to_dict()

    # Delete file
    full_link.unlink()
    assert not os.path.exists(full_link)


def test_read_non_existing_file():
    work_dir = Path(os.path.abspath(os.path.dirname(__file__))) / 'work//dir'   # wrong link
    assert not os.path.exists(work_dir)

    # Check with not workable link
    correct_file_name = 'aaaBBB.feather'
    full_link = work_dir / correct_file_name
    # Delete file
    if full_link.is_file():
        full_link.unlink()
    assert not os.path.exists(full_link)
    data_to_file = pd.DataFrame({
        'first_column': [1, 2],
        'second_column': [3, 4]
    })

    error, data_from_file = universal_access.read_data(full_link, work_dir=work_dir)
    assert error is not None

    assert not os.path.exists(full_link)







