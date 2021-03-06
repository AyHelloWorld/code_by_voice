insert_start_commands = {
    "insert": "i",
    "shift insert": "I",

    "change": "c",
    "change whiskey": "c,w",
    "change inner whiskey": "c,i,w",
    "change character": "c,right",
    "change (echo|end)": "c,e",
    "change a paragraph": "c,a,p",
    "change inner paragraph": "c,i,p",
    "change a (paren|parenthesis|raip|laip)": "c,a,rparen",
    "change inner (paren|parenthesis|raip|laip)": "c,i,rparen",
    "change inner quote": "c,i,dquote",
    "change inner single quote": "c,i,quote",
    "shift change": "C",

    "sub line" : "S",

    "(after | append)": "a",
    "shift (after | append)": "A",

    "oh": "o",
    "shift oh": "O",
    "exec insert": "colon",
    "exec control pee": "colon, C, t, r, l, P, enter",

    "open terminal": "colon, t, e, r, m, enter",
}


insert_end_commands = {
    "okay | kay | abort": "escape",
    "cancel | oops": "cancel",
}
