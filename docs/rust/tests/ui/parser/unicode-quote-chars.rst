tests/ui/parser/unicode-quote-chars.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    println!(“hello world”);
    //~^ ERROR unknown start of token: \u{201c}
    //~^^ HELP Unicode characters '“' (Left Double Quotation Mark) and '”' (Right Double Quotation Mark) look like '"' (Quotation Mark), but are not
    //~^^^ ERROR unknown start of token: \u{201d}
    //~^^^^ HELP Unicode character '”' (Right Double Quotation Mark) looks like '"' (Quotation Mark), but it is not
    //~^^^^^ ERROR expected `,`, found `world`
}


