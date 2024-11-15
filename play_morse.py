try:
    from pydub import AudioSegment #type: ignore
    from pydub.playback import play #type: ignore
    import time
except ModuleNotFoundError:
    print("Use your virtual envrioment")
    exit()

morsecode = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

morsemessage = []

def main():
    message=input("Message: ").upper()
    encryption(message)
    signal()

def encryption(m):
    letters=list(m)
    for i in letters:
        morsemessage.append(i)
    for b in range(len(morsemessage)):
        if morsemessage[b] in morsecode:
            morsemessage[b] = morsecode[morsemessage[b]]
            
def signal():
    long = AudioSegment.from_mp3("morselong.mp3")
    short = AudioSegment.from_mp3("morseshort.mp3")
    print(morsemessage)
    if len(morsemessage) > 1:
        for s in morsemessage:
            for char in s:
                if char ==".":
                    play(short)
                if char =="-":
                    play(long)
    else:
        for s in morsemessage:
            if s ==".":
                play(short)
                time.sleep(1)
            elif s=="-":
                play(long)
                time.sleep(1)
     

main()