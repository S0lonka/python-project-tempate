import simpleaudio as sa
import simpleaudio

def play(sound_name: str) -> simpleaudio.PlayObject:
    '''Функция проигрывает звук по нужному пути
    
    Args:
        sound_name: имя звукового файла (без расширения)
    '''

    sound_path = f"app/sounds/{sound_name}.wav"

    wave_obj = sa.WaveObject.from_wave_file(sound_path).play()

    return wave_obj # Возвращаем чтобы можно было использовать .wait_done() при вызове


