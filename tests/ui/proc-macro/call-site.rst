tests/ui/proc-macro/call-site.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:call-site.rs

extern crate call_site;

fn main() {
    let x1 = 10;
    call_site::check!(let x2 = x1;);
    let x6 = x5;
}


