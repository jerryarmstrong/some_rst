tests/ui/consts/const-eval/issue-84957-const-str-as-bytes.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass

trait Foo {}

struct Bar {
    bytes: &'static [u8],
    func: fn(&Box<dyn Foo>),
}
fn example(_: &Box<dyn Foo>) {}

const BARS: &[Bar] = &[
    Bar {
        bytes: "0".as_bytes(),
        func: example,
    },
    Bar {
        bytes: "0".as_bytes(),
        func: example,
    },
];

fn main() {
    let x = todo!();

    for bar in BARS {
        (bar.func)(&x);
    }
}


