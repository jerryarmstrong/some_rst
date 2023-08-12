tests/testsuite/init/fossil_autodetect/out/src/lib.rs
=====================================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}


