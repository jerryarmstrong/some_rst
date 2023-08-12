tests/ui/match/match-range-fail.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    match "wow" {
        "bar" ..= "foo" => { }
    };
    //~^^ ERROR only `char` and numeric types are allowed in range

    match "wow" {
        10 ..= "what" => ()
    };
    //~^^ ERROR only `char` and numeric types are allowed in range

    match "wow" {
        true ..= "what" => {}
    };
    //~^^ ERROR only `char` and numeric types are allowed in range

    match 5 {
        'c' ..= 100 => { }
        _ => { }
    };
    //~^^^ ERROR mismatched types
}


