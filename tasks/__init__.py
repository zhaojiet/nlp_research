import sys,os
ROOT_PATH = '/'.join(os.path.abspath(__file__).split('/')[:-1])
sys.path.append(ROOT_PATH)
from classify import Classify
from classify_m import ClassifyM
from match import Match

dl_tasks = {}
dl_tasks['classify'] = Classify
dl_tasks['match'] = Match


ml_tasks = {}
ml_tasks['classify_m'] = ClassifyM
