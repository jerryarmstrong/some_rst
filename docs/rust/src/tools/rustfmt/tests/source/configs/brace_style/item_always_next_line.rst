src/tools/rustfmt/tests/source/configs/brace_style/item_always_next_line.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-brace_style: AlwaysNextLine
// Item brace style

enum Foo {}

struct Bar {}

struct Lorem {
    ipsum: bool,
}

struct Dolor<T> where T: Eq {
    sit: T,
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {}
}


