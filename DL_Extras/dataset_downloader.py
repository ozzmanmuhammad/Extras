def Download_Kaggle_Dataset(dataset_name, extraction_path, type = "competition"):
  import os
  """
  Takes the competition or dataset name and downloads it into the colab's content space.
  Note: Before using this function please download the kaggle.json or API key from the kaggle.
  Parameters
  ----------
  dataset_name (str): string name of target dataset
  extraction_path(str): path to extract the dataset
  type (str): whether to download competition dataset or simple dataset, default competition
              options: competition or dataset.
  """
  os.system('rm -r ~/.kaggle')
  os.system('mkdir ~/.kaggle')
  os.system('mv ./kaggle.json ~/.kaggle/')
  os.system('chmod 600 ~/.kaggle/kaggle.json')
  os.system('kaggle datasets list')

  if type == "competition":
    os.system(f'kaggle competitions download -c {dataset_name}')
  elif type == "dataset":
    os.system(f'kaggle datasets download {dataset_name}')

  if len(dataset_name.split('/')) == 2:
    dataset_name = dataset_name.split('/')[1]
    os.system(f'unzip "/content/"{dataset_name} -d {extraction_path}')
  elif len(dataset_name.split('/')) == 1:
    os.system(f'unzip "/content/"{dataset_name} -d {extraction_path}')
