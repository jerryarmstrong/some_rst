tests/ui/half-open-range-patterns/half-open-range-pats-inclusive-no-end.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test `X...` and `X..=` range patterns not being allowed syntactically.
// FIXME(Centril): perhaps these should be semantic restrictions.

fn main() {}

#[cfg(FALSE)]
fn foo() {
    if let 0... = 1 {} //~ ERROR inclusive range with no end
    if let 0..= = 1 {} //~ ERROR inclusive range with no end
    const X: u8 = 0;
    if let X... = 1 {} //~ ERROR inclusive range with no end
    if let X..= = 1 {} //~ ERROR inclusive range with no end
}

fn bar() {
    macro_rules! mac {
        ($e:expr) => {
            let $e...; //~ ERROR inclusive range with no end
            let $e..=; //~ ERROR inclusive range with no end
        }
    }

    mac!(0);
}


