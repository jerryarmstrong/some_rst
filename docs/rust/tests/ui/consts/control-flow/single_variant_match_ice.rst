tests/ui/consts/control-flow/single_variant_match_ice.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

enum Foo {
    Prob,
}

const FOO: u32 = match Foo::Prob {
    Foo::Prob => 42,
};

const BAR: u32 = match Foo::Prob {
    x => 42,
};

impl Foo {
    pub const fn as_val(&self) -> u8 {
        use self::Foo::*;

        match *self {
            Prob => 0x1,
        }
    }
}

fn main() {}


