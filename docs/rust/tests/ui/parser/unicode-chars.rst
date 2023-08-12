tests/ui/parser/unicode-chars.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let y = 0;
    //~^ ERROR unknown start of token: \u{37e}
    //~^^ HELP Unicode character ';' (Greek Question Mark) looks like ';' (Semicolon), but it is not
        let x = 0;
    //~^ ERROR unknown start of token: \u{a0}
    //~^^ NOTE character appears 3 more times
    //~^^^ HELP Unicode character ' ' (No-Break Space) looks like ' ' (Space), but it is not
    let _ = 1 ⩵ 2;
    //~^ ERROR unknown start of token
    //~^^ HELP Unicode character '⩵' (Two Consecutive Equals Signs) looks like '==' (Double Equals Sign), but it is not
}


