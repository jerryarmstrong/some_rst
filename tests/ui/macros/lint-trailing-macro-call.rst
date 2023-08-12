tests/ui/macros/lint-trailing-macro-call.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
//
// Ensures that we properly lint
// a removed 'expression' resulting from a macro
// in trailing expression position

macro_rules! expand_it {
    () => {
        #[cfg(FALSE)] 25; //~  WARN trailing semicolon in macro
                          //~| WARN this was previously
    }
}

fn main() {
    expand_it!()
}


