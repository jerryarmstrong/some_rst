tests/ui/lint/rfc-2457-non-ascii-idents/lint-mixed-script-confusables.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(mixed_script_confusables)]

struct ΑctuallyNotLatin;
//~^ ERROR the usage of Script Group `Greek` in this crate consists solely of

fn main() {
    let v = ΑctuallyNotLatin;
}

mod роре {
//~^ ERROR the usage of Script Group `Cyrillic` in this crate consists solely of
    const エ: &'static str = "アイウ";
    //~^ ERROR the usage of Script Group `Japanese, Katakana` in this crate consists solely of
}


