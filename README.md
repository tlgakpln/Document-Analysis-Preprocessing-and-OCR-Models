# Document-Analysis-Preprocessing-and-OCR-Models

Installed 
> Pyhton 3.10.12

You need to install the system requirements.
> pip install -r requirements.txt

You should download tesseract.exe
> https://digi.bib.uni-mannheim.de/tesseract/
You need to specify the place where you installed the tesseract from the paths.

Original Image

![gray_img](https://github.com/tlgakpln/Document-Analysis-Preprocessing-and-OCR-Models/assets/46111780/beb1da3b-7579-4008-8f83-0360e4d6d2b5)

If your image not in fullscreen and need any preprocess steps
>  scanner.py

After Preprocess
![processed](https://github.com/tlgakpln/Document-Analysis-Preprocessing-and-OCR-Models/assets/46111780/ab3b05da-51f2-4b20-877f-8609fbd2c4be)

When we crop the image, the orientation of the image can be horizontal or upside down.
We had different solve about these problems
If you want to best solve for rotation you should use
> best_rotation_method.py

Rotated Image
![rotated](https://github.com/tlgakpln/Document-Analysis-Preprocessing-and-OCR-Models/assets/46111780/dba526b9-15ad-4605-9641-1dbf00464ed2)

Everything is ready for OCR algorithms. I used three different models.
> Pytesseract
> PaddleOCR
> EasyOCR

You can choose any models ouputs

Just run!
> ocr.py
