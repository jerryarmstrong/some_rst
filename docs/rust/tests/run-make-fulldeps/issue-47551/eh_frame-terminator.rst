tests/run-make-fulldeps/issue-47551/eh_frame-terminator.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[derive(Clone, Copy)]
struct Foo {
    array: [u64; 10240],
}

impl Foo {
    const fn new() -> Self {
        Self {
            array: [0x1122_3344_5566_7788; 10240]
        }
    }
}

static BAR: [Foo; 10240] = [Foo::new(); 10240];

fn main() {
    let bt = std::backtrace::Backtrace::force_capture();
    println!("Hello, world! {:?}", bt);
    println!("{:x}", BAR[0].array[0]);
}


