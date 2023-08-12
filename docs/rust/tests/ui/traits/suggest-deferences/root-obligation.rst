tests/ui/traits/suggest-deferences/root-obligation.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn get_vowel_count(string: &str) -> usize {
    string
        .chars()
        .filter(|c| "aeiou".contains(c))
        //~^ ERROR expected a `Fn<(char,)>` closure, found `char`
        .count()
}

fn main() {
    let _ = get_vowel_count("asdf");
}


