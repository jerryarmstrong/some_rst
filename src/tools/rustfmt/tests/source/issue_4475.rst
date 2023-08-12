src/tools/rustfmt/tests/source/issue_4475.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    #[cfg(debug_assertions)]
    { println!("DEBUG"); }
}

fn main() {
    #[cfg(feature = "foo")]
    {
        /*
        let foo = 0
        */
    }
}

fn main() {
    #[cfg(feature = "foo")]
    { /* let foo = 0; */ }
}

fn main() {
    #[foo]
    #[bar]
    #[baz]
    {
        // let foo = 0;
    }
}

