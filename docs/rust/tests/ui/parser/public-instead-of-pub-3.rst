tests/ui/parser/public-instead-of-pub-3.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
mod test {
    public const X: i32 = 123;
    //~^ ERROR expected one of `!` or `::`, found keyword `const`
}

fn main() {
    println!("{}", test::X);
}


