from flask import Flask, render_template, request

app = Flask(__name__)


char_map = {
    "A": "`?=2f", "B": "daj28?", "C": "z!f7L", "D": "5@Kcm", "E": "0w!d#", "F": "q#92D", "G": "8Zx$r", "H": "~3dLz",
    "I": "pl?X7", "J": "*d(1!", "K": "QWz@#", "L": "m33$", "M": "==Jd@", "N": "?e&y2", "O": "Yx#41", "P": "bv73$",
    "Q": "19X?*", "R": "0!jk2", "S": "t%83v", "T": "&3@rZ", "U": "#d8U*", "V": "we!@8", "W": "z3&vX", "X": "q1t$!",
    "Y": "Wq*12", "Z": "r@82J",
    "Ä": "92!a=", "Ö": "mf*0q", "Ü": "1D@#r", "Õ": "?qp92",
    "a": "s1df#", "b": "mz29@", "c": "odx!2", "d": "&f8==", "e": "#lwp3", "f": "x8@z1", "g": "zv71#", "h": "q9*0a",
    "i": "vv@*2", "j": "q!u7z", "k": "q2W1z", "l": "rr#2!", "m": "nW!8e", "n": "@71df", "o": "ddx@2", "p": "~f*91",
    "q": "90@#z", "r": "!zq@8", "s": "slW@0", "t": "r0*9Z", "u": "#aW7v", "v": "zzq*!8", "w": "2qX!!", "x": "*e91z",
    "y": "73v@#", "z": "Zxq2!", "ä": "qp!92", "ö": "dd*aa", "ü": "#zo12", "õ": "rz#0v",
    "0": "zZ0!q", "1": "92w#f", "2": "@fj91", "3": "*qod3", "4": "0d@x2", "5": "q#o83", "6": "&zj*1", "7": "!02q#", 
    "8": "c@W88", "9": "ddo*!",
    "`": "~1!df", "~": "!q@w1", "!": "*0==w", "@": "c8!@z", "#": "x9q2*", "$": "pq#81", "%": "r!z*1", "^": "0v*!3",
    "&": "&2w@*", "*": "81*#q", "(": "zq12!", ")": "dq!82", "-": "~!*1z", "_": "0x@9!", "=": "x2#dd", "+": "*@z91",
    "[": "!0&@q", "{": "pp*q2", "]": "3z!d@", "}": "88z*1", "\\": "@@*q2", "|": "Z9!q1", ";": "zpq&@", ":": "q2*!w",
    "'": "xzq#0", "\"": "*9z&@", ",": "pq0z!", "<": "!qx8@", ".": "zWq*!1", ">": "#@z02", "/": "81&q@", "?": "r!*@z",
    " ": "0@8hj"
}
UNKNOWN_CODE = "XXXXX"
char_map["<unknown>"] = UNKNOWN_CODE
reverse_map = {v: k for k, v in char_map.items()}
reverse_map[UNKNOWN_CODE] = "<null>"


def encrypt_text(text):
    return ''.join(char_map.get(char, UNKNOWN_CODE) for char in text)


def decrypt_text(code):
    return ''.join(reverse_map.get(code[i:i+5], "<null>") for i in range(0, len(code), 5))

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        action = request.form.get("action")
        user_text = request.form.get("text")
        if action == "encrypt":
            result = encrypt_text(user_text)
        elif action == "decrypt":
            result = decrypt_text(user_text)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
