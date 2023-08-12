src/tools/rustfmt/tests/target/configs/brace_style/item_prefer_same_line.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-brace_style: PreferSameLine
// Item brace style

struct Lorem {
    ipsum: bool,
}

struct Dolor<T>
where
    T: Eq, {
    sit: T,
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {}
}


