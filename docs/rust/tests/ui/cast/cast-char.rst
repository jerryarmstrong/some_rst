tests/ui/cast/cast-char.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(overflowing_literals)]

fn main() {
    const XYZ: char = 0x1F888 as char;
    //~^ ERROR only `u8` can be cast into `char`
    const XY: char = 129160 as char;
    //~^ ERROR only `u8` can be cast into `char`
    const ZYX: char = '\u{01F888}';
    println!("{}", XYZ);
}


