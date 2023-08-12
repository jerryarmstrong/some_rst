tests/run-make-fulldeps/issue-20626/foo.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn identity(a: &u32) -> &u32 { a }

fn print_foo(f: &fn(&u32) -> &u32, x: &u32) {
    print!("{}", (*f)(x));
}

fn main() {
    let x = &4;
    let f: fn(&u32) -> &u32 = identity;

    // Didn't print 4 on optimized builds
    print_foo(&f, x);
}


