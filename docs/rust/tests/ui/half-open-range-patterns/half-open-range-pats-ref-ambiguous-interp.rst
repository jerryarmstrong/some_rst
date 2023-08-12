tests/ui/half-open-range-patterns/half-open-range-pats-ref-ambiguous-interp.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

#[cfg(FALSE)]
fn syntax() {
    match &0 {
        &0.. | _ => {}
        //~^ ERROR the range pattern here has ambiguous interpretation
        &0..= | _ => {}
        //~^ ERROR the range pattern here has ambiguous interpretation
        //~| ERROR inclusive range with no end
        &0... | _ => {}
        //~^ ERROR inclusive range with no end
    }

    match &0 {
        &..0 | _ => {}
        //~^ ERROR the range pattern here has ambiguous interpretation
        &..=0 | _ => {}
        //~^ ERROR the range pattern here has ambiguous interpretation
        &...0 | _ => {}
        //~^ ERROR the range pattern here has ambiguous interpretation
        //~| ERROR range-to patterns with `...` are not allowed
    }
}


