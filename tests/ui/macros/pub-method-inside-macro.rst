tests/ui/macros/pub-method-inside-macro.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Issue #17436

// pretty-expanded FIXME #23616

mod bleh {
    macro_rules! foo {
        () => {
            pub fn bar(&self) { }
        }
    }

    pub struct S;

    impl S {
        foo!();
    }
}

fn main() {
    bleh::S.bar();
}


