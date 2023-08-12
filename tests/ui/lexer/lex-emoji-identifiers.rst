tests/ui/lexer/lex-emoji-identifiers.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn invalid_emoji_usages() {
    let arrow↔️ = "basic emoji"; //~ ERROR: identifiers cannot contain emoji
    // FIXME
    let planet🪐 = "basic emoji"; //~ ERROR: unknown start of token
    // FIXME
    let wireless🛜 = "basic emoji"; //~ ERROR: unknown start of token
    // FIXME
    let key1️⃣ = "keycap sequence"; //~ ERROR: unknown start of token
                                    //~^ WARN: identifier contains uncommon Unicode codepoints
    let flag🇺🇳 = "flag sequence"; //~ ERROR: identifiers cannot contain emoji
    let wales🏴 = "tag sequence"; //~ ERROR: identifiers cannot contain emoji
    let folded🙏🏿 = "modifier sequence"; //~ ERROR: identifiers cannot contain emoji
}

fn main() {
    invalid_emoji_usages();
}


