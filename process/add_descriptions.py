import os
from IO_file import IO_file
import pandas

io_file = IO_file()

def add_description(path, description_path):
  data_type = path.rsplit('/', 1)[1][:-5]
  description = io_file.load(description_path)
  data = io_file.load(path)
  if data_type == 'variable':
    data = pandas.merge(data, description, how='left', left_on='var_name_origin', right_on='variable')
    for i, row in data.iterrows():
      if row['description_y'] != '':
        data.at[i, 'description'] = row['description_y']
      else:
        data.at[i, 'description'] = row['description_x']
    data = data.drop(columns=['description_y', 'description_x', 'variable'])
  else: 
    data['description'] = description['description']
  
  io_file.save(path, data)

  path_len = 3 if data_type == 'database' else 4
  name = '/'.join(path.rsplit('/', path_len)[1:-1])
  print(data_type, 'description added for:', name)


add_description(
  "/Users/bassim/Documents/github/catalog_desktop/data/databases/open_data/geneve/batiment/variable.xlsx",
  "/Users/bassim/Documents/dr/data/open_data/open_data_swiss/geneve/CSV_OCS_BATLOG_SSECTEUR/variables_description.xlsx"
)
add_description(
  "/Users/bassim/Documents/github/catalog_desktop/data/databases/open_data/geneve/batiment/table.xlsx",
  "/Users/bassim/Documents/dr/data/open_data/open_data_swiss/geneve/CSV_OCS_BATLOG_SSECTEUR/table_description.xlsx"
)

add_description(
  "/Users/bassim/Documents/github/catalog_desktop/data/databases/open_data/geneve/accident/variable.xlsx",
  "/Users/bassim/Documents/dr/data/open_data/open_data_swiss/geneve/CSV_OTC_ACCIDENTS/variables_description.xlsx"
)
add_description(
  "/Users/bassim/Documents/github/catalog_desktop/data/databases/open_data/geneve/accident/table.xlsx",
  "/Users/bassim/Documents/dr/data/open_data/open_data_swiss/geneve/CSV_OTC_ACCIDENTS/table_description.xlsx"
)

add_description(
  "/Users/bassim/Documents/github/catalog_desktop/data/databases/open_data/geneve/batiment_depense_chaleur/variable.xlsx",
  "/Users/bassim/Documents/dr/data/open_data/open_data_swiss/geneve/CSV_SCANE_INDICE_DERNIER_2/variables_description.xlsx"
)
add_description(
  "/Users/bassim/Documents/github/catalog_desktop/data/databases/open_data/geneve/batiment_depense_chaleur/table.xlsx",
  "/Users/bassim/Documents/dr/data/open_data/open_data_swiss/geneve/CSV_SCANE_INDICE_DERNIER_2/table_description.xlsx"
)


add_description(
  "/Users/bassim/Documents/github/catalog_desktop/data/databases/open_data/geneve/database.xlsx",
  "/Users/bassim/Documents/dr/data/open_data/open_data_swiss/geneve/database_description.xlsx"
)