tests/ui/nll/user-annotations/closure-sig.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test fails if #104478 is fixed before #104477.

// check-pass

struct Printer<'a, 'b>(&'a (), &'b ());

impl Printer<'_, '_> {
    fn test(self) {
        let clo = |_: &'_ Self| {};
        clo(&self);
        clo(&self);
    }
}

fn main() {}


