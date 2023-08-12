tests/ui/lint/rfc-2457-non-ascii-idents/lint-mixed-script-confusables-2.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![deny(mixed_script_confusables)]

struct ΑctuallyNotLatin;

fn main() {
    let λ = 42; // this usage of Greek confirms that Greek is used intentionally.
}

mod роре {
    const エ: &'static str = "アイウ";

    // this usage of Katakana confirms that Katakana is used intentionally.
    fn ニャン() {
        let д: usize = 100; // this usage of Cyrillic confirms that Cyrillic is used intentionally.

        println!("meow!");
    }
}


