tests/ui/closures/closure-return-type-mismatch.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    || {
        if false {
            return "test";
        }
        let a = true;
        a //~ ERROR mismatched types
    };

    || -> bool {
        if false {
            return "hello" //~ ERROR mismatched types
        };
        let b = true;
        b
    };
}


