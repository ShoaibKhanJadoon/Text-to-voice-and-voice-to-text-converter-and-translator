from googletrans import Translator


class translation:
    def __init__(self):
        self.translator = Translator()

    def translate_to_persion(self,text):
        # Translate English to Persian
        translated = self.translator.translate(text, dest='fa')
        # Print the translated text

        print(f"Translated text: {translated.text}")
        return translated.text

