tests/ui/borrowck/borrowck-uninit-ref-chain.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S<X, Y> {
    x: X,
    y: Y,
}

fn main() {
    let x: &&Box<i32>;
    let _y = &**x; //~ ERROR [E0381]

    let x: &&S<i32, i32>;
    let _y = &**x; //~ ERROR [E0381]

    let x: &&i32;
    let _y = &**x; //~ ERROR [E0381]


    let mut a: S<i32, i32>;
    a.x = 0; //~ ERROR [E0381]
    let _b = &a.x;

    let mut a: S<&&i32, &&i32>;
    a.x = &&0; //~ ERROR [E0381]
    let _b = &**a.x;


    let mut a: S<i32, i32>;
    a.x = 0; //~ ERROR [E0381]
    let _b = &a.y;

    let mut a: S<&&i32, &&i32>;
    a.x = &&0; //~ ERROR [E0381]
    let _b = &**a.y;
}


