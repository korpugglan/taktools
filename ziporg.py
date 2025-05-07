
def unpack_zip_files_separately(start_dir):
    max_zip_file_name_len = 64
    del_char_list = ["~", ".", ",", "!", "@", "#", "$"]

    zip_file_list = [file for file in os.listdir(start_dir) if file.endswith(".zip")]
    for zip_file_name in zip_file_list:
        new_zip_file_name = zip_file_name[:-len(".zip")]
        for del_char in del_char_list:
            new_zip_file_name = new_zip_file_name.replace(del_char, "")
        while True:
            if "  " in new_zip_file_name:
                new_zip_file_name = new_zip_file_name.replace("  ", "")
            else:
                break
        new_zip_file_name = new_zip_file_name.strip()
        new_zip_file_name = new_zip_file_name[:max_zip_file_name_len] + ".zip"
        os.rename(os.path.join(start_dir, zip_file_name),
                  os.path.join(start_dir, new_zip_file_name))
        zip_file_name = new_zip_file_name

        full_zip_file_path = os.path.join(start_dir, zip_file_name)
        zip_dir_name = zip_file_name[:-4]

        full_zip_dir_path = os.path.join(start_dir, zip_dir_name)
        while True:
            if os.path.isdir(full_zip_dir_path):
                copy_dir_text = "-COPY"
                print(f"WARNING! Directory \"{full_zip_dir_path}\" exists. "
                      f"Adding \"{copy_dir_text}\" to directory name")
                full_zip_dir_path = os.path.join(start_dir, zip_dir_name + copy_dir_text)
            else:
                break
        os.mkdir(full_zip_dir_path)

        zipfile.ZipFile(full_zip_file_path).extractall(path=full_zip_dir_path)

        unpacked_file_list = os.listdir(full_zip_dir_path)
        for unpacked_file_name in unpacked_file_list:
            os.rename(os.path.join(full_zip_dir_path, unpacked_file_name),
                      os.path.join(full_zip_dir_path, zip_dir_name + "-" + unpacked_file_name))

        os.replace(full_zip_file_path, os.path.join(full_zip_dir_path, zip_file_name))

    return


