tests/ui/macros/macro-attribute-expansion.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
macro_rules! descriptions {
    ($name:ident is $desc:expr) => {
        // Check that we will correctly expand attributes
        #[doc = $desc]
        #[allow(dead_code)]
        const $name : &'static str = $desc;
    }
}

// item
descriptions! { DOG is "an animal" }
descriptions! { RUST is "a language" }

pub fn main() {
}


