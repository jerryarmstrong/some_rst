tests/ui/binding/match-with-ret-arm.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub fn main() {
    // sometimes we have had trouble finding
    // the right type for f, as we unified
    // bot and u32 here
    let f = match "1234".parse::<usize>().ok() {
        None => return (),
        Some(num) => num as u32
    };
    assert_eq!(f, 1234);
    println!("{}", f)
}


