tests/ui/lexer/lex-bad-char-literals-1.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static c3: char =
    '\x1' //~ ERROR: numeric character escape is too short
;

static s3: &'static str =
    "\x1" //~ ERROR: numeric character escape is too short
;

static c: char =
    '\●' //~ ERROR: unknown character escape
;

static s: &'static str =
    "\●" //~ ERROR: unknown character escape
;

fn main() {}


