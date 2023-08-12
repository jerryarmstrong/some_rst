tests/ui/codemap_tests/unicode_3.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {
    let s = "ZͨA͑ͦ͒͋ͤ͑̚L̄͑͋Ĝͨͥ̿͒̽̈́Oͥ͛ͭ!̏"; while true { break; } //~ WARNING while_true
    println!("{}", s);
}


