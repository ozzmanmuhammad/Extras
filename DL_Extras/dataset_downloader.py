def Download_Kaggle_Dataset(dataset_name, extraction_path, type = "competition"):
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
  !rm -r ~/.kaggle
  !mkdir ~/.kaggle
  !mv ./kaggle.json ~/.kaggle/
  !chmod 600 ~/.kaggle/kaggle.json
  !kaggle datasets list

  if type == "competition":
    !kaggle competitions download -c $dataset_name
  elif type == "dataset":
    !kaggle datasets download $dataset_name

  !mkdir $dataset_name
  !unzip "/content/"$dataset_name -d $extraction_path