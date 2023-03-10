import pathlib
import fastbook
import io
fastbook.setup_book()
from fastbook import *
from fastai.vision.all import *


def translate(prediction):
 trasnlation = ""
 if prediction == "concealer_png" : translation = "Консиллер"
 elif prediction == "cream_blush" : translation = "Румяна"
 elif prediction == "eyeliner_liquid_png" : translation = "Жидкую подводку"
 elif prediction == "face_powder_png" : translation = "Пудра для лица"
 elif prediction == "foundation_cream" : translation = "Тональник"
 elif prediction == "lipstick_png" : translation = "Помаду"
 elif prediction == "makeup_sponge" : translation = "Спондж"
 elif prediction == "mascara" : translation = "Тушь для ресниц"
 elif prediction == "palette_makeup" : translation = "Палетку"
 return "Мне кажется, что это похоже на " + translation

def Predict(image_file_url):
 byte_file = io.BytesIO()
 if os.name == "nt":
  pathlib.PosixPath = pathlib.WindowsPath
 path = Path(os.getcwd())
 path = os.path.join(path,'FinalAI.pkl')
 learn_inf = load_learner(path)
 byte_file.write(requests.get(image_file_url).content)
 img = PILImage.create(byte_file)
 pred, pred_idx, probs = learn_inf.predict(img)
 del byte_file
 return translate(pred)