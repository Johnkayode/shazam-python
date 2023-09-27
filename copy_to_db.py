import glob
from typing import List, Dict, Tuple
# from tqdm import tqdm
import pickle
from main import create_constellation, create_hashes


songs = glob.glob('data/samples/*.wav')
song_name_index = {}
database: Dict[int, List[Tuple[int, int]]] = {}