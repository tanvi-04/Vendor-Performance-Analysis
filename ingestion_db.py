{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ba55c13b-a7fa-462f-8944-8906e3f002d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "from sqlalchemy import create_engine\n",
    "import logging\n",
    "import time\n",
    "\n",
    "logging.basicConfig(\n",
    "    filename=\"logs/ingestion_db.log\",\n",
    "    level=logging.DEBUG,\n",
    "    format=\"%(asctime)s - %(levelname)s - %(message)s\",\n",
    "    filemode=\"a\"\n",
    ")\n",
    "\n",
    "\n",
    "engine = create_engine('sqlite:///inventory.db')\n",
    "\n",
    "def ingest_db(df, table_name, engine):\n",
    "    '''This function will ingest the dataframe into database table'''\n",
    "    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)\n",
    "\n",
    "def load_raw_data(): \n",
    "    '''This function will load the CSVs as dataframe and ingest into db'''\n",
    "    start = time.time()\n",
    "    for file in os.listdir('data'):\n",
    "        if '.csv' in file:\n",
    "            df = pd.read_csv('data/'+file)\n",
    "            logging.info(f'Ingesting {file} in db')\n",
    "            ingest_db(df, file[:-4], engine)\n",
    "    end = time.time()\n",
    "    total_time = (end - start)/60\n",
    "    logging.info('Ingestion Complete')\n",
    "    logging.info(f'\\nTotal time taken: {total_time} minutes')\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    load_raw_data()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
