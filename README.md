# Document-Analysis-Preprocessing-and-OCR-Models

Installed 
> Pyhton 3.10.12

You need to install the system requirements.
> pip install -r requirements.txt

You should download tesseract.exe
> https://digi.bib.uni-mannheim.de/tesseract/
You need to specify the place where you installed the tesseract from the paths.

If your image not in fullscreen and need any preprocess steps
>  scanner.py 

When we crop the image, the orientation of the image can be horizontal or upside down.
We had different solve about these problems
If you want to best solve for rotation you should use
> best_rotation_method.py

Everything is ready for OCR algorithms. I used three different models.
> Pytesseract
> PaddleOCR
> EasyOCR

You can choose any models ouputs
After just run!
> ocr.py
